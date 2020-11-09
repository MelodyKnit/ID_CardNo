#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import time, localtime, strftime


class Query:
    zodiac = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    star_name = ['水瓶座	', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
    star_sign = [
        [[1, 21], [2, 19]],
        [[2, 20], [3, 20]],
        [[3, 21], [4, 20]],
        [[4, 21], [5, 21]],
        [[5, 22], [6, 21]],
        [[6, 22], [7, 22]],
        [[7, 23], [8, 23]],
        [[8, 24], [9, 23]],
        [[9, 24], [10, 23]],
        [[10, 24], [11, 22]],
        [[11, 23], [12, 21]],
        [[12, 22], [1, 1, 20]]
    ]

    @classmethod
    def get_starSign(cls, t: list):
        """
        判断十二星座某一星座
        :param t: 只需传入月和日
        提取t的月作为索引
        按照导入的天数来计算
        最小天数 < 当前天数 < 最大天数
        满足上述条件表示索引对应的星座
        不满足则表示为上一个星座也就是 t-1
        :return: str
        """
        t = [int(i) for i in t]
        t, _num = t[0]-1, cls.get_day(t, [0, 0, 0])
        _min, _max = (cls.get_day(i, [0, 0, 0]) for i in cls.star_sign[t])
        if _min <= _num <= _max:
            return cls.star_name[t]
        return cls.star_name[t-1]

    @classmethod
    def get_zodiac(cls, y: int or str):
        """
        :param y: 年份
        传入年份,出现的4表示2020年除12余4
        因为2020年是鼠年十二生肖的起点,取余后推导出4
        :return: str
        """
        y = int(y)
        return cls.zodiac[(y-4) % len(cls.zodiac)]

    @classmethod
    def get_day(cls, t: list, c: list = None):
        """
        用于只获取时间
        :param t: 出生年月日
        获取出生日期到今年已经多少天了，可以从而得出年龄
        大于0表示还没出生
        等于0表示今天刚出生
        :param c: 指点年份 全称 current
        也可以用于计算，传入指定年份来计算时间差
        :return: int
        这个计算的每月是按 365 / 12 估算出来的一个月，不属于自然月
        """
        if len(t) < 3: t.insert(0, 0)
        if not c: c = strftime('%Y %m %d', localtime(time())).split(' ')
        t = [int(i) for i in t]
        c = [int(i) for i in c]
        day = 0
        for i, j in enumerate([365, 365 / 12, 1]):
            day += (t[i] - c[i]) * j
        return cls.int(day)

    @staticmethod
    def int(num: float):
        if num % 1: num += -1 if num < 0 else 1
        return int(num)
