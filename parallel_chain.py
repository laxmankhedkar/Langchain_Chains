import os 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

hf_key = os.getenv('HUGGINGFACE_KEY')

llm = HuggingFaceEndpoint(
    repo_id= 'Qwen/Qwen2.5-1.5B-Instruct',
    task = 'text-generation',
    huggingfacehub_api_token= hf_key
)


prompt = PromptTemplate(
    template= ('Generate a detailed summary on {topic}'),
    input_variables= ['topic']
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

result = chain = prompt | model | parser

print(result)


chain.get_graph().print_ascii()