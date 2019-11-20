import time


class LeapYear(object):
    '''判断某年是否为闰年，默认判断当前年'''
    def __init__(self, current_year=time.localtime().tm_year):
        self.current_year = current_year     # 获取当前年
    # print(current_year.tm_year)
    # 普通闰年:公历年份是4的倍数的   世纪闰年:公历年份是整百数的，必须是400的倍数

    def leap_year(self):
        if self.current_year % 100 == 0:
            if self.current_year % 400 == 0:
                print(str(self.current_year) + '年是闰年。')
            else:
                print(str(self.current_year) + '年不是闰年。')
        elif self.current_year % 4 == 0:
            print(str(self.current_year) + '年是闰年。')
        else:
            print(str(self.current_year) + '年不是闰年。')


if __name__ == '__main__':
    leap_judge = LeapYear()
    leap_judge.leap_year()
    leap_judge1 = LeapYear(2000)
    leap_judge1.leap_year()
