def function(num):
    mylist = [num]
    while num!=1:
        if num%2==0:
            num = num//2
        else:
            num = num*3+1
        mylist.append(num)

    return mylist, len(mylist)-1

print(function(7))
