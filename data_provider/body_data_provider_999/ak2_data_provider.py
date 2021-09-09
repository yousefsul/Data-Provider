from data_provider.body_data_provider_999.ik403CodeDescription import get_ik403_definition
from data_provider.body_data_provider_999.ik304CodeDescription import get_ik304_definition
from data_provider.body_data_provider_999.ik502CodeDescription import get_ik502_definition


class Ak2DataProvider:
    def __init__(self, ak2):
        self.__ak2 = ak2
        self.__segment = None
        self.__ak201 = None
        self.__ak202 = None
        self.__ak203 = None
        self.__ik3 = {}
        self.__ik3_first_context, self.__ik3_second_context = {}, {}
        self.__count_ik3_ctx = 0
        self.__ik301 = None
        self.__ik302 = None
        self.__ik303 = None
        self.__ik304 = None
        self.__ik304_definition = None
        self.__ik4 = {}
        self.__ik4_first_context = {}
        self.__ik401 = None
        self.__ik402 = None
        self.__ik403 = None
        self.__ik403_definition = None
        self.__ik5 = {}
        self.__ik501 = None
        self.__ik502 = None
        self.__ik502_definition = None
        self.__bulid_sub_loops()

    def get_ak201(self):
        self.__ak201 = self.__ak2.get('01')
        return self.__ak201

    def get_ak202(self):
        self.__ak202 = self.__ak2.get('02')
        return self.__ak202

    def get_ak203(self):
        self.__ak203 = self.__ak2.get('03')
        return self.__ak203

    def get_ik501(self):
        self.__ik501 = self.__ik5.get('01')
        return self.__ik501

    def get_ik502(self):
        self.__ik502 = self.__ik5.get('02')
        return self.__ik502

    def get_ik301(self):
        self.__ik301 = self.__ik3.get('01')
        return self.__ik301

    def get_ik302(self):
        self.__ik302 = self.__ik3.get('02')
        return self.__ik302

    def get_ik303(self):
        self.__ik303 = self.__ik3.get('03')
        return self.__ik303

    def get_ik304(self):
        self.__ik304 = self.__ik3.get('04')
        return self.__ik304

    def get_ik304_definition(self):
        return self.__ik304_definition

    def get_ik502_definition(self):
        return self.__ik502_definition

    def __bulid_ik4(self):
        for segment in self.__ak2.get(self.__segment):
            if segment.split('-')[0] == 'IK4':
                self.__ik4 = self.__ak2.get(self.__segment).get(segment)
                self.__bulid_ik4_context()
                self.__ik403_definition = get_ik403_definition(self.get_ik403())

    def get_ik401(self):
        self.__ik401 = self.__ik4.get('01')
        return self.__ik401

    def get_ik402(self):
        self.__ik402 = self.__ik4.get('02')
        return self.__ik402

    def get_ik403(self):
        self.__ik403 = self.__ik4.get('03')
        return self.__ik403

    def get_ik403_definition(self):
        return self.__ik403_definition

    def __bulid_sub_loops(self):
        for self.__segment in self.__ak2:
            if self.__segment.split('-')[0] == 'IK5':
                self.__ik5 = self.__ak2.get(self.__segment)
                if self.get_ik502():
                    self.__ik502_definition = get_ik502_definition(self.get_ik502())

            if self.__segment.split('-')[0] == 'IK3':
                self.__ik3 = self.__ak2.get(self.__segment)
                self.__bulid_ik3_context()
                self.__ik304_definition = get_ik304_definition(self.get_ik304())
                self.__bulid_ik4()

    def __bulid_ik3_context(self):
        for segment in self.__ak2.get(self.__segment):
            if segment.split('-')[0] == 'CTX':
                if self.__count_ik3_ctx == 0:
                    self.__ik3_first_context = self.__ak2.get(self.__segment).get(segment)
                    self.__count_ik3_ctx += 1

                if self.__count_ik3_ctx == 1:
                    self.__ik3_second_context = self.__ak2.get(self.__segment).get(segment)

    def __bulid_ik4_context(self):
        for segment in self.__ak2.get(self.__segment):
            if segment.split('-')[0] == 'CTX':
                self.__ik4_first_context = self.__ak2.get(self.__segment).get(segment)

    def get_ik3_context_01(self):
        return self.__ik3_first_context.get('01')


