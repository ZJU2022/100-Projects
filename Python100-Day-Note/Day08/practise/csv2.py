#写入csv文件
import csv
class Teacher:
    def __init__(self,name,age,title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1
    
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def title(self):
        return self.__title
    

def main():
    filename = 'teacher.csv'
    teachers = [Teacher('林飞武',22,'统计学'),Teacher('陆小容',21,'汉语言国际教育')]

    try:
        with open(filename,'w',encoding='utf-8') as f:
            '''csv.writer(csvfile, dialect='excel', **fmtparams)  返回一个 writer 对象，该对象负责将用户的数据在给定的文件类对象上转换为带分隔符的字符串。 '''
            write = csv.writer(f)
            for teacher in teachers:
                write.writerow([teacher.name,teacher.age,teacher.title])
    
    except BaseException as e:
        print('无法写入文件:',filename)
    else:
        print('操作完成')
            
if __name__ == '__main__':
    main()

    