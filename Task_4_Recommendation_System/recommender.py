import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobRecommender:
    def __init__(self, data_path="jobs.csv"):
        self.jobs = pd.read_csv(data_path)

        self.jobs["combined_features"] = (
            self.jobs["job_title"].astype(str) + " " +
            self.jobs["skills"].astype(str) + " " +
            self.jobs["experience_level"].astype(str) + " " +
            self.jobs["location"].astype(str) + " " +
            self.jobs["description"].astype(str)
        )

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.feature_matrix = self.vectorizer.fit_transform(
            self.jobs["combined_features"]
        )

    def get_job_titles(self):
        return self.jobs["job_title"].tolist()

    def get_locations(self):
        return sorted(self.jobs["location"].unique().tolist())

    def get_experience_levels(self):
        return sorted(self.jobs["experience_level"].unique().tolist())

    def get_job_details(self, job_title):
        job = self.jobs[self.jobs["job_title"] == job_title]

        if job.empty:
            return None

        return job.iloc[0]

    def analyze_skill_gap(self, user_skills, job_skills):
        user_skill_set = set(
            user_skills.lower()
            .replace(",", " ")
            .replace("-", " ")
            .split()
        )

        job_skill_set = set(
            job_skills.lower()
            .replace(",", " ")
            .replace("-", " ")
            .split()
        )

        matched_skills = user_skill_set.intersection(job_skill_set)
        missing_skills = job_skill_set.difference(user_skill_set)

        return {
            "matched_skills": ", ".join(sorted(matched_skills)) if matched_skills else "None",
            "missing_skills": ", ".join(sorted(missing_skills)) if missing_skills else "None"
        }

    def recommend_by_job_title(
        self,
        selected_job_title,
        top_n=5,
        location_filter="All",
        experience_filter="All"
    ):
        selected_job = self.jobs[self.jobs["job_title"] == selected_job_title]

        if selected_job.empty:
            return pd.DataFrame()

        selected_index = selected_job.index[0]

        similarity_scores = cosine_similarity(
            self.feature_matrix[selected_index],
            self.feature_matrix
        ).flatten()

        similarity_scores = list(enumerate(similarity_scores))

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        selected_skills = selected_job.iloc[0]["skills"]

        for index, score in similarity_scores:
            if index == selected_index:
                continue

            if score <= 0:
                continue

            job = self.jobs.iloc[index]

            if location_filter != "All" and job["location"] != location_filter:
                continue

            if experience_filter != "All" and job["experience_level"] != experience_filter:
                continue

            skill_gap = self.analyze_skill_gap(
                selected_skills,
                job["skills"]
            )

            recommendations.append(
                {
                    "job_title": job["job_title"],
                    "company": job["company"],
                    "location": job["location"],
                    "experience_level": job["experience_level"],
                    "skills": job["skills"],
                    "description": job["description"],
                    "match_score": round(score * 100, 2),
                    "matched_skills": skill_gap["matched_skills"],
                    "missing_skills": skill_gap["missing_skills"]
                }
            )

            if len(recommendations) == top_n:
                break

        return pd.DataFrame(recommendations)

    def recommend_by_skills(
        self,
        user_skills,
        top_n=5,
        location_filter="All",
        experience_filter="All"
    ):
        if not user_skills.strip():
            return pd.DataFrame()

        user_vector = self.vectorizer.transform([user_skills])

        similarity_scores = cosine_similarity(
            user_vector,
            self.feature_matrix
        ).flatten()

        similarity_scores = list(enumerate(similarity_scores))

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for index, score in similarity_scores:
            if score <= 0:
                continue

            job = self.jobs.iloc[index]

            if location_filter != "All" and job["location"] != location_filter:
                continue

            if experience_filter != "All" and job["experience_level"] != experience_filter:
                continue

            skill_gap = self.analyze_skill_gap(
                user_skills,
                job["skills"]
            )

            recommendations.append(
                {
                    "job_title": job["job_title"],
                    "company": job["company"],
                    "location": job["location"],
                    "experience_level": job["experience_level"],
                    "skills": job["skills"],
                    "description": job["description"],
                    "match_score": round(score * 100, 2),
                    "matched_skills": skill_gap["matched_skills"],
                    "missing_skills": skill_gap["missing_skills"]
                }
            )

            if len(recommendations) == top_n:
                break

        return pd.DataFrame(recommendations)