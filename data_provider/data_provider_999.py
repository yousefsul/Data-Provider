from data_provider.data_provider import DataProvider
from data_provider.body_data_provider_999.ak2_data_provider import Ak2DataProvider
from data_provider.header_data_provider.ak1_data_provider import Ak1DataProvider
from data_provider.header_data_provider.ta1_data_provider import Ta1DataProvider
from data_provider.header_data_provider.st_data_provider import StDataProvider
from data_provider.trailer_data_provider.ak9_data_provider import Ak9DataProvider


class DataProvider999(DataProvider):
    def __init__(self, ack_dict):
        self.__ack_dict = ack_dict
        self.__count_body_segments = 0
        super().__init__(self.__ack_dict)
        self.__bulid()

    def __bulid(self):
        for self.__ack_segment in self.__ack_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'AK1':
                self.ak1_data_provider = Ak1DataProvider(self.__ack_dict.get(self.__ack_segment))
                self.__bulid_ak9()

            if self.__segment == 'TA1':
                self.ta1_data_provider = Ta1DataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'ST':
                self.st_data_provider = StDataProvider(self.__ack_dict.get(self.__ack_segment))

    def bulid_body_data_provider(self, param):
        for self.__ack_segment in self.__ack_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'AK2' and self.__ack_dict.get(self.__ack_segment).get('02') == param:
                self.ak2_data_provider = Ak2DataProvider(self.__ack_dict.get(self.__ack_segment))

    def __bulid_ak9(self):
        for segment in self.__ack_dict.get(self.__ack_segment):
            self.__sub_segment = segment.split('-')[0]
            if self.__sub_segment == 'AK9':
                self.ak9_data_provider = Ak9DataProvider(self.__ack_dict.get(self.__ack_segment).get(segment))

    def get_count_body_segments(self):
        self.__count_body_segments = 0
        for self.__ack_segment in self.__ack_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'AK2':
                self.__count_body_segments += 1
        return self.__count_body_segments

    def get_ack_file_name(self):
        return self.__ack_dict.get('header_section').get('file_name')

    def get_database_name(self):
        return self.__ack_dict.get('database_name')
