# 1. 模拟一个产品查询接口返回的响应数据（在 Python 里这叫字典 dict）
response = {
    "code": 200,
    "message": "success",
    "data": {
        "total": 2,
        "products": [
            {"id": 1001, "name": "AI 测试助手测试版", "price": 0.0},
            {"id": 1002, "name": "自动化测试高级课程", "price": 199.0}
        ]
    }
}

# 2. 自动化测试中最常做的事：断言（Assert）状态码
# 提取 code
status_code = response["code"]
print("--- 检查状态码 ---")
print(f"接口返回的状态码是: {status_code}")


# 3. 进阶：提取复杂的嵌套数据
print("\n--- 提取产品列表 ---")
# 顺着层级一层层往下找：response -> data -> products
product_list = response["data"]["products"]

# product_list 包含两个产品，它是一个列表（list）
# 我们用 for 循环把里面的商品名字和价格依次打印出来
for product in product_list:
    name = product["name"]
    price = product["price"]
    print(f"商品名称: {name} | 价格: {price}")