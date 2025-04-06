import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0.7)

# Define the prompt template for the tutor
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    You are a helpful and knowledgeable tutor. Answer the following question in a clear and concise manner:
    {question}
    """
)

# Streamlit app
st.title("Teacher-in-the-Loop Tutor")

# User input for the question
question = st.text_input("Ask a question:")

# Button to submit the question and get the response
if st.button("Get Answer"):
    if question:
        # Format the prompt with the user's question
        formatted_prompt = prompt.format(question=question)
        
        # Get the response from the LLM
        response = llm(formatted_prompt)
        
        # Display the response
        st.write("**Tutor's Response:**")
        st.write(response)
    else:
        st.write("Please enter a question to get an answer.")
