from data_provider.data_provider import DataProvider
from data_provider.body_data_provider_276.body_data_provider import BodyDataProvider


class DataProvider276(DataProvider):
    def __init__(self, edi_dict):
        self.__edi_dict = edi_dict
        self.__count_body_segments = 0
        super().__init__(edi_dict)

    def bulid_body_data_provider(self, param):
        self.st_data_provider = BodyDataProvider(param)

    def get_count_body_segments(self):
        self.__count_body_segments = 0
        for self.__ack_segment in self.__edi_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'ST':
                self.__count_body_segments += 1
        return self.__count_body_segments

    def get_edi_file_name(self):
        return self.__edi_dict.get('header_section').get('file_name')
