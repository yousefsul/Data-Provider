from data_provider.data_provider import DataProvider
from data_provider.header_data_provider.bht_data_provider import BhtDataProvider
from data_provider.trailer_data_provider.se_data_provider import SeDataProvider
from data_provider.header_data_provider.st_data_provider import StDataProvider
from data_provider.body_data_provider_277ca.body_data_provider import BodyDataProvider


class DataProvider277CA(DataProvider):
    def __init__(self, ack_dict):
        self.__ack_dict = ack_dict
        self.__count_body_segments = 0
        super().__init__(self.__ack_dict)
        self.__bulid()

    def __bulid(self):
        for self.__ack_segment in self.__ack_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'ST':
                self.st_data_provider = StDataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'BHT':
                self.bht_data_provider = BhtDataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'SE':
                self.se_data_provider = SeDataProvider(self.__ack_dict.get(self.__ack_segment))

    def bulid_body_data_provider(self):
        self.body_data_provider = BodyDataProvider(self.__ack_dict)


