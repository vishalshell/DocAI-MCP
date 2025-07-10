from googletrans import Translator

class TranslatorAgent:
    def __init__(self):
        self.translator = Translator()

    def handle(self, msg):
        text = msg.payload["text"]
        lang = msg.payload["target_lang"]
        translated = self.translator.translate(text, dest=lang)
        return {"translated_text": translated.text}