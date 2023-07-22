from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
import openai
import os



template = """You are given following information and a question. Generate a python code with plotly to find the answer. Provide Text as comments only in code.

Information:
{main_question}
=============
Question:
{sub_question}
Answer:"""

prompt = PromptTemplate(template=template, input_variables=["main_question", "sub_question"])

def set_openai_api_key(api_key):
    openai.api_key = api_key

def generate_plot(main_question, sub_question):
    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(main_question=main_question, sub_question=sub_question)
    return response