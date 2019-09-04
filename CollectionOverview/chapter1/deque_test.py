from collections import  deque

# 可迭代的变量初始化
user_deque = deque(('zhe', 'zhegng', 178))
print(user_deque)

user_deque.appendleft(2323233)
print(user_deque)

# 源码文档
# deque copy 浅拷贝 ， 拷贝基本类型
import copy
copy.deepcopy() # 深拷贝。， 拷贝list等

# deque 是线程安全的