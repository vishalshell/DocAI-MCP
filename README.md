# DocAI-MCP (Ollama Local LLM Edition)

A **private, modular, fully local GenAI document analysis tool** using the Model Context Protocol (MCP) with Agent-to-Agent (A2A) orchestration and **Ollama-hosted Mistral LLM** for all AI tasks.
No cloud API calls, no external data leakage. 100% private—runs on your GPU/CPU.

## 🚀 Features

- **Summarize PDF, DOCX, TXT:** Upload docs and get summaries using Mistral via Ollama.
- **Ask Questions:** Interactive Q&A on document content.
- **Translate Summaries:** Uses LLM prompts for translation, no external API.
- **Everything Local:** All model inference is on your server. No OpenAI, Google, or HuggingFace required.
- **Agentic (MCP/A2A) Orchestration:** Each function is a swappable agent.
- **Gradio UI:** Clean, web-based, no login.

## 🏗️ Project Structure

    docai-mcp/
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
    └── README.md

## ⚡ Getting Started

### 1. **Install [Ollama](https://ollama.com/download)**

- Install Ollama and run:
    ollama pull mistral
    ollama serve

### 2. **Install dependencies**

    pip install -r requirements.txt

### 3. **Run the app**

    python app.py

- App runs at `http://localhost:7860`
- Upload your doc, summarize, ask questions, translate—all on your local hardware.

## 🔄 Troubleshooting

- **Ollama must be running** locally (`http://localhost:11434`) and the model pulled (`mistral`).
- **Translation is prompt-based and not as accurate as specialized APIs.** For perfect translation, consider augmenting with external APIs if privacy allows.

## 📜 License

MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.