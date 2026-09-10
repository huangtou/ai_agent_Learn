from openai import OpenAI
# 阿里云的api_key
client = OpenAI(
    #配置了环境变量就不需要再在这里写api了
    #base_url="https://ws-suj12dc4jj7ku8fr.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    base_url="http://localhost:11434/v1"#接入地址本地
)

#事例数据
example_data={
    "新闻报道":"今日，股市经历了一轮震荡，受宏观经济数据和全球贸易局势的影响，投资者密切关注美联储政策调整，以适应市场不确定性",
    "体育赛事":"在昨晚的篮球比赛中，湖人队以101-89战胜了勇士队，詹姆斯和浓眉哥再次展现出了出色的表现，他们各自贡献了25分和20分",
    "娱乐新闻":"著名歌手周杰伦在昨晚的演唱会中，演唱了多首经典歌曲，包括《稻香》、《晴天》等，现场气氛热烈，观众反响热烈",
    "科技新闻":"谷歌公司宣布推出一款名为Pixel 7的新款智能手机，该手机采用了最新的Tensor处理单元，具有更快的计算速度和更低的能耗"
}

#分类类型
categories=["新闻报道","体育赛事","娱乐新闻","科技新闻"]

#四个不同类型以上新的文本问题
new_texts=["受国内消费数据以及海外市场波动影响，今日国内大宗商品市场出现明显波动，不少行业从业者正在密切关注后续政策导向，以此应对市场带来的各类风险",
           "在昨晚的足球比赛中，曼联队以3-1战胜了利物浦队，C罗在比赛中贡献了2个进球，再次展现出了出色的个人能力",
           "知名演员黄渤新电影正式官宣定档，影片聚焦普通人现实生活，一众实力派演员加盟，不少影迷表示十分期待影片正式上映",
           "苹果公司宣布推出一款名为iPhone 14的新款智能手机，该手机采用了最新的A15芯片，具有更快的计算速度和更低的能耗，同时支持5G网络",
           "你是谁"]

#创建
messages=[{"role": "system", "content": "你是文本分类专家，将文本分类为：['新闻报道','体育赛事','娱乐新闻','科技新闻']类型 如果不清楚请分类为 '不知道'"}]
#添加few
for category,text in example_data.items():
    messages.append({"role": "user", "content":text} )
    messages.append({"role": "assistant", "content":category} )

#print(messages)
#提问
for q in new_texts:
    resp=client.chat.completions.create(
        #model="qwen-turbo",
        model="qwen3:4b",#本地模型
        messages=messages+[{"role":"user","content":f"按照示例回答这段文本的类别{q}"}]
    )
    print(f"问题：{q}")

    print(resp.choices[0].message.content)