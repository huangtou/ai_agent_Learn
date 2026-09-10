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
    base_url="http://localhost:11434/v1"#接入地址
)

#model指定模型是什么
#messages指定输入内容
#role指定角色 有user和assistant和system
# system是系统提示，设定ai的行为，性格比如设置成一个python专家
# user是用户输入
# assistant是模型输出 人为设定ai助手回复
#content指定内容

resp = client.chat.completions.create(
    model="qwen3:4b",
    messages=[{"role":"user","content":"你好,你是谁，你能干什么"}]
)
print(resp.choices[0].message.content)
