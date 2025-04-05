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
# Invoking the LLM
result = llm.invoke("Who is Ludwig Wittgenstein?")
print(result.content)