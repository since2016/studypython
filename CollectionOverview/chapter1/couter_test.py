from collections import Counter

users = ['a', 'b', 'c', 'a', 'b']
user_counter = Counter(users)
print(user_counter)

counter = Counter("abdsasdfasdf")
print(counter)

counter.update("adasdfwefefsf")
print(counter)

counter1 = Counter("adasdfwefefsf")
counter.update(counter1)
# top n 堆
print(counter.most_common(3))