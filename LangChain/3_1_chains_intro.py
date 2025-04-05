# Imports
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain.schema.output_parser import StrOutputParser

# Finding .env
load_dotenv(find_dotenv())

# Setting the model
llm = ChatMistralAI(model="mistral-small-latest")

# Setting the prompt template // Same as before but without a variable
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert on animal facts who knows a lot about the {animal}"),
        ("human", "Tell me {fact_count} facts about this animal."),
    ]
)

# Constructing the chain
chain = prompt_template | llm | StrOutputParser() # | this is called the pipe operator

result = chain.invoke({"animal": "hedgehog", "fact_count": 3})

print(result)