import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter():
    tokenizer = tiktoken.get_encoding("cl100k_base")

    def tiktoken_len(text):
        tokens = tokenizer.encode(text, disallowed_special=())
        return len(tokens)

    return RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
        length_function=tiktoken_len,
        separators=["\n\n", "\n", " ", ""]
    )