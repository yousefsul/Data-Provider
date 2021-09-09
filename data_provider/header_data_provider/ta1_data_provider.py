from data_provider.body_data_provider_999.ta105CodeDescription import get_ta105_definition
class Ta1DataProvider:
    def __init__(self, ta1):
        self.__ta1 = ta1
        self.__ta101 = None
        self.__ta102 = None
        self.__ta103 = None
        self.__ta104 = None
        self.__ta105 = None
        self.__ta105_definition = None

    def get_ta101(self):
        self.__ta101 = self.__ta1.get('01')
        return self.__ta101

    def get_ta102(self):
        self.__ta102 = self.__ta1.get('02')
        return self.__ta102

    def get_ta103(self):
        self.__ta102 = self.__ta1.get('03')
        return self.__ta102

    def get_ta104(self):
        self.__ta102 = self.__ta1.get('04')
        return self.__ta102

    def get_ta105(self):
        self.__ta102 = self.__ta1.get('05')
        return self.__ta102

    def get_ta105_definition(self):
        return get_ta105_definition(self.get_ta105())