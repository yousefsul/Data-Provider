import json

from data_provider.body_data_provider_835.bpr_data_provider import BprDataProvider
from data_provider.data_provider import DataProvider
from data_provider.body_data_provider_835.st_data_provider import StDataProvider
from data_provider.body_data_provider_835.bpr_data_provider_by_id import BprDataProviderById
from data_provider.body_data_provider_835.st_data_provider_by_id import StDataProviderById
from data_provider.body_data_provider_835.claim_data_provider_by_id import ClaimDataProviderById
from application.ConnectMongoDB import ConnectMongoDB

class DataProvider835ById(DataProvider):
    def __init__(self, edi_dict):
        self.__count_clp_segments = None
        self.__payment = None
        self.__edi_dict = edi_dict
        self.__count_body_segments = self.__clp_count = 0
        super().__init__(edi_dict)

    def build_body_data_provider(self, param):
        self.st_data_provider = StDataProviderById(param)

    def build_claim_data_provider(self, param, final_report, param_full_st):
        self.claim_data_provider = ClaimDataProviderById(param, final_report, param_full_st)

    def get_count_body_segments(self):
        self.__count_body_segments = 0
        for self.__ack_segment in self.__edi_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'ST':
                self.__count_body_segments += 1
        return self.__count_body_segments

    def get_edi_file_name(self):
        return self.__edi_dict.get('header_section').get('file_name')

    def payment_data_provider_by_bpr(self, payment):
        self.__payment = payment
        self.bpr_data_provider = BprDataProviderById(self.__payment)

    def get_count_clp_segments(self):
        self.__clp_count = 0
        self.__check_clp_segment()
        return self.__clp_count

    def __check_clp_segment(self):
        for self.__ack_segment in self.__edi_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'ST':
                for segment in self.__edi_dict.get(self.__ack_segment):
                    check_segment = segment.split('-')[0]
                    if check_segment == 'CLP':
                        self.__count_clp_segments += 1
                    if check_segment == '1000A':
                        self.__check_1000a_loop(self.__edi_dict.get(self.__ack_segment).get(segment))
                    if check_segment == '1000B':
                        self.__check_1000b_loop(self.__edi_dict.get(self.__ack_segment).get(segment))
                    if check_segment == '2000':
                        self.__check_2000_loop(self.__edi_dict.get(self.__ack_segment).get(segment))

    def __check_1000a_loop(self, param):
        for segment in param:
            if segment.split('-')[0] == 'CLP':
                self.__count_clp_segments += 1

    def __check_1000b_loop(self, param):
        for segment in param:
            if segment.split('-')[0] == 'CLP':
                self.__count_clp_segments += 1

    def __check_2000_loop(self, param):
        for segment in param:
            if segment == '2100':
                self.__check_2100_loop(param.get(segment))
            if segment.split('-')[0] == 'CLP':
                self.__clp_count += 1

    def __check_2100_loop(self, param):
        for segment in param:
            if segment == '2110':
                self.__check_2110_loop(param.get(segment))
            if segment.split('-')[0] == 'CLP':
                self.__clp_count += 1

    def __check_2110_loop(self, param):
        for segment in param:
            if segment.split('-')[0] == 'CLP':
                self.__clp_count += 1
