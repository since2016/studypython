

# 不可变， iterable
name_tuple = ('bobby1', 12,32)
name_tuple = ('bohhd', 32,54343, 'beigjin')

#拆包
name , age, value ,*other= name_tuple
print(name, age, value, other)

# 不可变不绝对
name_tuple = ('nae', [239, 10323])
name_tuple[1].append(432)
print(name_tuple)

# immutable的重要性 ,性能优化， 线程安全， 可以作为dict的key, 拆包特效//
# 如果拿 c语言类比， tuple 对应struct, list 对应array