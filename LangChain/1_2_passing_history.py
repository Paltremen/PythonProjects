# Setting up the message history
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Setting the variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Importing the actual model
from langchain_mistralai import ChatMistralAI
llm = ChatMistralAI(
    model="mistral-small-latest",
    # temperature=0.5, # The parameters are commented to see the default behaviour
    # max_retries=2,
)

#Creating a message history
messages = [
    SystemMessage("You are an expert in social media content strategy."),
    HumanMessage("Give me a short tip for good Linkedin post writing"),
]

# Invoking the LLM
result = llm.invoke(messages)
print(result.content)