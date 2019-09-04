from  collections import ChainMap

dict1 = {"a":"hobby", 'b':"adfs"}
dict2 = {"c":"hobby", "d":"wewrw"}

new_dict = ChainMap(dict1, dict2)
for k, v in new_dict.items():
    print(k, v)

new_dict.new_child({"aa":"ad","cd":"da"})

print(new_dict.maps)
new_dict.maps[0]['a']="boby"
print(new_dict)