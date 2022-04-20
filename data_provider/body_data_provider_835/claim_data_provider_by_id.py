from application.CommnMethodUsed import CommonMethodUsed
from application.ConnectMongoDB import ConnectMongoDB
from bson import Decimal128

DEFAULT_CODE = "999-"


class ClaimDataProviderById:
    def __init__(self, claim, file):
        self.__claim = claim
        self.__file = file
        self.__final_report = file
        self.__parsed_claim = {}
        self.__number_of_svc = 0
        self.__svc = {}
        self.__id = None
        self.__is_code_description = self.__is_sub = self.__is_write_to_one_line = False
        self.__data_element_value = None
        self.__data_element = None
        self.__data_element_id = None
        self.__segment, self.__case_segment = None, 'CAS'
        self.__loop = None
        self.__request_code = None
        self.__code_description = None
        self.__description = None
        self.__is_by_code, self.__code = False, ''
        self.__data_element_label = None
        self.__data_element_id_description = None
        self.__request_data_element_id_sub = None
        self.__data_element_id_list = None
        self.__is_set_specific_data_element = self.__is_svc = False
        self.__data_element_to_exclude = []
        # self.__total_patient_responsibility, self.__total_insurance_responsibility = float

        self.__total_patient_responsibility = self.__total_insurance_responsibility = Decimal128(
            "{:.2f}".format(float(0.00)))
        self.__patient_responsibility_svc = self.__insurance_responsibility_svc = Decimal128(
            "{:.2f}".format(float(0.00)))
        self.__request_loop, self.__request_segment, self.__request_data_element_id = None, None, None
        self.__extract_2000_loop()
        self.__extract_2100_loop()
        self.__common_method = CommonMethodUsed()
        self.__calc_amounts_per_svc()
        self.__connection = ConnectMongoDB('devDB')
        self.__connection.connect_to_collection('Specification835')
        self.__specifications = self.__connection.find_from_collection_by_key("header_section.835_id", 5642377247)
        self.__connection.connect_to_collection('referenceTables')
        self.__reference_tables = self.__connection.find_from_collection()

    def __extract_2000_loop(self):
        self.__parsed_claim["2000"] = {}
        for self.__segment in self.__claim:
            if self.__segment.split('-')[0] != '2100':
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
        cas_segment = False
        self.__parsed_claim[self.__segment] = {}
        for segment in param:
            if segment.split('-')[0] == 'CAS':
                cas_segment = True
            self.__parsed_claim[self.__segment][segment] = {}
            for self.__data_element in param[segment]:
                if cas_segment:
                    self.__calc_amounts(param[segment], param[segment][self.__data_element])
                self.__parsed_claim[self.__segment][segment][self.__get_new_key()] = param[segment][self.__data_element]
        self.__build_svc_dict(self.__parsed_claim[self.__segment])

    def __write_specific_data_element(self):
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        for self.__data_element_id in self.__parsed_claim.get(self.__loop).get(self.__segment):
                            if self.__data_element_id == self.__request_data_element_id:
                                self.__data_element_value = self.__parsed_claim.get(self.__loop).get(
                                    self.__segment).get(self.__data_element_id)
                                self.__check_data_element_value()
                                self.__master_write_to_final_report()
                                return

    def write_all_data_elements(self):
        tmp_one_line_description = ""
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        for self.__data_element_id in self.__parsed_claim.get(self.__loop).get(self.__segment):
                            self.__request_data_element_id = self.__data_element_id
                            self.__data_element_value = self.__parsed_claim.get(self.__loop).get(self.__segment).get(
                                self.__data_element_id)
                            self.__check_data_element_value()
                            if self.__is_write_to_one_line:
                                tmp_one_line_description += self.__data_element_value
                            else:
                                self.__master_write_to_final_report()
                        if self.__is_write_to_one_line:
                            self.__data_element_value = tmp_one_line_description
                            self.__master_write_to_final_report()

    def write_all_data_elements_svc(self):
        request_data_element_id_sub_count = 1
        if not self.__request_data_element_id:
            for self.__loop in self.__svc:
                if self.__loop == self.__request_loop:
                    for self.__segment in self.__svc.get(self.__loop):
                        tmp_one_line_description = ""
                        if self.__segment.split('-')[0] == self.__request_segment:
                            for self.__data_element_id in self.__svc.get(self.__loop).get(self.__segment):
                                self.__request_data_element_id = self.__data_element_id
                                self.__data_element_value = self.__svc.get(self.__loop).get(
                                    self.__segment).get(
                                    self.__data_element_id)
                                self.__check_data_element_value()
                                if self.__is_write_to_one_line:
                                    tmp_one_line_description += self.__data_element_value + " "
                                else:
                                    self.__master_write_to_final_report()
                            if self.__is_write_to_one_line:
                                self.__data_element_value = tmp_one_line_description
                                self.__master_write_to_final_report()
        else:
            for self.__loop in self.__svc:
                if self.__loop == self.__request_loop:
                    for self.__segment in self.__svc.get(self.__loop):
                        if self.__segment.split('-')[0] == self.__request_segment:
                            for self.__data_element_id in self.__svc.get(self.__loop).get(self.__segment):
                                if self.__data_element_id == self.__request_data_element_id:
                                    self.__data_element_value = self.__svc.get(self.__loop).get(
                                        self.__segment).get(self.__data_element_id)
                                    if ":" in self.__data_element_value:
                                        self.__data_element_id_list = self.__data_element_value.split(':')
                                        for data_element in self.__data_element_id_list:
                                            self.__request_data_element_id_sub = self.__request_data_element_id + '-' + \
                                                                                 str(request_data_element_id_sub_count)
                                            self.__svc[self.__loop]['Procedure Code'] = self.__data_element_id_list[1]
                                            self.__data_element_value = data_element
                                            self.__check_data_element_value()
                                            self.__master_write_to_final_report()
                                            request_data_element_id_sub_count += 1
                                    else:
                                        self.__check_data_element_value()
                                        self.__master_write_to_final_report()
                                    return

    def write_all_data_elements_by_specific_code(self):
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        if self.__parsed_claim.get(self.__loop).get(self.__segment).get(
                                self.__request_data_element_id) == self.__code:
                            for self.__data_element_id in self.__parsed_claim.get(self.__loop).get(self.__segment):
                                self.__request_data_element_id = self.__data_element_id

                                self.__data_element_value = self.__parsed_claim.get(self.__loop).get(
                                    self.__segment).get(self.__data_element_id)
                                self.__check_data_element_value()
                                self.__master_write_to_final_report()

    def write_sub_data_elements(self):
        request_data_element_id_sub_count = 1
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        for self.__data_element_id in self.__parsed_claim.get(self.__loop).get(self.__segment):
                            if self.__data_element_id == self.__request_data_element_id:
                                self.__data_element_value = self.__parsed_claim.get(self.__loop).get(
                                    self.__segment).get(self.__data_element_id)
                                if ":" in self.__data_element_value:
                                    self.__data_element_id_list = self.__data_element_value.split(':')
                                    for data_element in self.__data_element_id_list:
                                        self.__request_data_element_id_sub = self.__request_data_element_id + '-' + \
                                                                             str(request_data_element_id_sub_count)
                                        self.__data_element_value = data_element
                                        self.__check_data_element_value()
                                        self.__master_write_to_final_report()
                                        request_data_element_id_sub_count += 1
                                return

    def write_to_excel_sheet(self):
        pass

    def write_to_final_report(self, request_loop, request_segment, request_data_element_id, is_by_code=False, code='',
                              is_sub=False, is_write_one_line=False, is_set_specific_data_element=False,
                              is_svc=False):
        self.__data_element_value = None
        self.__data_element_label = None
        self.__request_loop = request_loop
        self.__request_segment = request_segment
        self.__request_data_element_id = request_data_element_id
        self.__is_by_code = is_by_code
        self.__is_svc = is_svc
        self.__code = code
        self.__is_sub = is_sub
        self.__is_write_to_one_line = is_write_one_line
        self.__is_set_specific_data_element = is_set_specific_data_element

        # should be changed when we change to python 3.10

        if self.__is_set_specific_data_element and self.__is_svc:
            self.set_specific_data_element_svc()
            return

        if self.__is_set_specific_data_element:
            self.set_specific_data_element()
            return

        if self.__is_svc:
            self.write_all_data_elements_svc()
            return

        if self.__is_sub:
            self.write_sub_data_elements()
            return

        if self.__is_by_code and self.__code is not None:
            self.write_all_data_elements_by_specific_code()
            return

        if self.__request_data_element_id:
            self.__write_specific_data_element()
        else:
            self.write_all_data_elements()

    def __get_new_key(self):
        return self.__data_element.split('_')[0]

    def __check_data_element_value(self):
        if self.__is_sub:
            self.__check_data_element_sub_value()
            return
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
                self.__data_element_value = '$' + str(Decimal128("{:.2f}".format(float(self.__data_element_value))))

        self.__data_element_label = self.__specifications.get(self.__request_data_element_id).get("medvertex_label")
        self.__data_element_id_description = self.__get_code_description()
        if not self.__is_write_to_one_line:
            self.__data_element_value = self.__data_element_label + ': ' + self.__data_element_value
        else:
            self.__data_element_value = self.__data_element_value
        if self.__data_element_id_description:
            self.__data_element_value += self.__data_element_id_description

    def __check_data_element_sub_value(self):
        if self.__data_element_value is None or self.__data_element_value == "":
            data_type = self.__specifications.get(self.__request_data_element_id).get(
                self.__request_data_element_id_sub).get("data_type")
            # should be converted to switch when we change to python3.10
            if data_type == "ID" or data_type == "AN" or data_type == "DT":
                self.__data_element_value = DEFAULT_CODE + "Not provided for this claim"
            elif data_type == "R":
                self.__data_element_value = DEFAULT_CODE + '$' + str(Decimal128(str("0.00")))
            else:
                self.__data_element_value = DEFAULT_CODE + "Not provided for this claim"
        else:
            data_type = self.__specifications.get(self.__request_data_element_id).get(
                self.__request_data_element_id_sub).get("data_type")
            if data_type == 'DT':
                self.__data_element_value = self.__data_element_value[4: 6] + '/' + \
                                            self.__data_element_value[6: 8] + '/' + \
                                            self.__data_element_value[0: 4]
            if data_type == 'R':
                self.__data_element_value = '$' + str(Decimal128("{:.2f}".format(float(self.__data_element_value))))

        self.__data_element_label = self.__specifications.get(self.__request_data_element_id).get(
            self.__request_data_element_id_sub).get("medvertex_label")
        self.__data_element_id_description = self.__get_code_description_sub()
        self.__data_element_value = self.__data_element_label + ': ' + self.__data_element_value
        if self.__data_element_id_description:
            self.__data_element_value += self.__data_element_id_description

    def __master_write_to_final_report(self):
        self.__final_report.write(self.__data_element_value)
        self.__write_new_line_and_tap()

    def __write_new_line(self):
        self.__final_report.write('\n')

    def __write_new_line_and_tap(self):
        self.__final_report.write('\n\t')

    def __get_code_description(self):
        if self.__specifications.get(self.__request_data_element_id).get('need_description') == 'Y':
            implementation_name = self.__specifications.get(self.__request_data_element_id).get('data_element_name')
            self.__reference_tables.rewind()
            for ref in self.__reference_tables:
                ref.pop('_id')
                if implementation_name in ref.keys():
                    return '-' + ref.get(implementation_name).get(self.__data_element_value)

    def __get_code_description_sub(self):
        if self.__specifications.get(self.__request_data_element_id).get(
                self.__request_data_element_id_sub).get('need_description') == 'Y':
            implementation_name = self.__specifications.get(self.__request_data_element_id).get(
                self.__request_data_element_id_sub).get('data_element_name')
            self.__reference_tables.rewind()
            for ref in self.__reference_tables:
                ref.pop('_id')
                if implementation_name in ref.keys():
                    return '-' + str(ref.get(implementation_name).get(self.__data_element_value))

    def get_patient_responsibility(self):
        return self.__total_patient_responsibility

    def insurance_responsibility(self):
        return self.__total_insurance_responsibility

    def __calc_amounts(self, param, code):
        try:
            split_data_element = self.__data_element.split('_')
            tmp_id = int(split_data_element[0]) + 2
            tmp_data_element = int(split_data_element[1]) + 2
            tmp_data_element = format(tmp_data_element, '02d')
            final_result_data_element = str(tmp_id) + '_' + str(tmp_data_element)
            if code == 'PR':
                self.__total_patient_responsibility = self.__total_patient_responsibility.to_decimal() + \
                                                      Decimal128(param[final_result_data_element]).to_decimal()
            else:
                self.__total_insurance_responsibility = self.__total_insurance_responsibility.to_decimal() + \
                                                        Decimal128(param[final_result_data_element]).to_decimal()
        except Exception as E:
            pass

    def get_data_element_value(self):
        if self.__data_element_value is None:
            return '999'

        if ":" in self.__data_element_value:
            return self.__data_element_value.split(':', 1)[1].strip()
        else:
            return '$' + self.__data_element_value.split('$')[1]

    def get_data_element_label(self):
        return self.__data_element_label

    def set_data_element_value(self, data_element_value):
        self.__data_element_value = data_element_value

    def set_data_element_label(self, data_element_label):
        self.__data_element_label = data_element_label

    def set_data_element_value_label(self, data_element_label, data_element_value):
        self.__data_element_value = str(data_element_label) + ': ' + str(data_element_value)
        self.__data_element_label = str(data_element_label)

    def set_specific_data_element_svc(self):
        for self.__loop in self.__svc:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__svc.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        for self.__data_element_id in self.__svc.get(self.__loop).get(self.__segment):
                            if self.__data_element_id == self.__request_data_element_id:
                                self.__data_element_value = self.__svc.get(self.__loop).get(
                                    self.__segment).get(self.__data_element_id)
                                self.__check_data_element_value()
                                return

    def set_specific_data_element(self):
        for self.__loop in self.__parsed_claim:
            if self.__loop == self.__request_loop:
                for self.__segment in self.__parsed_claim.get(self.__loop):
                    if self.__segment.split('-')[0] == self.__request_segment:
                        for self.__data_element_id in self.__parsed_claim.get(self.__loop).get(self.__segment):
                            if self.__data_element_id == self.__request_data_element_id:
                                self.__data_element_value = self.__parsed_claim.get(self.__loop).get(
                                    self.__segment).get(self.__data_element_id)
                                self.__check_data_element_value()
                                return

    def __build_svc_dict(self, param):
        for segment in param:
            if segment.split('-')[0] == 'SVC':
                self.__number_of_svc += 1
                self.__svc[str(self.__number_of_svc)] = {}
                self.__svc[str(self.__number_of_svc)][segment] = param[segment]
                continue
            else:
                self.__svc[str(self.__number_of_svc)][segment] = param[segment]

    def __calc_amounts_per_svc(self):
        self.__pr_dict = {}
        self.__co_dict = {}
        self.__reason_codes = {}
        self.__patient_responsibility_total = self.__insurance_responsibility_total = \
            self.__common_method.convert_string_float_num('0')
        for svc in self.__svc:
            count = 1
            self.__pr_dict[str(svc)] = []
            self.__co_dict[str(svc)] = []
            self.__patient_responsibility_svc = self.__insurance_responsibility_svc = \
                self.__common_method.convert_string_float_num('0')
            for segment in self.__svc.get(svc):
                if segment.split('-')[0] == self.__case_segment:
                    for data_element in self.__svc.get(svc).get(segment):
                        match self.__svc.get(svc).get(segment).get(data_element):
                            case 'PR':
                                tmp_data_element = int(data_element) + 2
                                code_data_element = int(data_element) + 1
                                self.__patient_responsibility_svc = self.__svc.get(svc).get(segment).get(
                                    str(tmp_data_element))
                                self.__patient_responsibility_total += self.__common_method.convert_string_float_num(
                                    self.__patient_responsibility_svc)
                                self.__pr_dict[svc].append({self.__svc.get(svc).get(segment).get(
                                    str(code_data_element)): self.__svc.get(svc).get(segment).get(
                                    str(tmp_data_element))})
                                self.__reason_codes.update(
                                    {self.__svc.get(svc).get(segment).get(str(code_data_element)): tmp_data_element})
                                count += 1

                            case 'CO':
                                tmp_data_element = int(data_element) + 2
                                code_data_element = int(data_element) + 1
                                self.__insurance_responsibility_svc = self.__svc.get(svc).get(segment).get(
                                    str(tmp_data_element))
                                self.__insurance_responsibility_total += self.__common_method.convert_string_float_num(
                                    self.__insurance_responsibility_svc)
                                self.__co_dict[svc].append({self.__svc.get(svc).get(segment).get(
                                    str(code_data_element)): self.__svc.get(svc).get(segment).get(
                                    str(tmp_data_element))})
                                self.__reason_codes.update(
                                    {self.__svc.get(svc).get(segment).get(str(code_data_element)): tmp_data_element})
                                count += 1

    def get_patient_responsibility_svc(self):
        return self.__patient_responsibility_svc

    def get_insurance_responsibility_svc(self):
        return self.__insurance_responsibility_svc

    def get_number_of_svc(self):
        return self.__number_of_svc

    def decrement_number_of_svc(self):
        self.__number_of_svc -= 1

    def get_from_svc(self, svc, key):
        return self.__svc.get(svc).get(key)

    def get_pr_list(self, svc):
        return self.__pr_dict.get(svc)

    def get_co_list(self, svc):
        return self.__co_dict.get(svc)

    def get_reason_codes(self):
        return self.__reason_codes

    def append_svc_line_id(self, svc):
        self.__svc.get(svc)['id'] = self.get_data_element_value().split('L')[0]

    def get_svc_id(self, svc):
        return self.__svc.get(svc)['id']

    def get_patient_responsibility_total(self):
        return round(self.__patient_responsibility_total, 2)

    def get_insurance_responsibility_total(self):
        return round(self.__insurance_responsibility_total, 2)
