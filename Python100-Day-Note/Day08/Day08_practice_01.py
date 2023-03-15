'''
https://github.com/ZJU2022/Python-100-Days/blob/master/Day01-15/11.%E6%96%87%E4%BB%B6%E5%92%8C%E5%BC%82%E5%B8%B8.md
python操作文件
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），然后通过encoding参数指定编码（如果不指定，默认值是None，
那么在读取文件时使用的是操作系统默认的编码），如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，
那么就可能因无法解码字符而导致读取失败。下面的例子演示了如何读取一个纯文本文件。
'''

def main():
    f = open('致橡树.txt', 'r',encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()
    