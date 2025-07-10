from agents.summarizer import SummarizerAgent
from agents.qna import QnAAgent
from agents.translator import TranslatorAgent

class MCPMessage:
    def __init__(self, sender, receiver, task, payload):
        self.sender = sender
        self.receiver = receiver
        self.task = task
        self.payload = payload
        self.status = "pending"

def dispatch(msg: MCPMessage):
    if msg.receiver == "SummarizerAgent":
        return SummarizerAgent().handle(msg)
    elif msg.receiver == "QnAAgent":
        return QnAAgent().handle(msg)
    elif msg.receiver == "TranslatorAgent":
        return TranslatorAgent().handle(msg)
    else:
        raise Exception("Unknown agent: " + msg.receiver)