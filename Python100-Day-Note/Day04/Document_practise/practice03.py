#设计一个函数返回给定文件名的后缀名。

def suffix_get(filename,hotdog):
    pos = filename.rfind('.')
    if 0<pos<len(filename)-1:
        index = pos if hotdog else pos+1
        return filename[index:]
    
def main():
    print(suffix_get('Wechat.jpeg',False))

if __name__ == '__main__':
    main()