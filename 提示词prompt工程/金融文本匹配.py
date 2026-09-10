from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    #base_url="http://localhost:11434/v1"
)

examples_data = {
    "是": [
        ("公司ABC发布了季度财报，显示盈利增长。", "财报披露，公司ABC利润上升。"),
        ("公司ITCAST发布了年度财报，显示盈利大幅度增长。", "财报披露，公司ITCAST更赚钱了。")
    ],
    "不是": [
        ("黄金价格下跌，投资者抛售。", "外汇市场交易额创下新高。"),
        ("央行降息，刺激经济增长。", "新能源技术的创新。")
    ]
}

questions = [
    ("利率上升，影响房地产市场。", "高利率对房地产有一定的冲击。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]

#组装message
messages = [{"role": "system", "content": "你是一个金融专家，请根据以下示例判断文本是否匹配。"}]
for label, examples in examples_data.items():
    messages.append({"role": "user", "content": f"句子1:{examples[0][0]},句子2：{examples[0][1]}"})
    messages.append({"role": "assistant", "content": label})

#组装问题
for question in questions:
    messages.append({"role": "user", "content": f"句子1:{question[0]},句子2：{question[1]}"})
    resp = client.chat.completions.create(
        model="qwen-turbo",
        messages=messages
    )
    print(resp.choices[0].message.content)