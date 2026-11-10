from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    if db.query(models.Pattern).count() > 0:
        print("Database already seeded. Skipping.")
        db.close()
        return

    patterns_to_add = [
        {
            "title": "Chain-of-Thought Reasoning",
            "base_persona": "You are an expert logician and mathematician. Always prioritize accuracy over speed.",
            "context_examples": "Input: If I have 3 apples and eat 1, how many are left?\nReasoning: Start with 3. Subtract 1. Result is 2.\nOutput: 2",
            "task_instruction": "Solve the following problem. You MUST show your step-by-step reasoning before providing the final answer.",
            "tradeoffs": "Increases token usage and latency, but drastically reduces logic errors."
        },
        {
            "title": "Few-Shot Formatting",
            "base_persona": "You are a strict data formatting engine. You output ONLY valid JSON, no markdown, no explanations.",
            "context_examples": "Input: Apple, Red\nOutput: {\"item\": \"Apple\", \"color\": \"Red\"}\nInput: Banana, Yellow\nOutput: {\"item\": \"Banana\", \"color\": \"Yellow\"}",
            "task_instruction": "Convert the following unstructured text into the exact JSON schema shown in the examples above.",
            "tradeoffs": "Consumes context window quickly with repetitive examples."
        },
        {
            "title": "Role Priming for Expertise",
            "base_persona": "You are a senior risk analyst at a tier-one global bank with 20 years of experience in corporate law and compliance.",
            "context_examples": "",
            "task_instruction": "Review the following contract clause. Identify any hidden liabilities, non-standard terms, or compliance risks. Output a bulleted list of concerns.",
            "tradeoffs": "Can sometimes make the model overly verbose or adopt unwanted corporate mannerisms."
        },
        {
            "title": "Structured Output Enforcement",
            "base_persona": "You are an API integration assistant. Your responses must be machine-readable.",
            "context_examples": "",
            "task_instruction": "Analyze the text below. Return ONLY a valid JSON object with the keys: 'summary' (string), 'action_items' (array of strings), 'risk_level' (integer 1-10). Do not include markdown formatting.",
            "tradeoffs": "Models may still hallucinate JSON syntax if the prompt is too complex."
        }
    ]

    for p_data in patterns_to_add:
        new_pattern = models.Pattern(**p_data)
        db.add(new_pattern)

    db.commit()
    print("✅ Database successfully seeded with 4 Prompt Pyramid patterns!")
    db.close()

if __name__ == "__main__":
    seed_database()
