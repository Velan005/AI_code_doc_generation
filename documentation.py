import streamlit as st
import os
from groq import AsyncGroq
import asyncio

client = AsyncGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

async def summarize_with_groq(model_output):
    """
    This function sends the model-generated code to the Groq API and retrieves a summary.
    
    Parameters:
    model_output (str): The generated code or response from the AI model.
    
    Returns:
    str: The summarized explanation of the model output from the Groq API.
    """
    messages = [
        {
            "role": "user",
            "content": f"Please summarize the following code in a concise manner:\n\n{model_output}"
        }
    ]

    try:
        chat_completion = await client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192" 
        )
        
        summary = chat_completion.choices[0].message.content
        return summary

    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return "Error generating summary."


def display_summary():
    """
    Function to display the summary on the Streamlit UI.
    """
    st.title("AI Code Generation - Final Output Summary")

    model_output = """
    def sum_two_numbers(a, b):
        # This function takes two integers and returns their sum
        result = a + b
        return result

    def multiply_two_numbers(a, b):
        # This function multiplies two integers and returns the product
        result = a * b
        return result
    """
    
    st.write("### Full Output from AI Model:")
    st.code(model_output, language='python')  

    st.write("### Summarized Output:")

    summary = asyncio.run(summarize_with_groq(model_output))
    st.text(summary)


# def demo_run():
#     """
#     Function to demonstrate the summarization process with multiple AI-generated code snippets.
#     This section simulates multiple model outputs and summarizes them using Groq.
#     """
#     st.write("## Demo Run - Efficiency Showcase")
    
#     model_output_1 = """
#     def add_numbers(a, b):
#         # Adds two numbers
#         return a + b

#     def subtract_numbers(a, b):
#         # Subtracts two numbers
#         return a - b
#     """
    
#     st.write("### Example 1 - Full Output:")
#     st.code(model_output_1, language='python')
#     st.write("### Example 1 - Summarized Output:")
#     summary_1 = asyncio.run(summarize_with_groq(model_output_1))
#     st.text(summary_1)

#     model_output_2 = """
#     def calculate_area(radius):
#         # Calculates the area of a circle
#         import math
#         area = math.pi * radius * radius
#         return area

#     def calculate_perimeter(radius):
#         # Calculates the perimeter of a circle
#         import math
#         perimeter = 2 * math.pi * radius
#         return perimeter
#     """
    
#     st.write("### Example 2 - Full Output:")
#     st.code(model_output_2, language='python')
#     st.write("### Example 2 - Summarized Output:")
#     summary_2 = asyncio.run(summarize_with_groq(model_output_2))
#     st.text(summary_2)

#     model_output_3 = """
#     def greet_user(name):
#         # Greets a user with their name
#         print(f"Hello, {name}!")

#     def farewell_user(name):
#         # Says farewell to a user with their name
#         print(f"Goodbye, {name}!")
#     """
    
#     st.write("### Example 3 - Full Output:")
#     st.code(model_output_3, language='python')
#     st.write("### Example 3 - Summarized Output:")
#     summary_3 = asyncio.run(summarize_with_groq(model_output_3))
#     st.text(summary_3)


if __name__ == "__main__":
    display_summary()  
    # demo_run()  
