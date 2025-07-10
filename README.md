# DocAI-MCP

**A modular, agentic document analysis and summarization toolkit built on the Model Context Protocol (MCP) with Agent-to-Agent (A2A) orchestration.**

---

## 🚀 Features

- **Summarize PDF, DOCX, TXT:** Upload documents and get concise, model-powered summaries.
- **Ask Questions:** Interactively query document content in natural language.
- **Translate Summaries:** Instantly translate summaries into major world languages (English, Bahasa Indonesia, Malay, Chinese, Hindi, Tamil, and more).
- **Agentic Architecture:** All functions are modular “agents” communicating via MCP for maximum extensibility and traceability.
- **Gradio UI:** Clean, no-login web interface—runs locally or on cloud.
- **No Cloud Lock-In:** All core logic runs locally (uses open-source models and tools).

---

## 🏗️ Project Structure

```

docai-mcp/
│
├── app.py                # Gradio UI + Orchestration
├── agents/
│   ├── summarizer.py     # Summarization agent (BART/CNN)
│   ├── translator.py     # Translation agent (googletrans)
│   └── qna.py            # Q\&A agent (DistilBERT-SQuAD)
├── protocols/
│   └── mcp.py            # MCP message contract + dispatcher
├── utils/
│   ├── loader.py         # PDF, DOCX, TXT loader
│   └── config.py         # Config placeholder
├── requirements.txt
├── LICENSE
└── README.md

````

---

## ⚡ Getting Started

### 1. **Installation**

Clone the repo, install dependencies, and run:

```bash
git clone https://github.com/youruser/docai-mcp.git
cd docai-mcp
pip install -r requirements.txt
python app.py
````

### 2. **Usage**

* Launches a web UI (Gradio) on `http://localhost:7860` by default.
* Upload your document.
* Click “Summarize” to get a summary.
* Ask questions in the Q\&A box.
* Translate the summary to your preferred language.

---

## 🧠 How It Works

* **Model Context Protocol (MCP):** Orchestrates requests by passing explicit messages between agents.
* **A2A Orchestration:** Summarizer, Q\&A, and Translator agents are independent and composable.
* **Agents:** Swap out models, add new functionality, or extend with your own code.

---

## 🔄 Troubleshooting

* **Transformer model downloads** can be slow first run (downloads weights from HuggingFace).
* **googletrans** uses Google’s unofficial API; for critical/prod, use official APIs or alternatives.
* If **PDF extraction** seems weak, try converting to TXT or DOCX first.

---

## 🤝 Contributing

Pull requests welcome!
File issues or suggestions—this is a template for further modular GenAI stacks.

---

## 📜 License

MIT License

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

**There is absolutely NO WARRANTY or GUARANTEE of any kind.
Use at your own risk.
This is community-supported open source—contributions, improvements, and suggestions are welcome!**
