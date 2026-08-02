product_list = [
    {"id": 1, "size": "m", "color": "white", "fabric": "cotton", "gender": "male", "stock":10},
    {"id": 2, "size": "l", "color": "red", "fabric": "synthetic", "gender": "female", "stock":20},
    {"id": 3, "size": "xl", "color": "black", "fabric": "linen", "gender": "male", "stock":30},
    {"id": 4, "size": "xxl", "color": "blue", "fabric": "satin", "gender": "female", "stock":40},
    {"id": 5, "size": "xxxl", "color": "merun", "fabric": "cotton", "gender": "male", "stock":50},
    {"id": 6, "size": "m", "color": "blue", "fabric": "linen", "gender": "female", "stock":10},
    {"id": 7, "size": "l", "color": "black", "fabric": "satin", "gender": "male", "stock":20},
    {"id": 8, "size": "xl", "color": "white", "fabric": "synthetic", "gender": "female", "stock":30},
    {"id": 9, "size": "xxl", "color": "merun", "fabric": "cotton", "gender": "male", "stock":40},
    {"id": 10, "size": "xxxl", "color": "red", "fabric": "linen", "gender": "female", "stock":50},
    {"id": 11, "size": "m", "color": "black", "fabric": "cotton", "gender": "male", "stock":10},
    {"id": 12, "size": "l", "color": "white", "fabric": "satin", "gender": "female", "stock":20},
    {"id": 13, "size": "xl", "color": "blue", "fabric": "synthetic", "gender": "male", "stock":30},
    {"id": 14, "size": "xxl", "color": "red", "fabric": "linen", "gender": "female", "stock":40},
    {"id": 15, "size": "xxxl", "color": "merun", "fabric": "satin", "gender": "male", "stock":50},
    {"id": 16, "size": "m", "color": "red", "fabric": "synthetic", "gender": "female", "stock":10},
    {"id": 17, "size": "l", "color": "merun", "fabric": "linen", "gender": "male", "stock":20},
    {"id": 18, "size": "xl", "color": "black", "fabric": "cotton", "gender": "female", "stock":30},
    {"id": 19, "size": "xxl", "color": "white", "fabric": "satin", "gender": "male", "stock":40},
    {"id": 20, "size": "xxxl", "color": "blue", "fabric": "cotton", "gender": "female", "stock":50},
]

size = input("Enter product size: ")
color = input("Enter product color: ")
fabric = input("Enter product fabric: ")
gender = input("Enter product gender: ")
stock = int(input("Enter product stock: "))

product = {
    "size": size,
    "color": color,
    "fabric": fabric,
    "gender": gender,
    "stock": stock,
}

product_list.append(product)

print(product_list)

id = int(input("Enter product id: "))
for product in product_list:
    if product["id"] == id:
        product_list.remove(product)
        break

print(product_list)