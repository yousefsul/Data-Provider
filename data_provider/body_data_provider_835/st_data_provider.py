from data_provider.body_data_provider_835 import loop1000A
from data_provider.body_data_provider_837 import loop1000B
from data_provider.body_data_provider_837 import loop2000A
from data_provider.body_data_provider_837 import loop2000B
from data_provider.body_data_provider_837 import loop2300


class StDataProvider:
    def __init__(self, st):
        self.__st = st
        self.__st01 = None
        self.__st02 = None
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
        self.__trn = {}
        self.__build_trn()
        self.__trn01 = None
        self.__trn02 = None
        self.__trn03 = None
        self.__trn04 = None
        self.__cur = {}
        self.__build_cur()
        self.__cur01 = None
        self.__cur02 = None
        self.__cur03 = None
        self.__cur04 = None
        self.__cur05 = None
        self.__cur06 = None
        self.__cur07 = None
        self.__cur08 = None
        self.__cur09 = None
        self.__cur10 = None
        self.__cur11 = None
        self.__cur12 = None
        self.__cur13 = None
        self.__cur14 = None
        self.__cur15 = None
        self.__cur16 = None
        self.__header_ref = {}
        self.__header_ref_list = []
        self.__build_header_ref()
        self.__header_ref01 = None
        self.__header_ref02 = None
        self.__header_ref03 = None
        self.__header_ref04 = None
        #     self.__se = {}
        #     self.__se01 = None
        #     self.__se02 = None
        #     self.__bulid_se()
        #     self.__st_status = None
        self.__loop1000a_n1 = loop1000A.get_n1(self.__st)

    #     self.__loop1000a_per = loop1000A.get_per(self.__st)
    #     self.__loop1000b_nm1 = loop1000B.get_nm1(self.__st)
    #     self.__loop2000a_hl = loop2000A.get_hl(self.__st)
    #     self.__loop2010aa_nm1 = loop2000A.get_loop2010aa_nm1(self.__st)
    #     self.__loop2010aa_n3 = loop2000A.get_loop2010aa_n3(self.__st)
    #     self.__loop2010aa_n4 = loop2000A.get_loop2010aa_n4(self.__st)
    #     self.__loop2010aa_ref = loop2000A.get_loop2010aa_ref(self.__st)
    #     self.__loop2010aa_per = loop2000A.get_loop2010aa_per(self.__st)
    #     self.__loop2000b_hl = loop2000B.get_hl(self.__st)
    #     self.__loop2000b_sbr = loop2000B.get_sbr(self.__st)
    #     self.__loop2010ba_nm1 = loop2000B.get_loop2010ba_nm1(self.__st)
    #     self.__loop2010ba_n3 = loop2000B.get_loop2010ba_n3(self.__st)
    #     self.__loop2010ba_n4 = loop2000B.get_loop2010ba_n4(self.__st)
    #     self.__loop2010ba_dmg = loop2000B.get_loop2010ba_dmg(self.__st)
    #     self.__loop2010bb_nm1 = loop2000B.get_loop2010bb_nm1(self.__st)
    #     self.__loop2010bb_n3 = loop2000B.get_loop2010bb_n3(self.__st)
    #     self.__loop2010bb_n4 = loop2000B.get_loop2010bb_n4(self.__st)
    #     self.__loop2300_clm = loop2300.get_clm(self.__st)
    #     self.__loop2300_hi = loop2300.get_hi(self.__st)
    #     self.__loop2310b_nm1 = loop2300.get_loop2310b_nm1(self.__st)
    #     self.__loop2310b_prv = loop2300.get_loop2310b_prv(self.__st)
    #     self.__loop2310c_nm1 = loop2300.get_loop2310c_nm1(self.__st)
    #     self.__loop2310c_n3 = loop2300.get_loop2310c_n3(self.__st)
    #     self.__loop2400_lx = loop2300.get_loop2400_lx(self.__st)
    #     self.__loop2400_sv1 = loop2300.get_loop2400_sv1(self.__st)
    #     self.__loop2400_dtp = loop2300.get_loop2400_dtp(self.__st)
    #     self.__loop2400_ref = loop2300.get_loop2400_ref(self.__st)
    #
    # def get_loop1000a_per01(self):
    #     return self.__loop1000a_per.get('01')
    #
    # def get_loop1000a_per02(self):
    #     return self.__loop1000a_per.get('02')
    #
    # def get_loop1000a_per03(self):
    #     return self.__loop1000a_per.get('03')
    #
    # def get_loop1000a_per04(self):
    #     return self.__loop1000a_per.get('04')
    #
    def get_loop1000a_n101(self):
        return self.__loop1000a_n1.get('01')

    def get_loop1000a_n102(self):
        return self.__loop1000a_n1.get('02')

    def get_loop1000a_n103(self):
        return self.__loop1000a_n1.get('03')

    def get_loop1000a_n104(self):
        return self.__loop1000a_n1.get('04')

    def get_loop1000a_n105(self):
        return self.__loop1000a_n1.get('05')

    def get_loop1000a_n106(self):
        return self.__loop1000a_n1.get('06')

    #
    # def get_loop1000a_nm107(self):
    #     return self.__loop1000a_nm1.get('07')
    #
    # def get_loop1000a_nm108(self):
    #     return self.__loop1000a_nm1.get('08')
    #
    # def get_loop1000a_nm109(self):
    #     return self.__loop1000a_nm1.get('09')
    #
    def get_st01(self):
        self.__st01 = self.__st.get('01')
        return self.__st01

    def get_st02(self):
        self.__st02 = self.__st.get('02')
        return self.__st02

    def __build_bpr(self):
        for segment in self.__st:
            if segment.split('-')[0] == 'BPR':
                self.__bpr = self.__st.get(segment)

    def get_bpr01(self):
        self.__bpr01 = self.__bpr.get('01')
        return self.__bpr01

    def get_bpr02(self):
        self.__bpr02 = self.__bpr.get('02')
        return self.__bpr02

    def get_bpr03(self):
        self.__bpr03 = self.__bpr.get('03')
        return self.__bpr03

    def get_bpr04(self):
        self.__bpr04 = self.__bpr.get('04')
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
        for segment in self.__st:
            if segment.split('-')[0] == 'TRN':
                self.__trn = self.__st.get(segment)

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

    def __build_cur(self):
        for segment in self.__st:
            if segment.split('-')[0] == 'CUR':
                self.__cur = self.__st.get(segment)

    def get_cur01(self):
        self.__cur01 = self.__cur.get('01')
        return self.__cur01

    def get_cur02(self):
        self.__cur02 = self.__cur.get('02')
        return self.__cur02

    def get_cur03(self):
        self.__cur03 = self.__cur.get('03')
        return self.__cur03

    def get_cur04(self):
        self.__cur04 = self.__cur.get('04')
        return self.__cur04

    def get_cur05(self):
        self.__cur05 = self.__cur.get('05')
        return self.__cur05

    def get_cur06(self):
        self.__cur06 = self.__cur.get('06')
        return self.__cur06

    def get_cur07(self):
        self.__cur07 = self.__cur.get('07')
        return self.__cur07

    def get_cur08(self):
        self.__cur08 = self.__cur.get('08')
        return self.__cur08

    def get_cur09(self):
        self.__cur09 = self.__cur.get('09')
        return self.__cur09

    def get_cur10(self):
        self.__cur10 = self.__cur.get('10')
        return self.__cur10

    def get_cur11(self):
        self.__cur11 = self.__cur.get('11')
        return self.__cur11

    def get_cur12(self):
        self.__cur12 = self.__cur.get('12')
        return self.__cur12

    def get_cur13(self):
        self.__cur13 = self.__cur.get('13')
        return self.__cur13

    def get_cur14(self):
        self.__cur14 = self.__cur.get('14')
        return self.__cur14

    def get_cur15(self):
        self.__cur15 = self.__cur.get('15')
        return self.__cur15

    def get_cur16(self):
        self.__cur16 = self.__cur.get('16')
        return self.__cur16

    def __build_header_ref(self):
        for segment in self.__st:
            if segment.split('-')[0] == 'REF':
                self.__header_ref = self.__st.get(segment)
                self.__header_ref_list.append(self.__header_ref)

    def get_header_ref01(self):
        header_ref_01 = []
        for i in range(len(self.__header_ref_list)):
            self.__cur16 = self.__cur.get('16')
        return header_ref_01
