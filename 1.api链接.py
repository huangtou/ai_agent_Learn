from openai import OpenAI

# 阿里云的api_key
# client = OpenAI(
#     #配置了环境变量就不需要再在这里写api了
#     base_url="https://ws-suj12dc4jj7ku8fr.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
# )
# # 测试，阿里云这里model填通义模型，例如 qwen‑turbo
# resp = client.chat.completions.create(
#     model="qwen-turbo",
#     messages=[{"role":"user","content":"你好,你是谁，你能干什么"}]
# )
# print(resp.choices[0].message.content)

#调用本地Ollama模型
client = OpenAI(
    #配置了环境变量就不需要再在这里写api了
    base_url="http://localhost:11434/v1"
)
resp = client.chat.completions.create(
    model="qwen3:4b",
    messages=[{"role":"user","content":"你好,你是谁，你能干什么"}]
)
print(resp.choices[0].message.content)
