from application.ConnectMongoDB import ConnectMongoDB
from bson import Decimal128

DEFAULT_CODE = "999-"


class ClaimDataProviderById:
    def __init__(self, claim, file):
        self.__claim = claim
        self.__file = file
        self.__final_report = file
        self.__parsed_claim = {}
        self.__id = None
        self.__is_code_description, self.__is_sub = False, False
        self.__data_element_value = None
        self.__data_element = None
        self.__segment = None
        self.__loop = None
        self.__request_code = None
        self.__code_description = None
        self.__description = None
        self.__is_by_code = False
        self.__patient_responsibility = 0
        self.__request_loop, self.__request_segment, self.__request_data_element_id = None, None, None
        self.__extract_2000_loop()
        self.__extract_2100_loop()

        self.__connection = ConnectMongoDB('devDB')
        self.__connection.connect_to_collection('Specification835')
        self.__specifications = self.__connection.find_from_collection_by_key("header_section.835_id", 5642377247)
        self.__connection.connect_to_collection('referenceTables')
        self.__reference_tables = self.__connection.find_from_collection()

    def __extract_2000_loop(self):
        for self.__segment in self.__claim:
            if self.__segment.split('-')[0] != '2100':
                self.__parsed_claim["2000"] = {}
                self.__parsed_claim["2000"][self.__segment] = {}
                for self.__data_element in self.__claim.get(self.__segment):
                    self.__parsed_claim["2000"][self.__segment][self.__get_new_key()] = \
                        self.__claim.get(self.__segment).get(self.__data_element)

    def __extract_2100_loop(self):
        for self.__loop in self.__claim:
            if self.__loop == '2100':
                self.__parsed_claim[self.__loop] = {}
                for self.__segment in self.__claim.get(self.__loop):
                    if self.__segment == "2110":
                        self.__extract_2110_loop(self.__claim.get(self.__loop).get(self.__segment))
                    self.__parsed_claim[self.__loop][self.__segment] = {}
                    for self.__data_element in self.__claim.get(self.__loop).get(self.__segment):
                        self.__parsed_claim[self.__loop][self.__segment][self.__get_new_key()] = \
                            self.__claim.get(self.__loop).get(self.__segment).get(self.__data_element)

    def __extract_2110_loop(self, param):
        self.__parsed_claim[self.__segment] = {}
        for segment in param:
            self.__parsed_claim[self.__segment][segment] = {}
            for self.__data_element in param[segment]:
                self.__parsed_claim[self.__segment][segment][self.__get_new_key()] = \
                    param[segment][self.__data_element]

    def write_by_specific_code(self, request_loop, request_segment, request_data_element_id, description,
                               is_description=False, is_sub=False):
        self.__request_loop = request_loop
        self.__request_segment = request_segment
        self.__request_data_element_id = request_data_element_id
        self.__description = description
        self.__is_code_description = is_description
        if is_sub:
            self.__handle_sub_data_element()
            return

        for self.__segment in self.__parsed_claim.get(self.__request_loop):
            if self.__segment.split('-')[0] == self.__request_segment:
                self.__data_element_value = self.__parsed_claim.get(self.__request_loop).get(self.__segment).get(
                    self.__request_data_element_id)

    def write_all_segments(self, request_loop, request_segment, request_data_element_id, description, request_code="",
                           is_description=False, is_sub=False, is_by_code=False):
        self.__request_code = request_code
        self.__is_by_code = is_by_code
        self.__request_loop = request_loop
        self.__request_segment = request_segment
        self.__request_data_element_id = request_data_element_id
        self.__description = description
        self.__is_code_description = is_description
        if is_by_code:
            self.__write_by_code()
            return
        if is_sub:
            self.__handle_sub_data_element()
            return
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        self.__data_element_value = \
                            self.__parsed_claim.get(self.__loop).get(self.__segment).get(self.__request_data_element_id)
                        # self.__write_description(self.__description)
                        self.__check_data_element_value()
                        # if self.__is_code_description:
                        #     self.__write_code_description()
                        return self.__data_element_value
                        self.__write_to_final_report()

    def get_by_id(self, data_element_id):
        self.__id = data_element_id
        self.__data_element_value = self.__parsed_claim.get(self.__id)
        self.__check_data_element_value()
        return self.__data_element_value

    def __get_new_key(self):
        return self.__data_element.split('_')[0]

    def __check_data_element_value(self):
        if self.__data_element_value is None or self.__data_element_value == "":
            data_type = self.__specifications.get(self.__request_data_element_id).get("data_type")
            # should be converted to switch when we change to python3.10
            if data_type == "ID" or data_type == "AN" or data_type == "DT":
                self.__data_element_value = DEFAULT_CODE + "Not provided for this claim"
            elif data_type == "R":
                self.__data_element_value = DEFAULT_CODE + '$' + str(Decimal128(str("0.00")))
            else:
                self.__data_element_value = DEFAULT_CODE + "Not provided for this claim"
        else:
            data_type = self.__specifications.get(self.__request_data_element_id).get("data_type")
            if data_type == 'DT':
                self.__data_element_value = self.__data_element_value[4: 6] + '/' + \
                                            self.__data_element_value[6: 8] + '/' + \
                                            self.__data_element_value[0: 4]
            if data_type == 'R':
                self.__data_element_value = '$' + str(Decimal128(self.__data_element_value).to_decimal())

    def __write_to_final_report(self):
        self.__final_report.write(self.__data_element_value)
        if self.__is_code_description:
            self.__final_report.write(' - ' + str(self.__code_description))
        self.__write_new_line_and_tap()

    def __write_new_line(self):
        self.__final_report.write('\n')

    def __write_new_line_and_tap(self):
        self.__final_report.write('\n\t')

    # def __write_description(self, description):
    #     self.__final_report.write(description)

    def __write_code_description(self):
        self.__reference_tables.rewind()
        for ref in self.__reference_tables:
            if ref.get(self.__request_loop):
                if ref.get(self.__request_loop).get(self.__request_segment):
                    if ref.get(self.__request_loop).get(self.__request_segment).get(self.__request_data_element_id):
                        self.__code_description = ref.get(self.__request_loop).get(self.__request_segment). \
                            get(self.__request_data_element_id).get(self.__data_element_value)
                        if self.__code_description is None:
                            self.__code_description = ""

    def __handle_sub_data_element(self):
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        self.__data_element_value = \
                            self.__parsed_claim.get(self.__loop).get(self.__segment).get(self.__request_data_element_id)
                        self.__sub_data_element = self.__data_element_value.split(':')
                        self.__data_element_value = self.__sub_data_element[0]
                        self.__write_description("Product or Service ID Qualifier ")
                        if self.__is_code_description:
                            self.__write_code_description()
                        self.__write_to_final_report()
                        self.__is_code_description = False
                        self.__data_element_value = self.__sub_data_element[1]
                        self.__write_description("Procedure Code ")
                        self.__write_to_final_report()
                        self.__data_element_value = self.__sub_data_element[2]
                        self.__write_description("Procedure Modifier ")
                        self.__write_to_final_report()

    def __write_by_code(self):
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment == self.__request_segment:
                        if self.__parsed_claim.get(self.__loop).get(self.__segment). \
                                get(self.__request_data_element_id) == self.__request_code:
                            pass
        # for self.__loop in self.__parsed_claim:
        #     if self.__loop == self.__request_loop:
        #         for self.__segment in self.__parsed_claim.get(self.__loop):
        #             if self.__segment.split('-')[0] == self.__request_segment:
        #                 self.__data_element_value = \
        #                     self.__parsed_claim.get(self.__loop).get(self.__segment).get(self.__request_data_element_id)
        #                 self.__write_description(self.__description)
        #                 self.__check_data_element_value()
        #                 if self.__is_code_description:
        #                     self.__write_code_description()
        #                 self.__write_to_final_report()
