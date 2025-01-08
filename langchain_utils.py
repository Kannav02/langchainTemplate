from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import SimpleSequentialChain,SequentialChain
from dotenv import load_dotenv, dotenv_values
import os


config = dotenv_values(".env")
openai_api_key = config["OPENAI_API_KEY"]
print(openai_api_key)

llm = OpenAI(api_key = openai_api_key, temperature = 0.6)

story_template = PromptTemplate(input_variables = ["topic"],template = "Generate me a brief story based on this {topic}?")
moral_template = PromptTemplate(input_variables=["story"],template = "What is the moral of the {story} ?")

story_chain = story_template | llm
story_result = story_chain.invoke({"topic":"The Punisher From Marvel Comics"})

moral_chain = moral_template | llm
moral_result = moral_chain.invoke({"story":story_result})

print(moral_result)





