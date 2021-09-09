class IeaDataProvider:
    def __init__(self, iea):
        self.__iea = iea
        self.__iea01 = None
        self.__iea02 = None

    def get_iea01(self):
        self.__iea01 = self.__iea.get('01')
        return self.__iea01

    def get_iea02(self):
        self.__iea02 = self.__iea.get('02')
        return self.__iea02
