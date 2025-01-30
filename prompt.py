



from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def code_generator_prompt(language, problem):
    """
    Generates Prompt template for code generation with basic context.

    Args:
        language -> str: The programming language for code generation (e.g., "Python").
        problem -> str: The problem or task description for code generation.

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """

    system_msg = f'''
                
You are an expert code generator assistant. Your task is to generate code in {language} based on the user’s provided specifications. Follow these guidelines:

1. Only respond to queries explicitly requesting code generation.
2. The output must strictly be the code, properly formatted, *including inline comments explaining each part of the code*.
3. Comments should describe *the logic, functions, and key steps* of the code.
4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.

Note: Ensure the generated code aligns with the user’s request and is functional.
''' 

    user_msg = f"Write a {language} function to {problem}"

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return prompt_template

def code_generator_rag_prompt(language, problem):
    """
    Generates a RAG-enabled Prompt template for code generation.

    Args:
        language -> str: The programming language for code generation (e.g., "Python").
        problem -> str: The problem or task description for code generation.

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """

    system_msg = f'''
You are an expert code generator assistant. Your task is to generate code in {language} based on the user’s provided specifications. Follow these guidelines:

1. Only respond to queries explicitly requesting code generation.
2. The output must strictly be the code, properly formatted, *including inline comments explaining each part of the code*.
3. Comments should describe *the logic, functions, and key steps* of the code.
4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.

Note: Ensure the generated code aligns with the user’s request and is functional.
'''

    user_msg = f"Write a {language} function to {problem}, considering the following context: {{context}}"

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return prompt_template

def code_generator_rag_prompt_from_hub(template="aarthy26/code_generator_rag"):
    """
    Generates Prompt template from the LangSmith prompt hub for code generation.

    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    
    prompt_template = hub.pull(template)
    return prompt_template