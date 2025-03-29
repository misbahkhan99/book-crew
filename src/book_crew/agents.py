from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()

llm = LLM(model = "gemini/gemini-1.5-flash")

class MyBookWriterAgent:

    def outliner(self):
        return Agent(
            role = "outliner",
            goal = "Develop a detailed outline for the book",
            backstory = " i am expert in writing book outline and i have 10+year of experience in writing book outline",
            llm = llm,
            verbose = True
        )
    

    def Book_Writer(self):
        return Agent(
            role = "Book_Writer",
            goal = "Develop a detailed outline on provided outline",
            backstory = " i am expert in writing book outline and i have 10+year of experience in writing book",
            llm = llm,
            verbose = True
        )

