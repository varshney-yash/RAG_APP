class ModelHandler:
    def __init__(self, llm):
        self.llm = llm

    def get_summary(self, text: str) -> str:
        summarizer = TextSummarizer(self.llm)
        return summarizer.summarize(text)