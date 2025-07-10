# DocAI-MCP (Ollama Local LLM Edition)

> Modular, fully local document analysis and Q&A powered by Model Context Protocol (MCP) and Agent-to-Agent (A2A) orchestration.  
> All AI runs on your own hardware using [Ollama](https://ollama.com/) and the Mistral large language model.

---

## 🚀 What is DocAI-MCP?

- **Upload a PDF, DOCX, or TXT file** – get an instant summary, ask questions, or translate summaries.
- **Private by default:** All processing happens locally—no cloud, no external API calls, no data leaves your machine.
- **Composable Agent Architecture (MCP, A2A):** Specialized “agents” for summarization, Q&A, and translation, working together with explicit, auditable messaging.
- **No API keys or subscriptions required.**
- **Simple, browser-based Gradio UI.**

---

## ⚡ Quick Start

### 1. Install Ollama

Ollama lets you run open-source large language models like Mistral on your PC, Mac, Linux server, or WSL.

#### Linux / WSL

```bash
curl -fsSL https://ollama.com/install.sh | sh
````

#### MacOS

```bash
brew install ollama
```

#### Windows

Ollama runs under [WSL2](https://learn.microsoft.com/en-us/windows/wsl/).
See [Ollama Windows setup](https://ollama.com/download) for instructions.

*For full details or troubleshooting, see the [Ollama documentation](https://ollama.com/download).*

---

### 2. Download the Mistral Model

After installing Ollama, run:

```bash
ollama pull mistral
```

This will download the Mistral model (\~4GB). You can swap for any Ollama-compatible model (see below).

---

### 3. Start the Ollama Server

```bash
ollama serve
```

By default, Ollama will serve its API at `http://localhost:11434`.

> **Tip:** You can run Ollama as a background service or leave the terminal open.

---

### 4. Clone and Run DocAI-MCP

```bash
git clone https://github.com/vishalshell/DocAI-MCP.git
cd DocAI-MCP
pip install -r requirements.txt
python app.py
```

Open your browser to [http://localhost:7860](http://localhost:7860).

* Upload a document, get a summary, ask questions, and translate—all without sending data to the cloud!

---

## 🏗️ Folder Structure

```
DocAI-MCP/
├── app.py
├── agents/
│   ├── summarizer.py
│   ├── qna.py
│   └── translator.py
├── protocols/
│   └── mcp.py
├── utils/
│   ├── loader.py
│   └── config.py
├── requirements.txt
├── LICENSE
├── README.md
└── WIKI.md
```

---

## 🤖 FAQ

**How private is this?**
100% private: your files and queries never leave your machine.

**What is MCP and A2A?**
See [WIKI.md](./WIKI.md) for details.
In short: Each function (summary, Q\&A, translation) is handled by a dedicated “agent” via formal, traceable messages. This makes the system modular, extensible, and easy to audit or extend.

**Can I use a different model?**
Yes!
Replace `"mistral"` with your preferred model (e.g., `"llama2"`, `"mixtral"`) in `agents/summarizer.py`, `agents/qna.py`, and `agents/translator.py`.
Just run `ollama pull MODELNAME` first.

**Is translation as good as Google Translate?**
No—prompt-based LLM translation is often good enough for casual/business use, but less accurate than a specialized API. For legal or medical translation, use dedicated tools.

**How fast is this?**
Depends on your hardware. On a modern GPU, Mistral can answer in seconds; on CPU, it’s slower.

---

## 🧰 Troubleshooting

* “Connection refused” – Is `ollama serve` running? Did you download (`ollama pull mistral`)?
* For very large files, only the first \~3000 characters are used per request (adjustable in the code).
* Some PDF/DOCX files with heavy formatting, images, or tables may not extract all text. For best results, use clear, text-rich documents.

---

## 🔐 Security and License

**MIT License** – see [LICENSE](./LICENSE)

**NO WARRANTY OR GUARANTEE OF ANY KIND.**
You are responsible for your own use, data, and results.

---

## 📝 Extending This Project

* Swap LLMs, add speech-to-text, OCR, or image agents.
* See [WIKI.md](./WIKI.md) for best practices, architectural explanations, and more.

---

## 🤝 Credits

* [Ollama](https://ollama.com/) for local LLM infrastructure
* [Mistral](https://ollama.com/library/mistral) for the LLM
* [Gradio](https://gradio.app/) for the UI

---

## 📚 More Info

* Full architecture, agent details, extensibility, and advanced usage in [WIKI.md](./WIKI.md)
* [Open an issue](https://github.com/vishalshell/DocAI-MCP/issues) for support or feature requests.
