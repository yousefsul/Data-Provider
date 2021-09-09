class BhtDataProvider:
    def __init__(self, bht):
        self.__bht = bht
        self.__bht01 = None
        self.__bht02 = None
        self.__bht03 = None
        self.__bht04 = None
        self.__bht05 = None
        self.__bht06 = None

    def get_bht01(self):
        self.__bht01 = self.__bht.get('01')
        return self.__bht01

    def get_bht02(self):
        self.__bht02 = self.__bht.get('02')
        return self.__bht02

    def get_bht03(self):
        self.__bht03 = self.__bht.get('03')
        return self.__bht03

    def get_bht04(self):
        self.__bht04 = self.__bht.get('04')
        return self.__bht04

    def get_bht05(self):
        self.__bht05 = self.__bht.get('05')
        return self.__bht05

    def get_bht06(self):
        self.__bht06 = self.__bht.get('06')
        return self.__bht06
