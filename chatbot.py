import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence




load_dotenv()
openrouter_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    openai_api_key=openrouter_key,
    openai_api_base="https://openrouter.ai/api/v1",  
    model="mistralai/mistral-7b-instruct:free",
   
)


schema = [
    ResponseSchema(name="reply", description="Reply to the user's message in a helpful tone")
]
parser = StructuredOutputParser.from_response_schemas(schema)


prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Chat history:
{chat_history}

User: {message}

{format_instructions}
""",
    input_variables=["message", "chat_history"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


chain = prompt | llm | parser


chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

print(" Chatbot is ready. Type 'exit' to quit.\n")


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break

   
    chat_history.append(HumanMessage(content=user_input))

    
    formatted_history = ""
    for msg in chat_history:
        if isinstance(msg, HumanMessage):
            formatted_history += f"User: {msg.content}\n"
        elif isinstance(msg, AIMessage):
            formatted_history += f"AI: {msg.content}\n"

  
    result = chain.invoke({"message": user_input, "chat_history": formatted_history})

   
    chat_history.append(AIMessage(content=result["reply"]))

  
    print("AI:", result["reply"])