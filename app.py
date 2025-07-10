import gradio as gr
from agents.summarizer import SummarizerAgent
from agents.qna import QnAAgent
from agents.translator import TranslatorAgent
from protocols.mcp import MCPMessage, dispatch
from utils.loader import load_text

summarizer = SummarizerAgent()
qna = QnAAgent()
translator = TranslatorAgent()

session_state = {"doc_text": "", "summary": ""}

def summarize_file(file):
    text = load_text(file)
    session_state["doc_text"] = text
    msg = MCPMessage("UI", "SummarizerAgent", "summarize", {"document": text})
    result = dispatch(msg)
    summary = result["summary"]
    session_state["summary"] = summary
    return summary

def qa(question):
    msg = MCPMessage("UI", "QnAAgent", "qa", {
        "question": question, "context": session_state["doc_text"]
    })
    result = dispatch(msg)
    return result["answer"]

def translate_summary(target_lang):
    msg = MCPMessage("UI", "TranslatorAgent", "translate", {
        "text": session_state["summary"], "target_lang": target_lang
    })
    result = dispatch(msg)
    return result["translated_text"]

with gr.Blocks(title="DocAI-MCP Orchestrator") as demo:
    gr.Markdown("# DocAI MCP: Document Summarizer & Agentic QnA")
    with gr.Row():
        file = gr.File(label="Upload Document (PDF, DOCX, TXT)")
        summary_btn = gr.Button("Summarize")
        summary_output = gr.Textbox(label="Summary", lines=6)
    with gr.Row():
        question = gr.Textbox(label="Ask a question about the document")
        answer_btn = gr.Button("Get Answer")
        answer_output = gr.Textbox(label="Answer", lines=4)
    with gr.Row():
        lang = gr.Dropdown(["en", "id", "ms", "zh-cn", "hi", "ta"], value="en", label="Translate Summary To")
        translate_btn = gr.Button("Translate")
        translate_output = gr.Textbox(label="Translated Summary", lines=6)

    summary_btn.click(fn=summarize_file, inputs=file, outputs=summary_output)
    answer_btn.click(fn=qa, inputs=question, outputs=answer_output)
    translate_btn.click(fn=translate_summary, inputs=lang, outputs=translate_output)

if __name__ == "__main__":
    demo.launch()