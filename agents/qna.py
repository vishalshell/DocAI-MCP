import requests

class QnAAgent:
    def __init__(self):
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "mistral"

    def handle(self, msg):
        question = msg.payload["question"]
        context = msg.payload["context"]
        if not context:
            return {"answer": "Please upload a document first."}
        prompt = f"Based on the following document, answer the question as precisely as possible.\n\nDocument:\n{context[:3000]}\n\nQuestion: {question}\nAnswer:"
        response = requests.post(self.model_url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        answer = response.json().get("response", "").strip()
        return {"answer": answer if answer else "No answer generated."}