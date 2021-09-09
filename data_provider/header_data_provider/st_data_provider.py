class StDataProvider:
    def __init__(self, st):
        self.__st = st
        self.__st01 = None
        self.__st02 = None
        self.__st03 = None

    def get_st01(self):
        self.__st01 = self.__st.get('01')
        return self.__st01

    def get_st02(self):
        self.__st02 = self.__st.get('02')
        return self.__st02

    def get_st03(self):
        self.__st03 = self.__st.get('03')
        return self.__st03
