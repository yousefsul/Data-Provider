from data_provider.body_data_provider_277 import loop2000A, loop2100A, loop2000B, loop2100B, loop2000C, loop2100C, \
    loop2000D, loop2100D, loop2200D, loop2220D


class BodyDataProvider:
    def __init__(self, ack_dict):
        self.ack_dict = ack_dict
        self.__loop2000a_hl = loop2000A.get_hl(self.ack_dict.get('2000A'))
        self.__loop2100a_nm1 = loop2100A.get_loop2100a_nm1(self.ack_dict.get('2100A'))

        self.__loop2000b_hl = loop2000B.get_hl(self.ack_dict.get('2000B'))
        self.__loop2100b_nm1 = loop2100B.get_loop2100b_nm1(self.ack_dict.get('2100B'))

        self.__loop2000c_hl = loop2000C.get_hl(self.ack_dict.get('2000C'))
        self.__loop2100c_nm1 = loop2100C.get_loop2100c_nm1(self.ack_dict.get('2100C'))

        self.__loop2000d_hl = loop2000D.get_hl(self.ack_dict.get('2000D'))
        self.__loop2100d_nm1 = loop2100D.get_loop2100d_nm1(self.ack_dict.get('2100D'))

        self.__loop2200d_trn = loop2200D.get_loop2200d_trn(self.ack_dict.get('2200D'))
        self.__loop2200d_stc = loop2200D.get_loop2200d_stc(self.ack_dict.get('2200D'))
        self.__loop2200d_ref_K1 = loop2200D.get_loop2200d_ref_1k(self.ack_dict.get('2200D'))
        self.__loop2200d_ref_EJ = loop2200D.get_loop2200d_ref_ej(self.ack_dict.get('2200D'))
        self.__loop2200d_dtp = loop2200D.get_loop2200d_dtp(self.ack_dict.get('2200D'))
        self.__loop2220d_svc = loop2220D.get_loop2200d_svc(self.ack_dict.get('2220D'))
        self.__loop2220d_stc = loop2220D.get_loop2200d_stc(self.ack_dict.get('2220D'))
        self.__loop2220d_dtp = loop2220D.get_loop2200d_dtp(self.ack_dict.get('2220D'))

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

    def get_loop2200d_trn01(self):
        return self.__loop2200d_trn.get('01')

    def get_loop2200d_trn02(self):
        return self.__loop2200d_trn.get('02')

    def get_loop2200d_stc01(self):
        return self.__loop2200d_stc.get('01')

    def get_loop2200d_stc02(self):
        return self.__loop2200d_stc.get('02')

    def get_loop2200d_stc03(self):
        return self.__loop2200d_stc.get('03')

    def get_loop2200d_stc04(self):
        return self.__loop2200d_stc.get('04')

    def get_loop2200d_stc05(self):
        return self.__loop2200d_stc.get('05')

    def get_loop2200d_stc06(self):
        return self.__loop2200d_stc.get('06')

    def get_loop2200d_stc07(self):
        return self.__loop2200d_stc.get('07')

    def get_loop2200d_stc08(self):
        return self.__loop2200d_stc.get('08')

    def get_loop2200d_stc09(self):
        return self.__loop2200d_stc.get('09')

    def get_loop2200d_ref_K101(self):
        return self.__loop2200d_ref_K1.get('01')

    def get_loop2200d_ref_K102(self):
        return self.__loop2200d_ref_K1.get('02')

    def get_loop2200d_ref_EJ01(self):
        return self.__loop2200d_ref_K1.get('01')

    def get_loop2200d_ref_EJ02(self):
        return self.__loop2200d_ref_K1.get('02')

    def get_loop2200d_dtp01(self):
        return self.__loop2200d_dtp.get('01')

    def get_loop2200d_dtp02(self):
        return self.__loop2200d_dtp.get('02')

    def get_loop2200d_dtp03(self):
        return self.__loop2200d_dtp.get('03')

    def get_loop2220d_svc01(self):
        return self.__loop2220d_svc.get('01')

    def get_loop2220d_svc02(self):
        return self.__loop2220d_svc.get('02')

    def get_loop2220d_svc03(self):
        return self.__loop2220d_svc.get('03')

    def get_loop2220d_svc04(self):
        return self.__loop2220d_svc.get('04')

    def get_loop2220d_svc05(self):
        return self.__loop2220d_svc.get('05')

    def get_loop2220d_svc06(self):
        return self.__loop2220d_svc.get('06')

    def get_loop2220d_svc07(self):
        return self.__loop2220d_svc.get('07')

    def get_loop2220d_stc01(self):
        return self.__loop2220d_stc.get('01')

    def get_loop2220d_stc02(self):
        return self.__loop2220d_stc.get('02')

    def get_loop2220d_dtp01(self):
        return self.__loop2220d_dtp.get('01')

    def get_loop2220d_dtp02(self):
        return self.__loop2220d_dtp.get('02')

    def get_loop2220d_dtp03(self):
        return self.__loop2220d_dtp.get('03')
