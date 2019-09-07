from time import  time


def main():
    total = 0
    number_list = [x for x in range(1,100000001)]
    start = time()
    for num in number_list:
        total += num

    print(total)
    end = time()
    print('Executive time : %.3fs' % (end -start))


if __name__ == '__main__':
    main()