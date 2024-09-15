from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class TextSummarizer:
    def __init__(self, llm):
        self.llm = llm

    def summarize(self, text: str) -> str:
        template = """Summarize the following text:
        {text}
        Summary:"""
        prompt = ChatPromptTemplate.from_template(template)

        summarize_chain = (
            {"text": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )

        return summarize_chain.invoke(text)
