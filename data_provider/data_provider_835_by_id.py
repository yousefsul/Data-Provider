import json

from data_provider.body_data_provider_835.bpr_data_provider import BprDataProvider
from data_provider.data_provider import DataProvider
from data_provider.body_data_provider_835.st_data_provider import StDataProvider
from data_provider.body_data_provider_835.bpr_data_provider_by_id import BprDataProviderById
from data_provider.body_data_provider_835.st_data_provider_by_id import StDataProviderById
from data_provider.body_data_provider_835.claim_data_provider_by_id import ClaimDataProviderById


class DataProvider835ById(DataProvider):
    def __init__(self, edi_dict):
        self.__payment = None
        self.__edi_dict = edi_dict
        self.__count_body_segments = 0
        super().__init__(edi_dict)

    def build_body_data_provider(self, param):
        self.st_data_provider = StDataProviderById(param)

    def build_claim_data_provider(self, param,final_report):
        self.claim_data_provider = ClaimDataProviderById(param,final_report)

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
