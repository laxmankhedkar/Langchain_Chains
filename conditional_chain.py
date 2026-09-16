from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
import os

load_dotenv()

hf_key = os.getenv("HUGGINGFACE_KEY")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_key
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


# 1. Classifier prompt

classifier_prompt = PromptTemplate(
    template="""
Classify the sentiment of the following feedback.

Return ONLY one word:
positive
or
negative

Feedback:
{feedback}
""",
    input_variables=["feedback"]
)


# 2. Classifier chain

classifier_chain = classifier_prompt | model | parser


# 3. Positive response

prompt2 = PromptTemplate(
    template="""
Write an appropriate response to this positive feedback:

{feedback}
""",
    input_variables=["feedback"]
)


# 4. Negative response

prompt3 = PromptTemplate(
    template="""
Write an appropriate response to this negative feedback:

{feedback}
""",
    input_variables=["feedback"]
)


# 5. Conditional branch
branch_chain = RunnableBranch(

    (
        lambda x: x.strip().lower() == "positive",
        prompt2 | model | parser
    ),

    (
        lambda x: x.strip().lower() == "negative",
        prompt3 | model | parser
    ),

    RunnableLambda(
        lambda x: "Could not find sentiment"
    )
)

# 6. Complete chain

chain = classifier_chain | branch_chain


result = chain.invoke({
    "feedback": "This is a beautiful phone"
})

print(result)