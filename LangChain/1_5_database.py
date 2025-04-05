# Importing dependencies for the message history
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Importing dependencies for the database connection with Google Firestore
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory

# Setting the variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Setting up Firestore
PROJECT_ID = "langchain-c04bb"
SESSION_ID = input("Enter your name (main - Daniel): ") # I know this is supposed to be a constant, whatever
COLLECTION_NAME = "chat_history"

# Initialise Firestore client
print("Initialising Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialise Firestore message history
print("Initialising Firestore chat message history...")
chat_history = FirestoreChatMessageHistory(
    session_id = SESSION_ID,
    collection = COLLECTION_NAME,
    client = client,
)

print("Chat history initialised.")
print("Current chat history:\n", chat_history.messages)

# Importing the actual model
from langchain_mistralai import ChatMistralAI
llm = ChatMistralAI(
    model="mistral-large-latest",
    # temperature=0.5, # The parameters are commented to see the default behaviour
    # max_retries=2, # Can change and uncomment to experiment
)

# Initialising the chat loop and invoking the LLM within it
while True:
    human_input = input('Type your message here ("exit" to exit): ')
    if human_input.lower() == 'exit':
        break
    chat_history.add_user_message(human_input) # Adds the user message to history

    ai_response = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content) # Adds the AI message to the history
    
    print(f"AI: {ai_response.content}")