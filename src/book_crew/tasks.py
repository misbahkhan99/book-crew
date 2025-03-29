from crewai import Task
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import SerperDevTool

internet_search = SerperDevTool()

class MyTask:
    def outliner_Task(self, agent, topic):
        return Task(
            agent = agent,
            description = f"""Write a detail outline for a book on the mentioned topic it must contain 10 chapter and each chapter headlines should be descriptively
            parameters:
            topic: {topic}
            """,
            tools = [internet_search],
            expected_output = f"""your output should be according to the following mentioned structure


                1. Introduction (200 words)
                2. Theoretical Framework (200 words)
                3. Literature Review (200 words)
                4. Research Methodology (200 words)
                5. Data Analysis (200 words)
                6. Results and Conclusion (200 words)
                7. Discussion 
                8. Reference 
                9. Appendices 
                10. Future work 
            """,

        )
    


    def Book_Writer_Task(self, agent, context):
        return Task(
            agent = agent,
            description = f"""Write a detail book on oytline topic it should be descriptively""",
            context = context,
            expected_output = f"""your output should be according to the following mentioned structure

                1. Introduction (200 words)
                2. Theoretical Framework (200 words)
                3. Literature Review (200 words)
                4. Research Methodology (200 words)
                5. Data Analysis (200 words)
                6. Results and Conclusion (200 words)
                7. Discussion 
                8. Reference 
                9. Appendices 
                10. Future work 

                make a professionally formated book according to the international standards
                """,

        )
