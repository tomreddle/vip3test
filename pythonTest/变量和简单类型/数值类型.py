# python支持的数值类型
# 1.整型：四种表示形式
#   十进制：普通的整数
#   二进制：以0b或0B开头的整数
#   八进制：以0o或0O开头的整数
#   十六进制：以0x或0X开头的整数,10～15以字母a～f指代，不区分大小写
# 十六进制
hex_value1 = 0x13
hex_value2 = 0XaF
print(hex_value1, hex_value2)
# 八进制
oct_val1 = 0o54
oct_val2 = 0O17
print(oct_val1, oct_val2)
# 二进制
bin_val1 = 0b111
bin_val2 = 0B101
print(bin_val1, bin_val2)

# python3.x允许数值添加下划线作为分隔符，但不影响数值本身
one_million = 1_000_000
print(one_million)


# 2. 浮点型（保存小数点的数值）
# 表现形式分为两种
# 一、十进制形式  如5.12,5.120
# 二、科学计数法  如5.12e2（5.12×10^2）
# 需注意的是，只有浮点型数值才可以使用科学计数法
af1 = 5.23455556
af2 = 25.2345
f1 = 5.12e2
f2 = 5e3
print(af1)
print(af2)
print(f1)
print(f2)

# 复数（a + bj）
# 虚部使用j或J表示
# 如要对复数进行计算，可导入cmath()模块
ac1 = 3 + 0.2j
print(type(ac1))    # <class 'complex'>
print(ac1)          # (3+0.2j)
ac2 = 4 - 0.1j
print(ac1 + ac2)    # (7+0.1j)
# sqrt() 开方
import cmath
ac3 = cmath.sqrt(-1)
print(ac3)
