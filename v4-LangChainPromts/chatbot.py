from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate,load_prompt
model = ChatOllama(
    model="llama3.2:1b"
)
chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input=input('you: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    else:
        result=model.invoke(chat_history)
        chat_history.append((AIMessage(content=result.content)))
        print('AI: ',result.content)
print(chat_history)
# history vich message hai pr eh ni pta ki chat message ai ne bhya ya user ne jd history bht bdi hojani fir ai ne confuse hojana
