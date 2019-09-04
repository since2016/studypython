from collections import namedtuple

User = namedtuple("User", ['name', 'age', 'height', 'edu'])
# 类比定义class
user = User(name='zh', age = 29, height=158)

# 使用tuple 和dict也可以初始化一个实例
user_tuple=('zheng', 23, 190)
user = User(*user_tuple, edu='master')
user_dict = {
    "name":"zheng",
    "age":32,
    "height":179
}

user = User(*user_dict, edu='master')

print(user.age, user.height)

## 可以拆包