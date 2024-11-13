import asyncio
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from adapter import chat_model

output_parser = StrOutputParser()


async def base_chat(user_input: str, history: list | None = None):
    template_prompt = [
        ("system", "You are a helpful AI bot."),
    ]

    user_prompt = ("human", user_input)

    if history is None:
        history = [("system", "You are a helpful AI bot.")]
    # 将用户输入添加到 history
    history.append(user_prompt)

    prompt = ChatPromptTemplate(history)
    chain = prompt | chat_model | output_parser
    response = chain.invoke({})
    # 将 AI 的回复添加到 history
    history.append(("ai", response))

    return response, history


if __name__ == "__main__":
    history = None
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["退出", "exit", "quit"]:
            print("聊天结束。")
            break
        response, history = asyncio.run(base_chat(user_input, history))
        print(f"AI: {response}")
