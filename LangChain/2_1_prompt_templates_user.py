from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())

llm = ChatMistralAI(model="mistral-small-latest")

template = """Write a {tone} email to a decision-maker in {company} asking if
    they are interested in {service}. Keep it to 4 lines max."""

prompt_template = ChatPromptTemplate.from_template(template)

# takes an OBJECT, in this case a dictionary, by invoking converts it into a format Langchain can understand (HumanMessage)
prompt = prompt_template.invoke({
    "tone": "casual",
    "company": "KPMG",
    "service": "custom software development"
})

result = llm.invoke(prompt) # So basicaly the argument can be whatever
print (result.content)