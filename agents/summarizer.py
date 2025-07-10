from transformers import pipeline

class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def handle(self, msg):
        doc = msg.payload["document"]
        if len(doc) > 4000:
            doc = doc[:4000]
        summary = self.summarizer(doc, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
        return {"summary": summary}