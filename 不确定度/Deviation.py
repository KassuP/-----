import math
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# # 中文字符不能正确显示可能是默认字符编码的错误（通过这里强制修改）

def calculate_standard_deviation():
    n = int(input("输入数据的数量 (n): "))
    if n <= 1:
        print("错误:n必须是大于1的整数。")
        return
    
    data = []
    for i in range(1, n+1):
        x = float(input(f"输入数据 x{i}: "))
        data.append(x)
    
    # 计算x的平均值
    mean = sum(data) / n
    
    # Calculate sum of squared differences
    sum_sq_diff = sum((x - mean) ** 2 for x in data)
    
    # 计算实验标准差
    standard_deviation = math.sqrt(sum_sq_diff / (n - 1))
    
    # 计算实验的A类不确定度
    if n == 2:
        z = 9.0
    elif n == 3:
        z = 2.5
    elif n == 4:
        z = 1.6
    elif n == 1.5:
        z =1.2
    elif 5 < n <=10:
        z = 1
    else:
        z = 2.0/math.sqrt(n)

    u = z*standard_deviation
    # 用科学计数法输出结果
    print(f"实验标准差 (科学计数法): {standard_deviation:.2e}")
    print(f"A类不确定度 (科学计数法): {u:.2e}")

# Call the function to calculate and display the standard deviation
calculate_standard_deviation()

input("回车 结束运行...")