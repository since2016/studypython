from collections import defaultdict

user_dict = {}

default_dict = defaultdict(int)
users = ['a', 'b', 'c', 'a', 'b']

for user in users:
    # 1.
    # if user not in user_dict:
    #     user_dict[user] = 0
    # else:
    #     user_dict[user] += 1
    #
    # # 2.
    # user_dict.setdefault(user, 0)

    # 3. defaultdict 可以在key第一次出现时候给他赋初始值
    default_dict[user]+=1
