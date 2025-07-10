import requests

class SummarizerAgent:
    def __init__(self):
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "mistral"

    def handle(self, msg):
        doc = msg.payload["document"]
        prompt = f"Summarize the following document in concise English (max 200 words):\n\n{doc[:3000]}"
        response = requests.post(self.model_url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        summary = response.json().get("response", "").strip()
        return {"summary": summary if summary else "No summary generated."}