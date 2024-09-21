import math

# 计算三角形的面积（已知三边，使用海伦公式）
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

a,b,c = input().split()

area = triangle_area(float(a), float(b), float(c))
formated_area = "{:.1f}".format(area)
print(formated_area)  # 输出: 6.0
