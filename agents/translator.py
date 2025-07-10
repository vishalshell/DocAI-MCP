import requests

class TranslatorAgent:
    def __init__(self):
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "mistral"
        self.languages = {
            "en": "English", "id": "Indonesian", "ms": "Malay",
            "zh-cn": "Simplified Chinese", "hi": "Hindi", "ta": "Tamil"
        }

    def handle(self, msg):
        text = msg.payload["text"]
        lang = msg.payload["target_lang"]
        lang_name = self.languages.get(lang, "English")
        prompt = f"Translate the following text into {lang_name}:\n\n{text}"
        response = requests.post(self.model_url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        translated = response.json().get("response", "").strip()
        return {"translated_text": translated if translated else "No translation generated."}