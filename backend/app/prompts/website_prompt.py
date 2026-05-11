SYSTEM_PROMPT = """
Analyze the following website.

Return ONLY valid JSON.

Structure:

{
  "overview": "",
  "purpose": "",
  "history": "",
  "key_features": [],
  "target_audience": "",
  "business_model": "",
  "ratings_reputation": "",
  "reviews_summary": "",
  "trust_safety": "",
  "final_verdict": ""
}

Rules:
- No markdown
- No extra explanation
- No code block
- Always valid JSON
"""