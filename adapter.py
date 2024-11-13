import json
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


# 读取配置文件
def read_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config


config = read_config()

api_key = config['apikey']
endpoint = config['endpoint']
model_name = config['modelName']

# 实例化模型
chat_model = ChatOpenAI(api_key=api_key, base_url=endpoint, model=model_name)
# embeddings = OpenAIEmbeddings(api_key=api_key, base_url=endpoint),


if __name__ == '__main__':
    print(chat_model.invoke("你好").content)
