from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace

llm=HuggingFacePipeline.from_model_id(
    model_id="openai/gpt-oss-120b",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("what is capital of india?")
print(result.content)