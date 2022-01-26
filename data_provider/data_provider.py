from data_provider.header_data_provider.isa_data_provider import IsaDataProvider
from data_provider.header_data_provider.gs_data_provider import GsDataProvider

from data_provider.trailer_data_provider.ge_data_provider import GeDataProvider
from data_provider.trailer_data_provider.iea_data_provider import IeaDataProvider


class DataProvider:
    def __init__(self, ack_dict):
        self.__ack_dict = ack_dict
        self.__ack_segment, self.__segment, self.__sub_segment = None, None, None
        self.__build()

    def __build(self):
        for self.__ack_segment in self.__ack_dict:
            self.__segment = self.__ack_segment.split('-')[0]
            if self.__segment == 'ISA':
                self.isa_data_provider = IsaDataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'GS':
                self.gs_data_provider = GsDataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'GE':
                self.ge_data_provider = GeDataProvider(self.__ack_dict.get(self.__ack_segment))

            if self.__segment == 'IEA':
                self.iea_data_provider = IeaDataProvider(self.__ack_dict.get(self.__ack_segment))

    def get_count_body_segments(self):
        print("Count of body segments is ")

    def get_database_name(self):
        return self.__ack_dict.get('database_name')
