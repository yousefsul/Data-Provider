class GeDataProvider:
    def __init__(self, ge):
        self.__ge = ge
        self.__ge01 = None
        self.__ge02 = None

    def get_ge01(self):
        self.__ge01 = self.__ge.get('01')
        return self.__ge01

    def get_ge02(self):
        self.__ge02 = self.__ge.get('02')
        return self.__ge02
