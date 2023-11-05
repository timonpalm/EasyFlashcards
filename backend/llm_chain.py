import langchain
from langchain.llms import LlamaCpp, HuggingFaceHub, OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["OPENAI_API_KEY"] = "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"

class Chain():
    def __init__(self):
        self.template = """You are given a text document. Create 2 unique flashcards to learn the content of that text document.

        Use the following format:
        flashcards:
            1. [frontside of flashcard 1][backside of flashcard 1]
            2. [frontside of flashcard 2][backside of flashcard 2]
            3. ...

        Create 10 unique flashcards!

        text: {text}

        flashcards:"""

        self.prompt = PromptTemplate(template=self.template, input_variables=["text"])

        self.llm = OpenAI(
            temperature=0.2,
            model_name='gpt-3.5-turbo', 
            verbose=True
            )

        self.llm_chain = LLMChain(
            prompt=self.prompt, 
            llm=self.llm, 
            verbose=True
            )
    
    def create_flashcards(self, text):
        return self.llm_chain.run(text)

# text = """Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems.
# In a nutshell, Scrum requires a Scrum Master to foster an environment where:
# 1. A Product Owner orders the work for a complex problem into a Product Backlog.
# 2. The Scrum Team turns a selection of the work into an Increment of value during a Sprint.
# 3. The Scrum Team and its stakeholders inspect the results and adjust for the next Sprint.
# 4. Repeat
# Scrum is simple. Try it as is and determine if its philosophy, theory, and structure help to achieve goals and create value. The Scrum framework is purposefully incomplete, only defining the parts required to implement Scrum theory. Scrum is built upon by the collective intelligence of the people using it. Rather than provide people with detailed instructions, the rules of Scrum guide their relationships and interactions.
# Various processes, techniques and methods can be employed within the framework. Scrum wraps around existing practices or renders them unnecessary. Scrum makes visible the relative efficacy of current management, environment, and work techniques, so that improvements can be made."""

# print(llm_chain.run(text))