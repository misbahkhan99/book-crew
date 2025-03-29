from .agents import MyBookWriterAgent
from .tasks import MyTask
from crewai import Crew

agents = MyBookWriterAgent()
tasks = MyTask()

#obj
outliner = agents.outliner()
Book_Writer = agents.Book_Writer()

#Task
outliner_Task = tasks.outliner_Task(
    agent = outliner,
    topic = "Machine Learning"
)

Book_Writer_Task = tasks.Book_Writer_Task(
    agent = Book_Writer,
    context= [outliner_Task]
)

crew = Crew(
    agents = [outliner, Book_Writer],
    tasks = [outliner_Task, Book_Writer_Task],
    verbose = True
)

def main():
    result = crew.kickoff()
    print(f"Final result: {result}")


    