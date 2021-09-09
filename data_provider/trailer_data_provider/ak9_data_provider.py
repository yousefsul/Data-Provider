from data_provider.body_data_provider_999.ak901CodeDescription import get_ak901_definition


class Ak9DataProvider:
    def __init__(self, ak9):
        self.__ak9 = ak9
        self.__ak901 = None
        self.__ak902 = None
        self.__ak903 = None
        self.__ak904 = None
        self.__ak901_definition = None

    def get_ak901(self):
        self.__ak901 = self.__ak9.get('01')
        return self.__ak901

    def get_ak902(self):
        self.__ak902 = self.__ak9.get('02')
        return self.__ak902

    def get_ak903(self):
        self.__ak903 = self.__ak9.get('03')
        return self.__ak903

    def get_ak904(self):
        self.__ak904 = self.__ak9.get('01')
        return self.__ak904

    def get_ak901_definition(self):
        self.__ak901_definition = get_ak901_definition(self.get_ak901())
        return self.__ak901_definition
