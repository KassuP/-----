import math

def calculate_Body():
    print("输入您的性别,1代表男性,0代表女性")
    
    n = int(input("您的性别："))
    if n == 1:
        print("您是男性")
        z = 1
    elif n== 0:
        print("您是女性")
        z = 0
    else :
        print("请输入1或0")
        return
    
    # 输入身高、年龄、体重
    weight = float(input("输入您的体重(kg):"))
    height1 = float(input("输入您的身高(cm):"))
    age = int(input("输入您的年龄(year):"))

    height2 = height1/100

    # 计算BMI
    BMI = weight/(height2*height2)

    # 计算体脂率
    Bodyfat_fraction = 1.2*BMI+0.23*age-5.4-10.8*z

    # 计算代谢率REE
    if z == 1 :
        REE = 10*weight + 6.25*height1 -5*age +5
    else :
        REE = 10*weight + 6.25*height1 -5*age -161
    
    print(f"您的BMI是: {BMI:.2f}")
    print(f"您的体脂率是: {Bodyfat_fraction:.2f}%")
    print(f"您的基础代谢率REE是: {REE:.2f}Kcal")

# 使用函数
calculate_Body()
input("回车 结束运行...")
