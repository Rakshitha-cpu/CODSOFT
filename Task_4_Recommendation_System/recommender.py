from pathlib import Path
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobRecommender:

    def __init__(self, data_path=None):

        # Locate jobs.csv relative to this Python file
        current_dir = Path(__file__).resolve().parent

        if data_path is not None:
            csv_path = Path(data_path)
            if not csv_path.is_absolute():
                csv_path = current_dir / csv_path
        else:
            csv_path = current_dir / "jobs.csv"

        if not csv_path.is_file():
            raise FileNotFoundError(
                f"Dataset not found: {csv_path}. "
                "Upload jobs.csv into Task_4_Recommendation_System."
            )

        # Load dataset
        self.jobs = pd.read_csv(csv_path)

        required_columns = [
            "job_id",
            "job_title",
            "company",
            "location",
            "experience_level",
            "skills",
            "description",
        ]

        missing_columns = [
            col for col in required_columns
            if col not in self.jobs.columns
        ]

        if missing_columns:
            raise ValueError(
                "Missing CSV columns: "
                + ", ".join(missing_columns)
            )

        if self.jobs.empty:
            raise ValueError("jobs.csv contains no job records.")

        self.jobs = self.jobs.dropna(
            subset=["job_title"]
        ).reset_index(drop=True)

        # Clean text columns
        text_columns = [
            "job_title",
            "company",
            "location",
            "experience_level",
            "skills",
            "description",
        ]

        for col in text_columns:
            self.jobs[col] = (
                self.jobs[col].fillna("").astype(str)
            )

        # Combine features for content-based recommendations
        self.jobs["combined_features"] = (
            self.jobs["job_title"] + " "
            + self.jobs["skills"] + " "
            + self.jobs["experience_level"] + " "
            + self.jobs["location"] + " "
            + self.jobs["description"]
        )

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.feature_matrix = self.vectorizer.fit_transform(
            self.jobs["combined_features"]
        )

    # Extract individual skills
    @staticmethod
    def _skill_set(text):
        return {
            token.lower()
            for token in re.findall(
                r"[a-zA-Z][a-zA-Z0-9+#.-]*",
                str(text)
            )
        }

    # Get available job titles
    def get_job_titles(self):
        return sorted(
            self.jobs["job_title"].unique().tolist()
        )

    # Get available locations
    def get_locations(self):
        return sorted(
            self.jobs["location"].unique().tolist()
        )

    # Get available experience levels
    def get_experience_levels(self):
        return sorted(
            self.jobs["experience_level"].unique().tolist()
        )

    # Get details for a selected job
    def get_job_details(self, job_title):
        matching = self.jobs[
            self.jobs["job_title"] == job_title
        ]

        if matching.empty:
            return None

        return matching.iloc[0].to_dict()

    # Find missing skills for a selected role
    def analyze_skill_gap(self, user_skills, job_title):
        job = self.get_job_details(job_title)

        if job is None:
            return []

        required = self._skill_set(job["skills"])
        provided = self._skill_set(user_skills)

        return sorted(required - provided)

    # Apply location and experience filters
    def _filter_jobs(
        self,
        results,
        location_filter="All",
        experience_filter="All"
    ):

        if results.empty:
            return results

        if location_filter and location_filter != "All":
            results = results[
                results["location"].str.casefold()
                == str(location_filter).casefold()
            ]

        if experience_filter and experience_filter != "All":
            results = results[
                results["experience_level"].str.casefold()
                == str(experience_filter).casefold()
            ]

        return results.copy()

    # Add match percentage and skill-gap details
    def _add_match_details(self, results, user_skills):

        if results.empty:
            return results

        user_skill_set = self._skill_set(user_skills)

        match_scores = []
        matched_skills_list = []
        missing_skills_list = []

        for _, job in results.iterrows():

            required_skills = self._skill_set(job["skills"])

            matched = sorted(
                user_skill_set & required_skills
            )

            missing = sorted(
                required_skills - user_skill_set
            )

            if required_skills:
                skill_score = (
                    len(matched) / len(required_skills)
                ) * 100
            else:
                skill_score = 0.0

            # Combine content similarity and skill overlap
            similarity = float(
                job.get("similarity_score", 0.0)
            ) * 100

            score = (
                0.6 * skill_score
                + 0.4 * similarity
            )

            match_scores.append(round(score, 2))
            matched_skills_list.append(
                ", ".join(matched) if matched else "None"
            )
            missing_skills_list.append(
                ", ".join(missing) if missing else "None"
            )

        results["match_score"] = match_scores
        results["matched_skills"] = matched_skills_list
        results["missing_skills"] = missing_skills_list

        return results.sort_values(
            "match_score",
            ascending=False
        ).reset_index(drop=True)

    # Recommend jobs using the candidate's skills
    def recommend_by_skills(
        self,
        user_skills,
        top_n=5,
        location_filter="All",
        experience_filter="All"
    ):

        if not user_skills or not user_skills.strip():
            return pd.DataFrame()

        # Compare candidate skills against every job
        user_vector = self.vectorizer.transform(
            [user_skills]
        )

        scores = cosine_similarity(
            user_vector,
            self.feature_matrix
        ).flatten()

        results = self.jobs.copy()

        results["similarity_score"] = scores

        # Apply selected filters
        results = self._filter_jobs(
            results,
            location_filter,
            experience_filter
        )

        if results.empty:
            return results

        # Calculate match score and skill gaps
        results = self._add_match_details(
            results,
            user_skills
        )

        return results.head(int(top_n)).reset_index(drop=True)

    # Recommend jobs similar to the selected role
    def recommend_by_job_title(
        self,
        job_title,
        top_n=5,
        location_filter="All",
        experience_filter="All"
    ):

        matching = self.jobs.index[
            self.jobs["job_title"] == job_title
        ].tolist()

        if not matching:
            return pd.DataFrame()

        selected_index = matching[0]

        # Compare the selected job with other jobs
        scores = cosine_similarity(
            self.feature_matrix[selected_index],
            self.feature_matrix
        ).flatten()

        results = self.jobs.copy()

        results["similarity_score"] = scores

        # Exclude the selected job itself
        results = results[
            results.index != selected_index
        ]

        # Apply selected filters
        results = self._filter_jobs(
            results,
            location_filter,
            experience_filter
        )

        if results.empty:
            return results

        # Use the selected role's skills for gap analysis
        selected_skills = self.jobs.iloc[
            selected_index
        ]["skills"]

        results = self._add_match_details(
            results,
            selected_skills
        )

        return results.head(int(top_n)).reset_index(drop=True)
