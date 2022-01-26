class BprDataProvider:
    def __init__(self, payment):
        self.__payment = payment
        self.__bpr03_description = {
            "C": "Credit",
            "D": "Debit",
            "NP": "Not Provided",
        }
        self.__bpr04_description = {
            "ACH": "Automated Clearing House",
            "BOP": "Financial Institution Option",
            "CHK": "Check",
            "FWT": "Federal Reserve Funds/Wire Transfer - Nonrepetitive",
            "NON": "Non-Payment Data",
            "NP": "Not Provided",
        }
        self.__bpr01 = None
        self.__bpr02 = None
        self.__bpr03 = None
        self.__bpr04 = None
        self.__bpr05 = None
        self.__bpr06 = None
        self.__bpr07 = None
        self.__bpr08 = None
        self.__bpr09 = None
        self.__bpr10 = None
        self.__bpr11 = None
        self.__bpr12 = None
        self.__bpr13 = None
        self.__bpr14 = None
        self.__bpr15 = None
        self.__bpr16 = None
        self.__bpr = {}
        self.__build_bpr()
        self.__trn01 = None
        self.__trn02 = None
        self.__trn03 = None
        self.__trn04 = None
        self.__np = 'NP'
        self.__trn = {}
        self.__build_trn()

    def __build_bpr(self):
        for segment in self.__payment:
            if segment == 'BPR':
                self.__bpr = self.__payment.get(segment)

    def get_bpr01(self):
        if self.__bpr.get('01'):
            self.__bpr01 = self.__bpr.get('01')
        else:
            self.__bpr01 = self.__np
        return self.__bpr01

    def get_bpr02(self):
        if self.__bpr.get('02'):
            self.__bpr02 = self.__bpr.get('02')
        else:
            self.__bpr02 = self.__np
        return self.__bpr02

    def get_bpr03(self):
        if self.__bpr.get('03'):
            self.__bpr03 = self.__bpr.get('03')
        else:
            self.__bpr03 = "NP"
        return self.__bpr03

    def get_bpr04(self):
        if self.__bpr.get('04'):
            self.__bpr04 = self.__bpr.get('04')
        else:
            self.__bpr04 = "NP"
        return self.__bpr04

    def get_bpr05(self):
        self.__bpr05 = self.__bpr.get('05')
        return self.__bpr05

    def get_bpr06(self):
        self.__bpr06 = self.__bpr.get('06')
        return self.__bpr06

    def get_bpr07(self):
        self.__bpr07 = self.__bpr.get('07')
        return self.__bpr07

    def get_bpr08(self):
        self.__bpr08 = self.__bpr.get('08')
        return self.__bpr08

    def get_bpr09(self):
        self.__bpr09 = self.__bpr.get('09')
        return self.__bpr09

    def get_bpr10(self):
        self.__bpr10 = self.__bpr.get('10')
        return self.__bpr10

    def get_bpr11(self):
        self.__bpr11 = self.__bpr.get('11')
        return self.__bpr11

    def get_bpr12(self):
        self.__bpr12 = self.__bpr.get('12')
        return self.__bpr12

    def get_bpr13(self):
        self.__bpr13 = self.__bpr.get('13')
        return self.__bpr13

    def get_bpr14(self):
        self.__bpr14 = self.__bpr.get('14')
        return self.__bpr14

    def get_bpr15(self):
        self.__bpr15 = self.__bpr.get('15')
        return self.__bpr15

    def get_bpr16(self):
        self.__bpr16 = self.__bpr.get('16')
        return self.__bpr16

    def __build_trn(self):
        for segment in self.__payment:
            if segment == 'TRN':
                self.__trn = self.__payment.get(segment)

    def get_trn01(self):
        self.__trn01 = self.__trn.get('01')
        return self.__trn01

    def get_trn02(self):
        self.__trn02 = self.__trn.get('02')
        return self.__trn02

    def get_trn03(self):
        self.__trn03 = self.__trn.get('03')
        return self.__trn03

    def get_trn04(self):
        self.__trn04 = self.__trn.get('04')
        return self.__trn04

    def get_bpr03_description(self):
        return self.__bpr03_description.get(self.__bpr03)

    def get_bpr04_description(self):
        return self.__bpr04_description.get(self.__bpr04)

