import json
#字典列表转化为JSON用 json.dumps(对象，ensure_ascii=False)
#ensure_ascii=False 确保中文不乱码
#JSON转化为python用 json.loads(对象)
#创建字典
dict_list = {
    "name": "张三",
    "age": 20,
    "gender": "男",
    "address": "北京市"
}

#字典转换为JSON结构  ensure_ascii=False 确保中文不乱码
json_data = json.dumps(dict_list, ensure_ascii=False)
print(json_data)

li=[
{
    "name": "张三",
    "age": 20,
    "gender": "男",
    "address": "北京市"
},
{
    "name": "张三",
    "age": 20,
    "gender": "男",
    "address": "北京市"
},
{
    "name": "张三",
    "age": 20,
    "gender": "男",
    "address": "北京市"
}
]
json_data1 = json.dumps(li, ensure_ascii=False)
print(json_data1)

json_str='{"name": "张三", "age": 20, "gender": "男", "address": "北京市"}'
#JSON转化为python
dict_data = json.loads(json_str)
print(type(dict_data))
print(type(json_str))