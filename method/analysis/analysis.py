from csv import reader


class Analysis:
    area: dict = None
    path: str = 'idtoad.csv'
    debugger: bool = True

    @classmethod
    def _log(cls, msg):
        return msg if cls.debugger else None

    @classmethod
    def get_uid15And18(cls, uid: str):
        """
        :param uid:
        获取号码长度，满足15长度或18长度分别进行返回
        如果返回值是None表示填写信息有误
        :return:
        """
        length = len(uid)
        if length == 18:
            # 验证信息校验码是否正确
            if cls.check(uid):
                return uid, cls.get_15IdNum(uid)
            return cls._log('inputError')
        elif length == 15:
            return cls.get_18IdNum(uid), uid
        return cls._log('lengthError')

    @staticmethod
    def get_time(uid: str):
        """
        :param uid:
        [年, 月, 日]
        :return: list
        """
        return [uid[6:10], uid[10:12], uid[12: 14]]

    @classmethod
    def get_area(cls, uid: str):
        """
        :param uid: 身份证号码前6位用于从数据中查询对应地区
        程序会先查看当前类的 area 是否有信息，如果没用则通过路径获取当前位置的文件夹里的信息
        然后将信息赋值到 area
        重新执行 get_area
        :return: 返回以list的形式地区，如果没用查询到则返回False
        """
        if cls.area:
            uid = uid[:6]
            if uid in cls.area:
                return cls.area[uid]
        else:
            cls.readAreaData()
            return cls.get_area(uid)

    @classmethod
    def readAreaData(cls, path: str = None):
        """
        读取所在区域的所有数据，将其整合位字典(数组)
        :param path: 地区所在位置
        返回所以区域数据
        :return: dict
        """
        with open(path or cls.path, 'r') as file:
            cls.area = {i[0]: i[1:] for i in reader(file)}

    @classmethod
    def get_18IdNum(cls, uid: str):
        """
        :param uid: 身份证ID
        返回整改过的信息
        :return: str
        """
        uid = uid[:6]+'19'+uid[6:]
        uid += cls.code(uid)
        return uid

    @staticmethod
    def get_15IdNum(uid: str):
        """
        去掉年份的19年与验证码
        :return: str
        """
        return uid[:6] + uid[8:17]

    @staticmethod
    def get_gender(uid: str):
        """
        男 == False | 女 == True
        :return: bool
        """
        uid = int(uid[16:17])
        return not uid % 2

    @staticmethod
    def code(uid: str):
        """
        计算出号码尾数验证码
        计算：
            提取uid每一位和每一位索引
            index += 每一位 乘以 (2的(号码长度 减 当前索引次幂) 除以 11 取余)
        ----------------------------------------------------------------
        为什么11的取余而不是其他数字
        ps:
            因为校验码的数字是[0-10]
            而从0数到10是有11个数字
            在身份证号码18位，如果显示10便会变为19位
            解决10的问题就是将10替换为罗马数字Ⅹ
        :return: str
        """
        index = 0
        length = len(uid)   # 身份证长度
        for i, n in enumerate(uid):
            # i = 每一个数字索引值,n = 每一个数字
            index += int(n) * (2 ** (length - i) % 11)
        return {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7',
                6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}[index % 11]

    @classmethod
    def check(cls, uid: str):
        """
        :param uid:
        检查号码尾数的验证码是否满足
        :return: bool
        """
        # 提取验证码
        code = uid[17]
        # 验证码如果是x或Ⅹ统一转为大写X
        if code == 'x' or code == 'Ⅹ': code = 'X'
        return code == cls.code(uid[:17])
