def main():
    try:
        with open('guido.png','rb') as fs:
            data = fs.read()
            print(type(data))
        with open('jido.png','wb') as fs2:
            fs2.write(data)
    
    except IOError as e:
        print('读写文件时出错')
    except FileNotFoundError as w:
        print('指定的文件无法打开.')
    print('程序执行结束')

if __name__ == '__main__':
    main()
        