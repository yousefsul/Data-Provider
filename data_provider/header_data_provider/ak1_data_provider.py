class Ak1DataProvider:
    def __init__(self, ak1):
        self.__ak1 = ak1
        self.__ak101 = None
        self.__ak102 = None
        self.__ak103 = None

    def get_ak101(self):
        self.__ak101 = self.__ak1.get('01')
        return self.__ak101

    def get_ak102(self):
        self.__ak102 = self.__ak1.get('02')
        return self.__ak102

    def get_ak103(self):
        self.__ak103 = self.__ak1.get('03')
        return self.__ak103
