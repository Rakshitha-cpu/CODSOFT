from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobRecommender:

    def __init__(self, data_path=None):

        # Locate the directory containing this Python file
        current_dir = Path(__file__).resolve().parent

        # Check possible locations for jobs.csv
        possible_paths = []

        if data_path is not None:
            possible_paths.append(Path(data_path))

        possible_paths.extend([
            current_dir / "jobs.csv",
            current_dir / "data" / "jobs.csv",
            current_dir.parent / "jobs.csv",
            current_dir.parent.parent / "jobs.csv",
        ])

        # Select the first existing dataset
        csv_path = None

        for path in possible_paths:
            if path.is_file():
                csv_path = path
                break

        # Give a clear error if the dataset is missing
        if csv_path is None:
            checked_paths = "\n".join(
                str(path.resolve()) for path in possible_paths
            )

            raise FileNotFoundError(
                "Could not find jobs.csv.\n\n"
                "Please create or upload jobs.csv inside:\n"
                f"{current_dir}\n\n"
                "Locations checked:\n"
                f"{checked_paths}"
            )

        # Load the dataset
        self.jobs = pd.read_csv(csv_path)

        # Validate the required columns
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
            column
            for column in required_columns
            if column not in self.jobs.columns
        ]

        if missing_columns:
            raise ValueError(
                "jobs.csv is missing these required columns: "
                + ", ".join(missing_columns)
            )

        if self.jobs.empty:
            raise ValueError(
                "jobs.csv contains no job records."
            )

        # Remove rows without job titles
        self.jobs = self.jobs.dropna(
            subset=["job_title"]
        ).reset_index(drop=True)

        # Replace missing text values
        text_columns = [
            "job_title",
            "company",
            "location",
            "experience_level",
            "skills",
            "description",
        ]

        for column in text_columns:
            self.jobs[column] = (
                self.jobs[column]
                .fillna("")
                .astype(str)
            )

        # Combine relevant fields for recommendation
        self.jobs["combined_features"] = (
            self.jobs["job_title"] + " "
            + self.jobs["skills"] + " "
            + self.jobs["experience_level"] + " "
            + self.jobs["location"] + " "
            + self.jobs["description"]
        )

        # Convert job information into TF-IDF vectors
        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.feature_matrix = (
            self.vectorizer.fit_transform(
                self.jobs["combined_features"]
            )
        )

    # Return all available job titles
    def get_job_titles(self):
        return sorted(
            self.jobs["job_title"].unique().tolist()
        )

    # Return all available locations
    def get_locations(self):
        return sorted(
            self.jobs["location"].unique().tolist()
        )

    # Return all available experience levels
    def get_experience_levels(self):
        return sorted(
            self.jobs["experience_level"].unique().tolist()
        )

    # Return details for a selected job
    def get_job_details(self, job_title):

        matching_jobs = self.jobs[
            self.jobs["job_title"] == job_title
        ]

        if matching_jobs.empty:
            return None

        return matching_jobs.iloc[0].to_dict()

    # Identify skills that may be missing
    def analyze_skill_gap(
        self,
        user_skills,
        job_title
    ):

        job = self.get_job_details(job_title)

        if job is None:
            return []

        required_skills = {
            skill.strip().lower()
            for skill in job["skills"].split()
            if skill.strip()
        }

        provided_skills = {
            skill.strip().lower()
            for skill in user_skills.split(",")
            if skill.strip()
        }

        return sorted(
            required_skills - provided_skills
        )

    # Recommend jobs based on a selected job title
    def recommend_by_job_title(
        self,
        job_title,
        top_n=5
    ):

        matching_indices = self.jobs.index[
            self.jobs["job_title"] == job_title
        ].tolist()

        if not matching_indices:
            return pd.DataFrame()

        job_index = matching_indices[0]

        similarity_scores = cosine_similarity(
            self.feature_matrix[job_index],
            self.feature_matrix
        ).flatten()

        ranked_indices = similarity_scores.argsort()[::-1]

        # Exclude the selected job itself
        ranked_indices = [
            index
            for index in ranked_indices
            if index != job_index
        ]

        results = self.jobs.iloc[
            ranked_indices[:top_n]
        ].copy()

        results["similarity_score"] = [
            float(similarity_scores[index])
            for index in ranked_indices[:top_n]
        ]

        return results

    # Recommend jobs based on the user's skills
    def recommend_by_skills(
        self,
        user_skills,
        top_n=5
    ):

        if not user_skills or not user_skills.strip():
            return pd.DataFrame()

        user_vector = self.vectorizer.transform(
            [user_skills]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.feature_matrix
        ).flatten()

        ranked_indices = similarity_scores.argsort()[::-1][
            :top_n
        ]

        results = self.jobs.iloc[
            ranked_indices
        ].copy()

        results["similarity_score"] = [
            float(similarity_scores[index])
            for index in ranked_indices
        ]

        return results
