'''
terms = {
    "LLM" : "a language model that speaks like a human",
    "RAG" : "a way to add external sources to AI",
    "fine-tuning" : "a way to tailor models to specific queries",
    "Mistral" : "a French open-source language model",
    "Gemma" : "an open-source LLM by Google",
}
for key, value in terms.items():
    print(f"{key} is {value}")'
'''

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

should_take_poll = ['chris', 'edward', 'emma']
for person in should_take_poll:
    if person in favorite_languages.keys():
        print(f"Thanks for responding, {person.title()}!")
    else:
        print(f"You should take the poll, {person.title()}!")