from data_provider.body_data_provider_837 import loop1000A
from data_provider.body_data_provider_837 import loop1000B
from data_provider.body_data_provider_837 import loop2000A
from data_provider.body_data_provider_837 import loop2000B
from data_provider.body_data_provider_837 import loop2300


class StDataProvider:
    def __init__(self, st):
        self.__st = st
        self.__st01 = None
        self.__st02 = None
        self.__st03 = None
        self.__bht01 = None
        self.__bht02 = None
        self.__bht03 = None
        self.__bht04 = None
        self.__bht05 = None
        self.__bht06 = None
        self.__bht = {}
        self.__bulid_bht()
        self.__se = {}
        self.__se01 = None
        self.__se02 = None
        self.__bulid_se()
        self.__st_status = None
        self.__loop1000a_nm1 = loop1000A.get_nm1(self.__st)
        self.__loop1000a_per = loop1000A.get_per(self.__st)
        self.__loop1000b_nm1 = loop1000B.get_nm1(self.__st)
        self.__loop2000a_hl = loop2000A.get_hl(self.__st)
        self.__loop2010aa_nm1 = loop2000A.get_loop2010aa_nm1(self.__st)
        self.__loop2010aa_n3 = loop2000A.get_loop2010aa_n3(self.__st)
        self.__loop2010aa_n4 = loop2000A.get_loop2010aa_n4(self.__st)
        self.__loop2010aa_ref = loop2000A.get_loop2010aa_ref(self.__st)
        self.__loop2010aa_per = loop2000A.get_loop2010aa_per(self.__st)
        self.__loop2000b_hl = loop2000B.get_hl(self.__st)
        self.__loop2000b_sbr = loop2000B.get_sbr(self.__st)
        self.__loop2010ba_nm1 = loop2000B.get_loop2010ba_nm1(self.__st)
        self.__loop2010ba_n3 = loop2000B.get_loop2010ba_n3(self.__st)
        self.__loop2010ba_n4 = loop2000B.get_loop2010ba_n4(self.__st)
        self.__loop2010ba_dmg = loop2000B.get_loop2010ba_dmg(self.__st)
        self.__loop2010bb_nm1 = loop2000B.get_loop2010bb_nm1(self.__st)
        self.__loop2010bb_n3 = loop2000B.get_loop2010bb_n3(self.__st)
        self.__loop2010bb_n4 = loop2000B.get_loop2010bb_n4(self.__st)
        self.__loop2300_clm = loop2300.get_clm(self.__st)
        self.__loop2300_hi = loop2300.get_hi(self.__st)
        self.__loop2310b_nm1 = loop2300.get_loop2310b_nm1(self.__st)
        self.__loop2310b_prv = loop2300.get_loop2310b_prv(self.__st)
        self.__loop2310c_nm1 = loop2300.get_loop2310c_nm1(self.__st)
        self.__loop2310c_n3 = loop2300.get_loop2310c_n3(self.__st)
        self.__loop2400_lx = loop2300.get_loop2400_lx(self.__st)
        self.__loop2400_sv1 = loop2300.get_loop2400_sv1(self.__st)
        self.__loop2400_dtp = loop2300.get_loop2400_dtp(self.__st)
        self.__loop2400_ref = loop2300.get_loop2400_ref(self.__st)

    def get_loop1000a_per01(self):
        return self.__loop1000a_per.get('01')

    def get_loop1000a_per02(self):
        return self.__loop1000a_per.get('02')

    def get_loop1000a_per03(self):
        return self.__loop1000a_per.get('03')

    def get_loop1000a_per04(self):
        return self.__loop1000a_per.get('04')

    def get_loop1000a_nm101(self):
        return self.__loop1000a_nm1.get('01')

    def get_loop1000a_nm102(self):
        return self.__loop1000a_nm1.get('02')

    def get_loop1000a_nm103(self):
        return self.__loop1000a_nm1.get('03')

    def get_loop1000a_nm104(self):
        return self.__loop1000a_nm1.get('04')

    def get_loop1000a_nm105(self):
        return self.__loop1000a_nm1.get('05')

    def get_loop1000a_nm106(self):
        return self.__loop1000a_nm1.get('06')

    def get_loop1000a_nm107(self):
        return self.__loop1000a_nm1.get('07')

    def get_loop1000a_nm108(self):
        return self.__loop1000a_nm1.get('08')

    def get_loop1000a_nm109(self):
        return self.__loop1000a_nm1.get('09')

    def get_st01(self):
        self.__st01 = self.__st.get('01')
        return self.__st01

    def get_st02(self):
        self.__st02 = self.__st.get('02')
        return self.__st02

    def get_st03(self):
        self.__st03 = self.__st.get('03')
        return self.__st03

    def get_st_status(self):
        self.__st_status = self.__st.get('status')
        return self.__st_status

    def __bulid_bht(self):
        for segment in self.__st:
            if segment.split('-')[0] == 'BHT':
                self.__bht = self.__st.get(segment)

    def get_bht01(self):
        self.__bht01 = self.__bht.get('01')
        return self.__bht01

    def get_bht02(self):
        self.__bht02 = self.__bht.get('02')
        return self.__bht02

    def get_bht03(self):
        self.__bht03 = self.__bht.get('03')
        return self.__bht03

    def get_bht04(self):
        self.__bht04 = self.__bht.get('04')
        return self.__bht04

    def get_bht05(self):
        self.__bht05 = self.__bht.get('05')
        return self.__bht05

    def get_bht06(self):
        self.__bht06 = self.__bht.get('01')
        return self.__bht06

    def __bulid_se(self):
        for segment in self.__st:
            if segment.split('-')[0] == 'SE':
                self.__se = self.__st.get(segment)

    def get_se01(self):
        self.__se01 = self.__se.get('01')
        return self.__se01

    def get_se02(self):
        self.__se02 = self.__se.get('02')
        return self.__se02

    def get_loop1000b_nm101(self):
        return self.__loop1000b_nm1.get('01')

    def get_loop1000b_nm102(self):
        return self.__loop1000b_nm1.get('02')

    def get_loop1000b_nm103(self):
        return self.__loop1000b_nm1.get('03')

    def get_loop1000b_nm104(self):
        return self.__loop1000b_nm1.get('04')

    def get_loop1000b_nm105(self):
        return self.__loop1000b_nm1.get('05')

    def get_loop1000b_nm106(self):
        return self.__loop1000b_nm1.get('06')

    def get_loop1000b_nm107(self):
        return self.__loop1000b_nm1.get('07')

    def get_loop1000b_nm108(self):
        return self.__loop1000b_nm1.get('08')

    def get_loop1000b_nm109(self):
        return self.__loop1000b_nm1.get('09')

    def get_loop2000a_hl101(self):
        return self.__loop2000a_hl.get('01')

    def get_loop2000a_hl102(self):
        return self.__loop2000a_hl.get('02')

    def get_loop2000a_hl103(self):
        return self.__loop2000a_hl.get('03')

    def get_loop2000a_hl104(self):
        return self.__loop2000a_hl.get('04')

    def get_loop2010aa_nm101(self):
        return self.__loop2010aa_nm1.get('01')

    def get_loop2010aa_nm102(self):
        return self.__loop2010aa_nm1.get('02')

    def get_loop2010aa_nm103(self):
        return self.__loop2010aa_nm1.get('03')

    def get_loop2010aa_nm104(self):
        return self.__loop2010aa_nm1.get('04')

    def get_loop2010aa_nm105(self):
        return self.__loop2010aa_nm1.get('05')

    def get_loop2010aa_nm106(self):
        return self.__loop2010aa_nm1.get('06')

    def get_loop2010aa_nm107(self):
        return self.__loop2010aa_nm1.get('07')

    def get_loop2010aa_nm108(self):
        return self.__loop2010aa_nm1.get('08')

    def get_loop2010aa_nm109(self):
        return self.__loop2010aa_nm1.get('09')

    def get_loop2010aa_n301(self):
        return self.__loop2010aa_n3.get('01')

    def get_loop2010aa_n401(self):
        return self.__loop2010aa_n4.get('01')

    def get_loop2010aa_n402(self):
        return self.__loop2010aa_n4.get('02')

    def get_loop2010aa_n403(self):
        return self.__loop2010aa_n4.get('03')

    def get_loop2010aa_ref01(self):
        return self.__loop2010aa_ref.get('01')

    def get_loop2010aa_ref02(self):
        return self.__loop2010aa_ref.get('02')

    def get_loop2010aa_per01(self):
        return self.__loop2010aa_per.get('01')

    def get_loop2010aa_per02(self):
        return self.__loop2010aa_per.get('02')

    def get_loop2010aa_per3(self):
        return self.__loop2010aa_per.get('03')

    def get_loop2010aa_per04(self):
        return self.__loop2010aa_per.get('04')

    def get_loop2000b_hl101(self):
        return self.__loop2000b_hl.get('01')

    def get_loop2000b_hl102(self):
        return self.__loop2000b_hl.get('02')

    def get_loop2000b_hl103(self):
        return self.__loop2000b_hl.get('03')

    def get_loop2000b_hl104(self):
        return self.__loop2000b_hl.get('04')

    def get_loop2000b_sbr01(self):
        return self.__loop2000b_sbr.get('01')

    def get_loop2000b_sbr02(self):
        return self.__loop2000b_sbr.get('02')

    def get_loop2000b_sbr03(self):
        return self.__loop2000b_sbr.get('03')

    def get_loop2000b_sbr04(self):
        return self.__loop2000b_sbr.get('04')

    def get_loop2000b_sbr05(self):
        return self.__loop2000b_sbr.get('05')

    def get_loop2000b_sbr06(self):
        return self.__loop2000b_sbr.get('06')

    def get_loop2000b_sbr07(self):
        return self.__loop2000b_sbr.get('07')

    def get_loop2000b_sbr08(self):
        return self.__loop2000b_sbr.get('08')

    def get_loop2000b_sbr09(self):
        return self.__loop2000b_sbr.get('09')

    def get_loop2010ba_nm101(self):
        return self.__loop2010ba_nm1.get('01')

    def get_loop2010ba_nm102(self):
        return self.__loop2010ba_nm1.get('02')

    def get_loop2010ba_nm103(self):
        return self.__loop2010ba_nm1.get('03')

    def get_loop2010ba_nm104(self):
        return self.__loop2010ba_nm1.get('04')

    def get_loop2010ba_nm105(self):
        return self.__loop2010ba_nm1.get('05')

    def get_loop2010ba_nm106(self):
        return self.__loop2010ba_nm1.get('06')

    def get_loop2010ba_nm107(self):
        return self.__loop2010ba_nm1.get('07')

    def get_loop2010ba_nm108(self):
        return self.__loop2010ba_nm1.get('08')

    def get_loop2010ba_nm109(self):
        return self.__loop2010ba_nm1.get('09')

    def get_loop2010ba_n301(self):
        return self.__loop2010ba_n3.get('01')

    def get_loop2010ba_n401(self):
        return self.__loop2010ba_n4.get('01')

    def get_loop2010ba_n402(self):
        return self.__loop2010ba_n4.get('02')

    def get_loop2010ba_n403(self):
        return self.__loop2010ba_n4.get('03')

    def get_loop2010ba_dmg01(self):
        return self.__loop2010ba_dmg.get('01')

    def get_loop2010ba_dmg02(self):
        return self.__loop2010ba_dmg.get('02')

    def get_loop2010ba_dmg03(self):
        return self.__loop2010ba_dmg.get('03')

    def get_loop2010bb_nm101(self):
        return self.__loop2010bb_nm1.get('01')

    def get_loop2010bb_nm102(self):
        return self.__loop2010bb_nm1.get('02')

    def get_loop2010bb_nm103(self):
        return self.__loop2010bb_nm1.get('03')

    def get_loop2010bb_nm104(self):
        return self.__loop2010bb_nm1.get('04')

    def get_loop2010bb_nm105(self):
        return self.__loop2010bb_nm1.get('05')

    def get_loop2010bb_nm106(self):
        return self.__loop2010bb_nm1.get('06')

    def get_loop2010bb_nm107(self):
        return self.__loop2010bb_nm1.get('07')

    def get_loop2010bb_nm108(self):
        return self.__loop2010bb_nm1.get('08')

    def get_loop2010bb_nm109(self):
        return self.__loop2010bb_nm1.get('09')

    def get_loop2010bb_n301(self):
        return self.__loop2010bb_n3.get('01')

    def get_loop2010bb_n401(self):
        return self.__loop2010bb_n4.get('01')

    def get_loop2010bb_n402(self):
        return self.__loop2010bb_n4.get('02')

    def get_loop2010bb_n403(self):
        return self.__loop2010bb_n4.get('03')

    def get_loop2300_clm01(self):
        return self.__loop2300_clm.get('01')

    def get_loop2300_clm02(self):
        return self.__loop2300_clm.get('02')

    def get_loop2300_clm03(self):
        return self.__loop2300_clm.get('03')

    def get_loop2300_clm04(self):
        return self.__loop2300_clm.get('04')

    def get_loop2300_clm05(self):
        return self.__loop2300_clm.get('05')

    def get_loop2300_clm06(self):
        return self.__loop2300_clm.get('06')

    def get_loop2300_clm07(self):
        return self.__loop2300_clm.get('07')

    def get_loop2300_clm08(self):
        return self.__loop2300_clm.get('08')

    def get_loop2300_clm09(self):
        return self.__loop2300_clm.get('09')

    def get_loop2300_clm10(self):
        return self.__loop2300_clm.get('10')

    def get_loop2300_hi01(self):
        return self.__loop2300_hi.get('01')

    def get_loop2300_hi02(self):
        return self.__loop2300_hi.get('12')

    def get_loop2310b_nm101(self):
        return self.__loop2310b_nm1.get('01')

    def get_loop2310b_nm102(self):
        return self.__loop2310b_nm1.get('02')

    def get_loop2310b_nm103(self):
        return self.__loop2310b_nm1.get('03')

    def get_loop2310b_nm104(self):
        return self.__loop2310b_nm1.get('04')

    def get_loop2310b_nm105(self):
        return self.__loop2310b_nm1.get('05')

    def get_loop2310b_nm106(self):
        return self.__loop2310b_nm1.get('06')

    def get_loop2310b_nm107(self):
        return self.__loop2310b_nm1.get('07')

    def get_loop2310b_nm108(self):
        return self.__loop2310b_nm1.get('08')

    def get_loop2310b_nm109(self):
        return self.__loop2310b_nm1.get('09')

    def get_loop2310b_prv01(self):
        return self.__loop2310b_prv.get('01')

    def get_loop2310b_prv02(self):
        return self.__loop2310b_prv.get('02')

    def get_loop2310b_prv03(self):
        return self.__loop2310b_prv.get('03')

    def get_loop2310c_nm101(self):
        return self.__loop2310c_nm1.get('01')

    def get_loop2310c_nm102(self):
        return self.__loop2310c_nm1.get('02')

    def get_loop2310c_nm103(self):
        return self.__loop2310c_nm1.get('03')

    def get_loop2310c_nm104(self):
        return self.__loop2310c_nm1.get('04')

    def get_loop2310c_nm105(self):
        return self.__loop2310c_nm1.get('05')

    def get_loop2310c_nm106(self):
        return self.__loop2310c_nm1.get('06')

    def get_loop2310c_nm107(self):
        return self.__loop2310c_nm1.get('07')

    def get_loop2310c_nm108(self):
        return self.__loop2310c_nm1.get('08')

    def get_loop2310c_nm109(self):
        return self.__loop2310c_nm1.get('09')

    def get_loop2310c_n301(self):
        return self.__loop2010aa_n3.get('01')

    def get_loop2400_lx01(self):
        return self.__loop2400_lx.get('01')

    def get_loop2400_sv101(self):
        return self.__loop2400_sv1.get('01')

    def get_loop2400_sv102(self):
        return self.__loop2400_sv1.get('02')

    def get_loop2400_sv103(self):
        return self.__loop2400_sv1.get('03')

    def get_loop2400_sv104(self):
        return self.__loop2400_sv1.get('04')

    def get_loop2400_sv105(self):
        return self.__loop2400_sv1.get('05')

    def get_loop2400_sv106(self):
        return self.__loop2400_sv1.get('06')

    def get_loop2400_sv107(self):
        return self.__loop2400_sv1.get('07')

    def get_loop2400_dtp01(self):
        return self.__loop2400_dtp.get('01')

    def get_loop2400_dtp02(self):
        return self.__loop2400_dtp.get('02')

    def get_loop2400_dtp03(self):
        return self.__loop2400_dtp.get('03')

    def get_loop2400_ref01(self):
        return self.__loop2400_ref.get('01')

    def get_loop2400_ref02(self):
        return self.__loop2400_ref.get('02')