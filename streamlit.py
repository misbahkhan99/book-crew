import streamlit as st
from src.book_crew.agents import MyBookWriterAgent
from src.book_crew.tasks import MyTask
from crewai import Crew

def main():
    st.title("Book Writing CrewAI App")
    st.write("This app uses CrewAI agents to outline and write a book on your chosen topic.")

    # User input
    topic = st.text_input("Enter the topic for your book:", "Machine Learning")
    
    if st.button("Generate Book"):
        with st.spinner("Creating your book... This may take a while"):
            # Initialize agents and tasks
            agents = MyBookWriterAgent()
            tasks = MyTask()

            # Create agents
            outliner = agents.outliner()
            book_writer = agents.Book_Writer()

            # Create tasks
            outliner_task = tasks.outliner_Task(
                agent=outliner,
                topic=topic
            )

            book_writer_task = tasks.Book_Writer_Task(
                agent=book_writer,
                context=[outliner_task]
            )

            # Create and run crew
            crew = Crew(
                agents=[outliner, book_writer],
                tasks=[outliner_task, book_writer_task],
                verbose=True
            )

            result = crew.kickoff()
            
            # Display results
            st.subheader("Generated Book Content")
            st.write(result)

if __name__ == "__main__":
    main()