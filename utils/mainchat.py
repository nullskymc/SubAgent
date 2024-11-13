import asyncio
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from adapter import chat_model

output_parser = StrOutputParser()


async def base_chat(user_input: str, history: list | None = None):
    template_prompt = [
        ("system", "You are a helpful AI bot."),
    ]

    user_prompt = ("human", "{user_input}"),

    if history is None:
        history = template_prompt
    elif history != template_prompt:
        history = template_prompt.append(user_prompt)

    prompt = ChatPromptTemplate(history)
    chain = prompt | chat_model | output_parser
    response = chain.invoke({"user_input": user_input})
    history.append(("ai", response))

    return response, history


if __name__ == "__main__":
    user_input = input("Please input: ")
    response, history = asyncio.run(base_chat(user_input))
    print(response, history)
