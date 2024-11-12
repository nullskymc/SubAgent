import json

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 读取配置文件
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

api_key = config['apikey']
endpoint = config['endpoint']
model_name = config['modelName']

#实例化模型
chat_model = ChatOpenAI(api_key=api_key, base_url=endpoint, model=model_name)
#embeddings = OpenAIEmbeddings(api_key=api_key, base_url=endpoint)


if __name__ == '__main__':
    print(chat_model.invoke("你好").content)