from method.analysis.analysis import Analysis
from method.query.query import Query
from time import sleep


"""
以下代码是依照 Analysis 和 Query
编写出的功能
"""


class Output(Analysis, Query):
    error = {
        'inputError': '您的号码校验码有误！',
        'lengthError': '您输入的长度有误！',
        'areaError': '麻烦检查一下您的号码是否输入有误，未查询到您的地址！'
    }
    endLyric = []

    def __init__(self, path: str = None):
        self.readAreaData(path)

    def dateWhereError(self, uid):
        data = self.get_time(uid)
        d1 = self.get_day(data)
        d2 = ''.join([d + k for k, d in zip(['年', '月', '日'], data)])
        print('您的出生日期是', d2, self.get_starSign(data[1:]), self.get_zodiac(data[0]))
        self.sexWhereError(uid)
        text = '等等，好像哪里不对劲'
        if d1 > 0:
            print(text, '==> 难道您还有%s天就要出生了？<==' % d1, 'Σ( ° △ °|||)︴')
        elif d1 == 0:
            print(text, '==> 您是今天出生吗？ <==', 'Σ( ° △ °|||)︴')

    def sexWhereError(self, uid):
        sex = self.get_gender(uid)
        text = '看来您还是一个'
        if sex:
            text += '可爱漂亮你女孩子呀！(>▽<)'
        else:
            text += '非常英俊潇洒的男孩子呀！✧(≖ ◡ ≖✿)'
        print(text)

    def areaWhereError(self, uid):
        area = self.get_area(uid)
        if area:
            print('您居住在%s' % ''.join(area))
            self.dateWhereError(uid)
        else:
            self.Error('areaError')

    def uidWhereError(self, uid):
        uid = self.get_uid15And18(uid)
        if isinstance(uid, str):
            self.Error(uid)
            return
        uid18, uid15 = uid
        for i in uid:
            print('您的%s位身份号为:' % len(i), i)
        self.areaWhereError(uid18)

    def Error(self, val: str):
        print(self.error[val])

    def input(self, text: str = None, *, uid: str = None):
        uid = uid or input(text)
        self.uidWhereError(uid)
        self.end()

    def end(self):
        input('\n看完了吗？看完了可以按下回车结束哟！\n看久了人家会害羞的 <= o(*////▽////*)q')

    def __del__(self):
        for txt in self.endLyric:
            print(txt)
            sleep(0.7)
        sleep(3)
