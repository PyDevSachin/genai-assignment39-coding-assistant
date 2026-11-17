
import os
import streamlit as st
from dotenv import load_dotenv

from task3 import (
    generate_code,
    explain_code,
    debug_code,
    optimize_code
)

# Load local environment variables
load_dotenv()

# Read the API key from Streamlit secrets when deployed
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass


# Page configuration
st.set_page_config(
    page_title="AI Coding Assistant",
    page_icon="💻",
    layout="centered"
)


# Application title
st.title("💻 AI Coding Assistant")

st.write(
    "An AI-powered coding assistant that helps developers "
    "generate, explain, debug and optimize Python code."
)

st.caption("Powered by Groq API and GPT-OSS 20B")

st.divider()


# Select coding task
task = st.selectbox(
    "Select Your Task",
    [
        "Generate Code",
        "Explain Code",
        "Debug Code",
        "Optimize Code"
    ]
)


# Input placeholder
if task == "Generate Code":

    placeholder = (
        "Example: Write a Python program to calculate factorial."
    )

elif task == "Explain Code":

    placeholder = "Paste the code you want explained here."

elif task == "Debug Code":

    placeholder = "Paste your code containing errors here."

else:

    placeholder = "Paste the code you want to optimize here."


# User input
user_input = st.text_area(
    "Enter your requirement or code:",
    height=200,
    placeholder=placeholder
)


# Submit button
if st.button("Submit", type="primary"):

    if not user_input.strip():

        st.warning("Please enter some text or code.")

    else:

        with st.spinner("AI is processing your request..."):

            try:

                if task == "Generate Code":

                    result = generate_code(user_input)

                elif task == "Explain Code":

                    result = explain_code(user_input)

                elif task == "Debug Code":

                    result = debug_code(user_input)

                else:

                    result = optimize_code(user_input)


                st.subheader("AI Response")
                st.markdown(result)

            except Exception as e:

                st.error(f"An error occurred: {e}")


st.divider()

st.caption(
    "AI-generated code should always be reviewed and tested before use."
)
