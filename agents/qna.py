from transformers import pipeline

class QnAAgent:
    def __init__(self):
        self.qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

    def handle(self, msg):
        question = msg.payload["question"]
        context = msg.payload["context"]
        if not context:
            return {"answer": "Please upload a document first."}
        result = self.qa(question=question, context=context[:4096])
        return {"answer": result['answer']}