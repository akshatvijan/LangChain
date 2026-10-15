from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import ChatOllama
model = ChatOllama(
    model="llama3.2:1b"
)

# user message jo user bhjda hai eg what is capital of india
# ai message jo ai bhjda hai eg capital of india is new delhi
# system message jive koi role set krna hai eg you are a doctor tell me medicine for this generally in start of chat

message=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]
result=model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)