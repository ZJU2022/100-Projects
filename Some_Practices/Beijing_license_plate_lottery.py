#允许用户最多选3次
#每次放出20个车牌供用户选择
#京[A-Z]-[XXXXX],数字和字母在组合
import string
import random

#A-Z
second_letter = string.ascii_uppercase
#5个随机数含大写字母和数字
third_letter = string.ascii_uppercase+string.digits
car_nums = []
count = 0
while count < 3:
    for i in range(20):
        car_num = f"京{''.join(random.sample(second_letter,1))}-{''.join(random.sample(third_letter,5))}"
        print(f'{i+1} {car_num}')
        car_nums.append(car_num)
    choice = input('请输入心仪的车牌...:').strip()
    if choice in car_nums:
        exit(f"恭喜你选择成功，您的车牌为{choice}")
    else:
        print(f"您输入的车牌不存在，您还可以选择{2-count}次车牌")
    count += 1
  