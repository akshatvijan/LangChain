from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("What is the capital of India")

print(result)

### this is llm code not preferred to be used we generally prefer to use chatmodels