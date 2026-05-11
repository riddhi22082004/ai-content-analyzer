from app.analyzer.llm_engine import (
    analyze_with_ai
)


class AIOrchestrator:

    def __init__(self):

        self.fallback = None

    def generate(self, scraped_data):

        try:

            return analyze_with_ai(
                scraped_data
            )

        except Exception as e:

            print(
                "Primary AI failed:",
                e
            )

            return {

                "overview": "",

                "purpose": "",

                "history": "",

                "key_features": [],

                "target_audience": "",

                "business_model": "",

                "ratings_reputation": "",

                "reviews_summary": "",

                "trust_safety": "AI service failed",

                "final_verdict": "AI analysis failed"
            }