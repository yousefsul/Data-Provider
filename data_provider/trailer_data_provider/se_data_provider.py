class SeDataProvider:
    def __init__(self, se):
        self.__se = se
        self.__se01 = None
        self.__se02 = None

    def get_se01(self):
        self.__se01 = self.__se.get('01')
        return self.__se01

    def get_se02(self):
        self.__se02 = self.__se.get('02')
        return self.__se02
