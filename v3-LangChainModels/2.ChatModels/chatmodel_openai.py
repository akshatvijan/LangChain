from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=1.8)
result=model.invoke('what is capital of india')
print(result.content)
# sirf sing ni aani addition data b aana


#temperature parametre

#temperature is a paramtre that controls the randomness of a language model's output.It affects how creative or deterministic the responses are
# lower value(0.0,0.3)-> more deterministic and predictable
# higher value(0.7,1.5)->More random,creative and diverse