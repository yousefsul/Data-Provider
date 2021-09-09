class GsDataProvider:
    def __init__(self, gs):
        self.__gs = gs
        self.__gs01 = None
        self.__gs02 = None
        self.__gs03 = None
        self.__gs04 = None
        self.__gs05 = None
        self.__gs06 = None
        self.__gs07 = None
        self.__gs08 = None

    def get_gs01(self):
        self.__gs01 = self.__gs.get('01')
        return self.__gs01

    def get_gs02(self):
        self.__gs02 = self.__gs.get('02')
        return self.__gs02

    def get_gs03(self):
        self.__gs03 = self.__gs.get('03')
        return self.__gs03

    def get_gs04(self):
        self.__gs04 = self.__gs.get('04')
        return self.__gs04

    def get_gs05(self):
        self.__gs05 = self.__gs.get('05')
        return self.__gs05

    def get_gs06(self):
        self.__gs06 = self.__gs.get('06')
        return self.__gs06

    def get_gs07(self):
        self.__gs07 = self.__gs.get('07')
        return self.__gs07

    def get_gs08(self):
        self.__gs08 = self.__gs.get('08')
        return self.__gs08
