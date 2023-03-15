#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import code
import random
def verification_code(len_code=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)
    code = ''
    for _ in range(len_code):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

def main():
    print(verification_code(5))

if __name__ == '__main__':
    main()
    