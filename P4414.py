"""
题目意思：
    按照所给的ABC顺序排列所给的三个数,A<B<C顺序
"""

# a,b,c = input().split()
# sequence = input()

'''
排列的可能:ABC,ACB,BAC,BCA,CAB,CBA
'''


def main():
    import sys

    # 读取第一行输入并转换为整数列表
    input_numbers = sys.stdin.readline().strip().split()
    '''
    
    sys是系统操作,需要 import sys
    stdin用于进行各种输入操作   stdin.read()读到结尾(EOT)   stdin.readline()读取一行
    输入的数据默认是str类型,也就是字符串类型，可以调用字符串的内置函数
    strip()去除输入内容里面的一些字符,默认是空格,也可以指定
    split()按字符分割,默认是空格
    
    '''
    numbers = list(map(int, input_numbers))

    # 排序，确保 A < B < C
    sorted_numbers = sorted(numbers)
    mapping = {'A': sorted_numbers[0], 'B': sorted_numbers[1], 'C': sorted_numbers[2]}  # 创建映射关系
    # map = {'A':sorted_numbers[0],'B':sorted_numbers[1],'C':sorted_numbers[2]}
    # 读取第二行输入，表示输出顺序
    order = sys.stdin.readline().strip()

    # 根据顺序映射对应的数值
    output_numbers = [str(mapping[char]) for char in order]  # 变成一个str列表
    # 列表推导式（List Comprehension）
    # output = [str(mapping[char]) for char in order]
    # 输出结果，用空格分隔
    print(' '.join(output_numbers))  # ' '.join()通过空格拼接


if __name__ == "__main__":
    main()
