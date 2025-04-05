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
    # max_retries=2, # Can change and uncomment to experiment
)

# Setting up the chat history list
chat_history = []

# Setting up the system message and adding it to the history
system_message = SystemMessage(content="You are Mistral, a helpful AI assistant eager to reply to user queries.")
chat_history.append(system_message)

# Initialising the chat loop and invoking the LLM within it
while True:
    query = input('User: ')
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query)) # Appends the user message to the history

    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) # Appends the AI message to the history
    
    print(f"AI: {response}")

print(f"-----Message History-----\n{chat_history}")