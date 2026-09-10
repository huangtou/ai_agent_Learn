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
        {"role":"system","content":"你是一个生活助手话不多"},
        {"role":"user","content":"你有2只猫"},
        {"role":"assistant","content":"好的"},
        {"role": "user", "content": "你有3只狗"},
        {"role": "assistant", "content": "好的"},
        {"role":"user","content":"你有几个小动物，怎么算的"}],
    # 流式输出
    stream=True,
)

for chunk in resp:
    print(chunk.choices[0].delta.content, end=" ")
    #end=" "表示以空格分割
    flush=True#离开刷新缓冲区

#print(resp.choices[0].message.content)