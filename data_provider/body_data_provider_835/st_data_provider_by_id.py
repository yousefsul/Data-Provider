import json

from application.ConnectMongoDB import ConnectMongoDB


class StDataProviderById:
    def __init__(self, st):
        self.__st = st
        self.__segment = None
        self.__loop = None
        self.__data_element_id = None
        self.__sub_loop = False
        self.__data_element_value = None
        self.__connection = ConnectMongoDB('devDB')
        self.__connection.connect_to_collection('Specification835')
        self.__specifications = self.__connection.find_from_collection_by_key("header_section.835_id", 5642377247)

    def get_by_id_repeated_once(self, loop, segment, data_element_id, sub_loop=False):
        self.__loop = loop
        self.__segment = segment
        self.__data_element_id = data_element_id
        self.__sub_loop = sub_loop
        if self.__sub_loop:
            return self.__get_by_sub_loop()
        if self.__loop:
            return self.__get_by_loop()

    def __get_by_loop(self):
        for segment in self.__st.get(self.__loop):
            if segment.split('-')[0] == self.__segment:
                self.__data_element_value = self.__st.get(self.__loop).get(segment).get(self.__data_element_id)
                self.__check_data_element_value()
                return self.__data_element_value

    def __get_by_sub_loop(self):
        for segment in self.__st.get("2000").get(self.__loop):
            if segment.split('-')[0] == self.__segment:
                self.__data_element_value = self.__st.get("2000").get(self.__loop).get(segment).get(self.__data_element_id)
                self.__check_data_element_value()
                return self.__data_element_value

    def __check_data_element_value(self):
        if self.__data_element_value is None or self.__data_element_value == "":
            data_type = self.__specifications.get(self.__data_element_id.split('_')[0]).get("data_type")
            # should be converted to switch when we change to python3.10
            if data_type == "ID" or data_type == "AN":
                self.__data_element_value = "Not provided for this claim"
            elif data_type == "R":
                self.__data_element_value = 0
            else:
                self.__data_element_value = "Not provided for this claim"
