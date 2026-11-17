
import os
from dotenv import load_dotenv
from groq import Groq

from prompts import (
    GENERATE_PROMPT,
    EXPLAIN_PROMPT,
    DEBUG_PROMPT,
    OPTIMIZE_PROMPT
)

load_dotenv()

MODEL_NAME = "openai/gpt-oss-20b"


# Common function to communicate with Groq
def get_response(prompt):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Please configure your API key."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and accurate Python coding assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=2048
    )

    return response.choices[0].message.content


# Function 1: Generate code
def generate_code(user_input):

    prompt = GENERATE_PROMPT.format(
        user_input=user_input
    )

    return get_response(prompt)


# Function 2: Explain code
def explain_code(user_input):

    prompt = EXPLAIN_PROMPT.format(
        user_input=user_input
    )

    return get_response(prompt)


# Function 3: Debug code
def debug_code(user_input):

    prompt = DEBUG_PROMPT.format(
        user_input=user_input
    )

    return get_response(prompt)


# Function 4: Optimize code
def optimize_code(user_input):

    prompt = OPTIMIZE_PROMPT.format(
        user_input=user_input
    )

    return get_response(prompt)