# def __bulid_se(self):
#     for segment in self.__st:
#         if segment.split('-')[0] == 'SE':
#             self.__se = self.__st.get(segment)
#
# def get_se01(self):
#     self.__se01 = self.__se.get('01')
#     return self.__se01
#
# def get_se02(self):
#     self.__se02 = self.__se.get('02')
#     return self.__se02
#
# def get_loop1000b_nm101(self):
#     return self.__loop1000b_nm1.get('01')
#
# def get_loop1000b_nm102(self):
#     return self.__loop1000b_nm1.get('02')
#
# def get_loop1000b_nm103(self):
#     return self.__loop1000b_nm1.get('03')
#
# def get_loop1000b_nm104(self):
#     return self.__loop1000b_nm1.get('04')
#
# def get_loop1000b_nm105(self):
#     return self.__loop1000b_nm1.get('05')
#
# def get_loop1000b_nm106(self):
#     return self.__loop1000b_nm1.get('06')
#
# def get_loop1000b_nm107(self):
#     return self.__loop1000b_nm1.get('07')
#
# def get_loop1000b_nm108(self):
#     return self.__loop1000b_nm1.get('08')
#
# def get_loop1000b_nm109(self):
#     return self.__loop1000b_nm1.get('09')
#
# def get_loop2000a_hl101(self):
#     return self.__loop2000a_hl.get('01')
#
# def get_loop2000a_hl102(self):
#     return self.__loop2000a_hl.get('02')
#
# def get_loop2000a_hl103(self):
#     return self.__loop2000a_hl.get('03')
#
# def get_loop2000a_hl104(self):
#     return self.__loop2000a_hl.get('04')
#
# def get_loop2010aa_nm101(self):
#     return self.__loop2010aa_nm1.get('01')
#
# def get_loop2010aa_nm102(self):
#     return self.__loop2010aa_nm1.get('02')
#
# def get_loop2010aa_nm103(self):
#     return self.__loop2010aa_nm1.get('03')
#
# def get_loop2010aa_nm104(self):
#     return self.__loop2010aa_nm1.get('04')
#
# def get_loop2010aa_nm105(self):
#     return self.__loop2010aa_nm1.get('05')
#
# def get_loop2010aa_nm106(self):
#     return self.__loop2010aa_nm1.get('06')
#
# def get_loop2010aa_nm107(self):
#     return self.__loop2010aa_nm1.get('07')
#
# def get_loop2010aa_nm108(self):
#     return self.__loop2010aa_nm1.get('08')
#
# def get_loop2010aa_nm109(self):
#     return self.__loop2010aa_nm1.get('09')
#
# def get_loop2010aa_n301(self):
#     return self.__loop2010aa_n3.get('01')
#
# def get_loop2010aa_n401(self):
#     return self.__loop2010aa_n4.get('01')
#
# def get_loop2010aa_n402(self):
#     return self.__loop2010aa_n4.get('02')
#
# def get_loop2010aa_n403(self):
#     return self.__loop2010aa_n4.get('03')
#
# def get_loop2010aa_ref01(self):
#     return self.__loop2010aa_ref.get('01')
#
# def get_loop2010aa_ref02(self):
#     return self.__loop2010aa_ref.get('02')
#
# def get_loop2010aa_per01(self):
#     return self.__loop2010aa_per.get('01')
#
# def get_loop2010aa_per02(self):
#     return self.__loop2010aa_per.get('02')
#
# def get_loop2010aa_per3(self):
#     return self.__loop2010aa_per.get('03')
#
# def get_loop2010aa_per04(self):
#     return self.__loop2010aa_per.get('04')
#
# def get_loop2000b_hl101(self):
#     return self.__loop2000b_hl.get('01')
#
# def get_loop2000b_hl102(self):
#     return self.__loop2000b_hl.get('02')
#
# def get_loop2000b_hl103(self):
#     return self.__loop2000b_hl.get('03')
#
# def get_loop2000b_hl104(self):
#     return self.__loop2000b_hl.get('04')
#
# def get_loop2000b_sbr01(self):
#     return self.__loop2000b_sbr.get('01')
#
# def get_loop2000b_sbr02(self):
#     return self.__loop2000b_sbr.get('02')
#
# def get_loop2000b_sbr03(self):
#     return self.__loop2000b_sbr.get('03')
#
# def get_loop2000b_sbr04(self):
#     return self.__loop2000b_sbr.get('04')
#
# def get_loop2000b_sbr05(self):
#     return self.__loop2000b_sbr.get('05')
#
# def get_loop2000b_sbr06(self):
#     return self.__loop2000b_sbr.get('06')
#
# def get_loop2000b_sbr07(self):
#     return self.__loop2000b_sbr.get('07')
#
# def get_loop2000b_sbr08(self):
#     return self.__loop2000b_sbr.get('08')
#
# def get_loop2000b_sbr09(self):
#     return self.__loop2000b_sbr.get('09')
#
# def get_loop2010ba_nm101(self):
#     return self.__loop2010ba_nm1.get('01')
#
# def get_loop2010ba_nm102(self):
#     return self.__loop2010ba_nm1.get('02')
#
# def get_loop2010ba_nm103(self):
#     return self.__loop2010ba_nm1.get('03')
#
# def get_loop2010ba_nm104(self):
#     return self.__loop2010ba_nm1.get('04')
#
# def get_loop2010ba_nm105(self):
#     return self.__loop2010ba_nm1.get('05')
#
# def get_loop2010ba_nm106(self):
#     return self.__loop2010ba_nm1.get('06')
#
# def get_loop2010ba_nm107(self):
#     return self.__loop2010ba_nm1.get('07')
#
# def get_loop2010ba_nm108(self):
#     return self.__loop2010ba_nm1.get('08')
#
# def get_loop2010ba_nm109(self):
#     return self.__loop2010ba_nm1.get('09')
#
# def get_loop2010ba_n301(self):
#     return self.__loop2010ba_n3.get('01')
#
# def get_loop2010ba_n401(self):
#     return self.__loop2010ba_n4.get('01')
#
# def get_loop2010ba_n402(self):
#     return self.__loop2010ba_n4.get('02')
#
# def get_loop2010ba_n403(self):
#     return self.__loop2010ba_n4.get('03')
#
# def get_loop2010ba_dmg01(self):
#     return self.__loop2010ba_dmg.get('01')
#
# def get_loop2010ba_dmg02(self):
#     return self.__loop2010ba_dmg.get('02')
#
# def get_loop2010ba_dmg03(self):
#     return self.__loop2010ba_dmg.get('03')
#
# def get_loop2010bb_nm101(self):
#     return self.__loop2010bb_nm1.get('01')
#
# def get_loop2010bb_nm102(self):
#     return self.__loop2010bb_nm1.get('02')
#
# def get_loop2010bb_nm103(self):
#     return self.__loop2010bb_nm1.get('03')
#
# def get_loop2010bb_nm104(self):
#     return self.__loop2010bb_nm1.get('04')
#
# def get_loop2010bb_nm105(self):
#     return self.__loop2010bb_nm1.get('05')
#
# def get_loop2010bb_nm106(self):
#     return self.__loop2010bb_nm1.get('06')
#
# def get_loop2010bb_nm107(self):
#     return self.__loop2010bb_nm1.get('07')
#
# def get_loop2010bb_nm108(self):
#     return self.__loop2010bb_nm1.get('08')
#
# def get_loop2010bb_nm109(self):
#     return self.__loop2010bb_nm1.get('09')
#
# def get_loop2010bb_n301(self):
#     return self.__loop2010bb_n3.get('01')
#
# def get_loop2010bb_n401(self):
#     return self.__loop2010bb_n4.get('01')
#
# def get_loop2010bb_n402(self):
#     return self.__loop2010bb_n4.get('02')
#
# def get_loop2010bb_n403(self):
#     return self.__loop2010bb_n4.get('03')
#
# def get_loop2300_clm01(self):
#     return self.__loop2300_clm.get('01')
#
# def get_loop2300_clm02(self):
#     return self.__loop2300_clm.get('02')
#
# def get_loop2300_clm03(self):
#     return self.__loop2300_clm.get('03')
#
# def get_loop2300_clm04(self):
#     return self.__loop2300_clm.get('04')
#
# def get_loop2300_clm05(self):
#     return self.__loop2300_clm.get('05')
#
# def get_loop2300_clm06(self):
#     return self.__loop2300_clm.get('06')
#
# def get_loop2300_clm07(self):
#     return self.__loop2300_clm.get('07')
#
# def get_loop2300_clm08(self):
#     return self.__loop2300_clm.get('08')
#
# def get_loop2300_clm09(self):
#     return self.__loop2300_clm.get('09')
#
# def get_loop2300_clm10(self):
#     return self.__loop2300_clm.get('10')
#
# def get_loop2300_hi01(self):
#     return self.__loop2300_hi.get('01')
#
# def get_loop2300_hi02(self):
#     return self.__loop2300_hi.get('12')
#
# def get_loop2310b_nm101(self):
#     return self.__loop2310b_nm1.get('01')
#
# def get_loop2310b_nm102(self):
#     return self.__loop2310b_nm1.get('02')
#
# def get_loop2310b_nm103(self):
#     return self.__loop2310b_nm1.get('03')
#
# def get_loop2310b_nm104(self):
#     return self.__loop2310b_nm1.get('04')
#
# def get_loop2310b_nm105(self):
#     return self.__loop2310b_nm1.get('05')
#
# def get_loop2310b_nm106(self):
#     return self.__loop2310b_nm1.get('06')
#
# def get_loop2310b_nm107(self):
#     return self.__loop2310b_nm1.get('07')
#
# def get_loop2310b_nm108(self):
#     return self.__loop2310b_nm1.get('08')
#
# def get_loop2310b_nm109(self):
#     return self.__loop2310b_nm1.get('09')
#
# def get_loop2310b_prv01(self):
#     return self.__loop2310b_prv.get('01')
#
# def get_loop2310b_prv02(self):
#     return self.__loop2310b_prv.get('02')
#
# def get_loop2310b_prv03(self):
#     return self.__loop2310b_prv.get('03')
#
# def get_loop2310c_nm101(self):
#     return self.__loop2310c_nm1.get('01')
#
# def get_loop2310c_nm102(self):
#     return self.__loop2310c_nm1.get('02')
#
# def get_loop2310c_nm103(self):
#     return self.__loop2310c_nm1.get('03')
#
# def get_loop2310c_nm104(self):
#     return self.__loop2310c_nm1.get('04')
#
# def get_loop2310c_nm105(self):
#     return self.__loop2310c_nm1.get('05')
#
# def get_loop2310c_nm106(self):
#     return self.__loop2310c_nm1.get('06')
#
# def get_loop2310c_nm107(self):
#     return self.__loop2310c_nm1.get('07')
#
# def get_loop2310c_nm108(self):
#     return self.__loop2310c_nm1.get('08')
#
# def get_loop2310c_nm109(self):
#     return self.__loop2310c_nm1.get('09')
#
# def get_loop2310c_n301(self):
#     return self.__loop2010aa_n3.get('01')
#
# def get_loop2400_lx01(self):
#     return self.__loop2400_lx.get('01')
#
# def get_loop2400_sv101(self):
#     return self.__loop2400_sv1.get('01')
#
# def get_loop2400_sv102(self):
#     return self.__loop2400_sv1.get('02')
#
# def get_loop2400_sv103(self):
#     return self.__loop2400_sv1.get('03')
#
# def get_loop2400_sv104(self):
#     return self.__loop2400_sv1.get('04')
#
# def get_loop2400_sv105(self):
#     return self.__loop2400_sv1.get('05')
#
# def get_loop2400_sv106(self):
#     return self.__loop2400_sv1.get('06')
#
# def get_loop2400_sv107(self):
#     return self.__loop2400_sv1.get('07')
#
# def get_loop2400_dtp01(self):
#     return self.__loop2400_dtp.get('01')
#
# def get_loop2400_dtp02(self):
#     return self.__loop2400_dtp.get('02')
#
# def get_loop2400_dtp03(self):
#     return self.__loop2400_dtp.get('03')
#
# def get_loop2400_ref01(self):
#     return self.__loop2400_ref.get('01')
#
# def get_loop2400_ref02(self):
#     return self.__loop2400_ref.get('02')
