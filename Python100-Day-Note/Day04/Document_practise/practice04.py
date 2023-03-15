#设计一个函数返回传入的列表中最大和第二大的元素的值。

def return_max(list):
    list1 = sorted(list)
    return list1[-1],list[-2]

def main():
    a = [1,3,5,7,233]
    print(return_max(a))
    
if __name__ == '__main__':
    main()