import json  # 引入 Python 自带的 JSON 处理工具箱

# 1. 打开并读取本地的 data.json 文件
# 'r' 代表 read（只读模式），encoding='utf-8' 防止中文乱码
with open('data.json', 'r', encoding='utf-8') as f:
    # 把文件里的文本内容，转换成 Python 可以操作的字典（dict）
    response = json.load(f)

print("--- 📂 成功读取本地 JSON 文件 ---")

# 2. 剥洋葱：拿到产品列表
product_list = response["data"]["products"]

print("\n--- 💰 正在自动筛选其中的【付费商品】 ---")

# 3. 循环遍历，并加入 if 条件判断
for product in product_list:
    name = product["name"]
    price = product["price"]
    
    # 核心测试逻辑：如果价格大于 0，说明是付费商品
    if price > 0:
        print(f"✨ 发现付费商品 -> 名称: {name} | 价格: ￥{price}")