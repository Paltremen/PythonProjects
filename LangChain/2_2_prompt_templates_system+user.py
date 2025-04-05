from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())

llm = ChatMistralAI(model="mistral-small-latest")

# good for setting the system message at the same time; using TUPLES;
# cannot use HumanMessage, SystemMessage in .from_messages() because it doesn't recognize placeholders
# READ THE FUCKING DOCUMENTATION dude
messages = [
    ("system", "You are an assistant designed for reaching out to decision makers at {company}"),
    ("human", "Write a {tone} email advertising my company's {service} services. Keep it brief"),
]

# if it's a message thing like this, use the .from_messages() method
prompt_template = ChatPromptTemplate.from_messages(messages)

# takes an OBJECT, in this case a dictionary, by invoking converts it into a format Langchain can understand (HumanMessage, AIMessage)
prompt = prompt_template.invoke({
    "company": "Deloitte",
    "tone": "professional",
    "service": "custom software development"
})

result = llm.invoke(prompt) # So basicaly the argument can be whatever
print (result.content)