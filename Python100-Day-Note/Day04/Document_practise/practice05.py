#输入学生考生成绩，输出每个学生及其对应的分数以及平均分

from re import S


def main():
    number = int(input('请输入学生的数量：'))
    Student_names = [None]*number
    Student_score = [None]*number
     
    for index in range(number):
        Student_names[index] = input("请输入第%d 个学生的名字: " %(index+1))
        Student_score[index] = float(input("请输入第%d个学生的成绩: " %(index+1)))
    
    sum = 0
    for i in range(len(Student_names)):
        sum += Student_score[i]
    print(sum/len(Student_names))
        
    
    
if __name__ == '__main__':
    main()