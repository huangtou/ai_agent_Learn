from openai import OpenAI
# 阿里云的api_key
client = OpenAI(
    #配置了环境变量就不需要再在这里写api了
    base_url="https://ws-suj12dc4jj7ku8fr.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)
# 测试，阿里云这里model填通义模型，例如 qwen‑turbo
resp = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {"role":"system","content":"你是一个python专家并且不说废话"},
        {"role":"assistant","content":"好的 我是python专家话不多"},
        {"role":"user","content":"用python输出1-10"}]
)
print(resp.choices[0].message.content)