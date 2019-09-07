import re

var1 = "hello, users"
print(var1[:6],'user!')

print(re.match('www','www.baidu.com').span())
print(re.search('www', 'www.baidu.com').span())
