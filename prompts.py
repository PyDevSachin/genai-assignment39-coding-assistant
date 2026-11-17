
# Prompt template for code generation
GENERATE_PROMPT = """
You are a helpful Python programming assistant.

Generate clean, correct and readable Python code
for the following requirement:

{user_input}

Include comments and a short explanation.
"""


# Prompt template for code explanation
EXPLAIN_PROMPT = """
You are a helpful programming teacher.

Explain the following code in simple language.
Describe how it works step by step.

Code:
{user_input}
"""


# Prompt template for debugging
DEBUG_PROMPT = """
You are an expert Python debugging assistant.

Find the errors in the following code.
Explain why the errors occur and provide corrected code.

Code:
{user_input}
"""


# Prompt template for code optimization
OPTIMIZE_PROMPT = """
You are an experienced Python developer.

Review the following code and suggest improvements
in readability, performance and efficiency.

Provide an optimized version of the code.

Code:
{user_input}
"""
