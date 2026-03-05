from langchain_community.document_loaders import PyPDFLoader

def load_pdf():
    loader = PyPDFLoader("data/sample.pdf")
    docs = loader.load()
    return docs
