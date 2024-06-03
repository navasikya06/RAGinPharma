import ollama


class ChatModel:
    def __init__(self, device="cpu"):        
        self.device = device

    def generate(self, question: str, context: str = None):

        if context == None or context == "":
            prompt = f"""Give a detailed answer to the following question. Question: {question}"""
        else:
            prompt = f"""Using the information contained in the context, give a detailed answer to the question.
Context: {context}.
Question: {question}"""

        answer = ollama.generate(model='gemma:2b', prompt = prompt)
        response = answer["response"]

        return response
