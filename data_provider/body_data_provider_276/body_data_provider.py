
from data_provider.body_data_provider_276 import loop2000A
from data_provider.body_data_provider_276 import loop2100A
from data_provider.body_data_provider_276 import loop2000B
from data_provider.body_data_provider_276 import loop2100B
from data_provider.body_data_provider_276 import loop2000C
from data_provider.body_data_provider_276 import loop2100C
from data_provider.body_data_provider_276 import loop2000D
from data_provider.body_data_provider_276 import loop2100D
from data_provider.body_data_provider_276 import loop2200D


class BodyDataProvider:
    def __init__(self, ack_dict):
        self.ack_dict = ack_dict
        self.__loop2000a_hl = loop2000A.get_hl(self.ack_dict.get('2000A'))
        self.__loop2100a_nm1 = loop2100A.get_loop2100a_nm1(self.ack_dict.get('2000A'))
        self.__loop2000b_hl = loop2000B.get_hl(self.ack_dict.get('2000B'))
        self.__loop2100b_nm1 = loop2100B.get_loop2100b_nm1(self.ack_dict.get('2000B'))
        self.__loop2000c_hl = loop2000C.get_hl(self.ack_dict.get('2000C'))
        self.__loop2100c_nm1 = loop2100C.get_loop2100c_nm1(self.ack_dict.get('2000C'))
        self.__loop2000d_hl = loop2000D.get_loop2000d_hl(self.ack_dict.get('2000D'))
        self.__loop2000d_dmg = loop2000D.get_loop2000d_dmg(self.ack_dict.get('2000D'))
        self.__loop2100d_nm1 = loop2100D.get_loop2100d_nm1(self.ack_dict.get('2000D'))
        self.__loop2200d_trn = loop2200D.get_loop2200d_trn(self.ack_dict.get('2000D'))
        self.__loop2200d_ref = loop2200D.get_loop2200d_ref(self.ack_dict.get('2000D'))
        self.__loop2200d_amt = loop2200D.get_loop2200d_amt(self.ack_dict.get('2000D'))
        self.__loop2200d_dtp = loop2200D.get_loop2200d_dtp(self.ack_dict.get('2000D'))

    def get_loop2000a_hl01(self):
        return self.__loop2000a_hl.get('01')

    def get_loop2000a_hl02(self):
        return self.__loop2000a_hl.get('02')

    def get_loop2000a_hl03(self):
        return self.__loop2000a_hl.get('03')

    def get_loop2000a_hl04(self):
        return self.__loop2000a_hl.get('04')

    def get_loop2100a_nm101(self):
        return self.__loop2100a_nm1.get('01')

    def get_loop2100a_nm102(self):
        return self.__loop2100a_nm1.get('02')

    def get_loop2100a_nm103(self):
        return self.__loop2100a_nm1.get('03')

    def get_loop2100a_nm104(self):
        return self.__loop2100a_nm1.get('04')

    def get_loop2100a_nm105(self):
        return self.__loop2100a_nm1.get('05')

    def get_loop2100a_nm106(self):
        return self.__loop2100a_nm1.get('06')

    def get_loop2100a_nm107(self):
        return self.__loop2100a_nm1.get('07')

    def get_loop2100a_nm108(self):
        return self.__loop2100a_nm1.get('08')

    def get_loop2100a_nm109(self):
        return self.__loop2100a_nm1.get('09')

    def get_loop2000b_hl01(self):
        return self.__loop2000b_hl.get('01')

    def get_loop2000b_hl02(self):
        return self.__loop2000b_hl.get('02')

    def get_loop2000b_hl03(self):
        return self.__loop2000b_hl.get('03')

    def get_loop2000b_hl04(self):
        return self.__loop2000b_hl.get('04')

    def get_loop2100b_nm101(self):
        return self.__loop2100b_nm1.get('01')

    def get_loop2100b_nm102(self):
        return self.__loop2100b_nm1.get('02')

    def get_loop2100b_nm103(self):
        return self.__loop2100b_nm1.get('03')

    def get_loop2100b_nm104(self):
        return self.__loop2100b_nm1.get('04')

    def get_loop2100b_nm105(self):
        return self.__loop2100b_nm1.get('05')

    def get_loop2100b_nm106(self):
        return self.__loop2100b_nm1.get('06')

    def get_loop2100b_nm107(self):
        return self.__loop2100b_nm1.get('07')

    def get_loop2100b_nm108(self):
        return self.__loop2100b_nm1.get('08')

    def get_loop2100b_nm109(self):
        return self.__loop2100b_nm1.get('09')

    def get_loop2000c_hl01(self):
        return self.__loop2000c_hl.get('01')

    def get_loop2000c_hl02(self):
        return self.__loop2000c_hl.get('02')

    def get_loop2000c_hl03(self):
        return self.__loop2000c_hl.get('03')

    def get_loop2000c_hl04(self):
        return self.__loop2000c_hl.get('04')

    def get_loop2100c_nm101(self):
        return self.__loop2100c_nm1.get('01')

    def get_loop2100c_nm102(self):
        return self.__loop2100c_nm1.get('02')

    def get_loop2100c_nm103(self):
        return self.__loop2100c_nm1.get('03')

    def get_loop2100c_nm104(self):
        return self.__loop2100c_nm1.get('04')

    def get_loop2100c_nm105(self):
        return self.__loop2100c_nm1.get('05')

    def get_loop2100c_nm106(self):
        return self.__loop2100c_nm1.get('06')

    def get_loop2100c_nm107(self):
        return self.__loop2100c_nm1.get('07')

    def get_loop2100c_nm108(self):
        return self.__loop2100c_nm1.get('08')

    def get_loop2100c_nm109(self):
        return self.__loop2100c_nm1.get('09')

    def get_loop2000d_hl01(self):
        return self.__loop2000d_hl.get('01')

    def get_loop2000d_hl02(self):
        return self.__loop2000d_hl.get('02')

    def get_loop2000d_hl03(self):
        return self.__loop2000d_hl.get('03')

    def get_loop2000d_hl04(self):
        return self.__loop2000d_hl.get('04')

    def get_loop2000d_dmg01(self):
        return self.__loop2000d_dmg.get('01')

    def get_loop2000d_dmg02(self):
        return self.__loop2000d_dmg.get('02')

    def get_loop2000d_dmg03(self):
        return self.__loop2000d_dmg.get('03')

    def get_loop2100d_nm101(self):
        return self.__loop2100d_nm1.get('01')

    def get_loop2100d_nm102(self):
        return self.__loop2100d_nm1.get('02')

    def get_loop2100d_nm103(self):
        return self.__loop2100d_nm1.get('03')

    def get_loop2100d_nm104(self):
        return self.__loop2100d_nm1.get('04')

    def get_loop2100d_nm105(self):
        return self.__loop2100d_nm1.get('05')

    def get_loop2100d_nm106(self):
        return self.__loop2100d_nm1.get('06')

    def get_loop2100d_nm107(self):
        return self.__loop2100d_nm1.get('07')

    def get_loop2100d_nm108(self):
        return self.__loop2100d_nm1.get('08')

    def get_loop2100d_nm109(self):
        return self.__loop2100d_nm1.get('09')

    def get_loop2200d_dtp01(self):
        return self.__loop2200d_dtp.get('01')

    def get_loop2200d_dtp02(self):
        return self.__loop2200d_dtp.get('02')

    def get_loop2200d_dtp03(self):
        return self.__loop2200d_dtp.get('03')

    def get_loop2200d_amt01(self):
        return self.__loop2200d_amt.get('01')

    def get_loop2200d_amt02(self):
        return self.__loop2200d_amt.get('02')

    def get_loop2200d_ref01(self):
        return self.__loop2200d_ref.get('01')

    def get_loop2200d_ref02(self):
        return self.__loop2200d_ref.get('02')

    def get_loop2200d_trn01(self):
        return self.__loop2200d_trn.get('01')

    def get_loop2200d_trn02(self):
        return self.__loop2200d_trn.get('02')
