from pathlib import Path
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobRecommender:
    """Skill-based and job-title-based recommendation engine."""

    def __init__(self, data_path=None):
        if data_path is None:
            data_path = Path(__file__).resolve().parent / "jobs.csv"

        self.data_path = Path(data_path)

        # Load the dataset and expose both attribute names.
        self.jobs_df = self._load_jobs()
        self.jobs = self.jobs_df

    def _load_jobs(self):
        """Load and normalize the job dataset."""

        if not self.data_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.data_path}"
            )

        df = pd.read_csv(self.data_path)

        # Normalize column names.
        df.columns = [
            str(column).strip().lower().replace(" ", "_")
            for column in df.columns
        ]

        # Support alternative dataset column names.
        aliases = {
            "title": "job_title",
            "role": "job_title",
            "job_role": "job_title",
            "company_name": "company",
            "employer": "company",
            "city": "location",
            "experience": "experience_level",
            "required_skills": "skills",
            "job_skills": "skills",
            "job_description": "description",
        }

        for old_name, new_name in aliases.items():
            if old_name in df.columns and new_name not in df.columns:
                df.rename(columns={old_name: new_name}, inplace=True)

        defaults = {
            "job_id": "",
            "job_title": "Untitled Job",
            "company": "Company Not Specified",
            "location": "Not Specified",
            "experience_level": "Not Specified",
            "skills": "",
            "description": "",
        }

        for column, default in defaults.items():
            if column not in df.columns:
                df[column] = default

        df = df[list(defaults.keys())].copy()

        for column in df.columns:
            df[column] = df[column].fillna("").astype(str).str.strip()

        df["job_title"] = df["job_title"].replace("", "Untitled Job")
        df["company"] = df["company"].replace(
            "", "Company Not Specified"
        )
        df["location"] = df["location"].replace("", "Not Specified")
        df["experience_level"] = df["experience_level"].replace(
            "", "Not Specified"
        )

        df = df.drop_duplicates(
            subset=["job_title", "company", "location"]
        )

        if df.empty:
            raise ValueError("The jobs.csv file contains no job records.")

        return df.reset_index(drop=True)

    @staticmethod
    def _normalize(text):
        """Normalize text for comparison."""

        text = str(text).lower().strip()
        text = text.replace("&", " and ")
        text = re.sub(r"[^a-z0-9+#. ]+", " ", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @classmethod
    def _parse_skills(cls, value):
        """
        Parse skills written with commas or spaces.

        Recognizes common multiword skills before splitting
        the remaining text into individual skills.
        """

        text = str(value or "").lower().strip()

        if not text:
            return []

        text = text.replace("\n", ",").replace(";", ",").replace("|", ",")

        multiword_skills = [
            "machine learning",
            "deep learning",
            "data science",
            "data analysis",
            "data analytics",
            "natural language processing",
            "computer vision",
            "artificial intelligence",
            "spring boot",
            "android studio",
            "react native",
            "web development",
            "software development",
            "object oriented programming",
            "data structures",
            "operating systems",
            "cloud computing",
            "microsoft azure",
            "amazon web services",
            "google cloud",
            "rest api",
            "rest apis",
            "power bi",
            "node js",
            "next js",
            "user interface",
            "user experience",
            "problem solving",
            "critical thinking",
        ]

        for phrase in sorted(multiword_skills, key=len, reverse=True):
            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(phrase)
                + r"(?![a-z0-9])"
            )

            text = re.sub(
                pattern,
                phrase.replace(" ", "_"),
                text,
            )

        # Support comma-separated and space-separated input.
        tokens = re.split(r"[, ]+", text)

        skills = []

        for token in tokens:
            token = token.strip()

            if not token:
                continue

            skill = cls._normalize(token.replace("_", " "))

            if skill and skill not in skills:
                skills.append(skill)

        return skills

    @staticmethod
    def _text_similarity(query, jobs_df):
        """Calculate TF-IDF cosine similarity."""

        if jobs_df.empty or not str(query).strip():
            return [0.0] * len(jobs_df)

        job_text = (
            jobs_df["job_title"].fillna("")
            + " "
            + jobs_df["skills"].fillna("")
            + " "
            + jobs_df["description"].fillna("")
        ).tolist()

        try:
            vectorizer = TfidfVectorizer(
                lowercase=True,
                stop_words="english",
                ngram_range=(1, 2),
                token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9+#.]*\b",
            )

            matrix = vectorizer.fit_transform(job_text + [str(query)])
            similarities = cosine_similarity(
                matrix[-1],
                matrix[:-1],
            ).flatten()

            return (similarities * 100).tolist()

        except ValueError:
            return [0.0] * len(jobs_df)

    def _apply_filters(
        self,
        location_filter="All",
        experience_filter="All",
    ):
        """Filter the dataset by location and experience."""

        df = self.jobs_df.copy()

        if location_filter and location_filter != "All":
            df = df[
                df["location"].str.casefold()
                == str(location_filter).casefold()
            ]

        if experience_filter and experience_filter != "All":
            df = df[
                df["experience_level"].str.casefold()
                == str(experience_filter).casefold()
            ]

        return df.reset_index(drop=True)

    def _recommend(
        self,
        query,
        user_skills,
        top_n=5,
        location_filter="All",
        experience_filter="All",
    ):
        """Generate and rank job recommendations."""

        df = self._apply_filters(
            location_filter=location_filter,
            experience_filter=experience_filter,
        )

        if df.empty:
            df["skill_score"] = pd.Series(dtype=float)
            df["similarity_score"] = pd.Series(dtype=float)
            df["match_score"] = pd.Series(dtype=float)
            df["matched_skills"] = pd.Series(dtype=str)
            df["missing_skills"] = pd.Series(dtype=str)
            return df

        user_skill_list = self._parse_skills(user_skills)
        user_skill_set = set(user_skill_list)

        similarity_scores = self._text_similarity(query, df)

        skill_scores = []
        matched_results = []
        missing_results = []
        final_scores = []

        for index, (_, job) in enumerate(df.iterrows()):
            required_skills = self._parse_skills(job["skills"])
            required_set = set(required_skills)

            matched = sorted(user_skill_set.intersection(required_set))
            missing = sorted(required_set.difference(user_skill_set))

            if required_set:
                skill_score = (
                    len(matched) / len(required_set)
                ) * 100
            else:
                skill_score = 0.0

            similarity_score = similarity_scores[index]

            # Skills contribute 80%; text similarity contributes 20%.
            match_score = (
                0.80 * skill_score
                + 0.20 * similarity_score
            )

            skill_scores.append(round(skill_score, 2))
            matched_results.append(
                ", ".join(matched) if matched else "None"
            )
            missing_results.append(
                ", ".join(missing) if missing else "None"
            )
            final_scores.append(round(match_score, 2))

        df["skill_score"] = skill_scores
        df["similarity_score"] = [
            round(score, 2) for score in similarity_scores
        ]
        df["match_score"] = final_scores
        df["matched_skills"] = matched_results
        df["missing_skills"] = missing_results

        df = df.sort_values(
            by=["match_score", "skill_score"],
            ascending=False,
        )

        return df.head(max(1, int(top_n))).reset_index(drop=True)

    def recommend_by_skills(
        self,
        user_skills,
        top_n=5,
        location_filter="All",
        experience_filter="All",
    ):
        """Recommend jobs based on user-entered skills."""

        skills = self._parse_skills(user_skills)

        if not skills:
            return pd.DataFrame()

        query = " ".join(skills)

        return self._recommend(
            query=query,
            user_skills=user_skills,
            top_n=top_n,
            location_filter=location_filter,
            experience_filter=experience_filter,
        )

    def recommend_by_job_title(
        self,
        job_title,
        top_n=5,
        location_filter="All",
        experience_filter="All",
    ):
        """Recommend jobs based on a desired job title."""

        if not str(job_title).strip():
            return pd.DataFrame()

        return self._recommend(
            query=str(job_title).strip(),
            user_skills="",
            top_n=top_n,
            location_filter=location_filter,
            experience_filter=experience_filter,
                )
