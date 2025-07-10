import docx
import PyPDF2

def load_text(file):
    name = file.name
    if name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    elif name.endswith('.docx'):
        doc = docx.Document(file)
        return '\n'.join([p.text for p in doc.paragraphs])
    else:
        return file.read().decode('utf-8')