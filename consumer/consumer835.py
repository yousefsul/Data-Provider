import os
from pathlib import Path

import pandas as pd
from application.CommnMethodUsed import CommonMethodUsed
from application.ConnectMongoDB import ConnectMongoDB
from application.GlobalVariables import GlobalVariables
from application.send_email.SendEmail import SendEmail
from bson import Decimal128

from data_provider.data_provider_835_by_id import DataProvider835ById


class Consumer835:
    def __init__(self, credentials_code):
        self.__excel_legend_data_frame = None
        self.__legend_data_frame = {}
        self.__column1 = None
        self.__column = None
        self.__credentials_code = credentials_code
        self.__credential = False
        self.__config_file = None
        self.__number_of_payments = 0
        self.__edi_file = None
        self.__payment = None
        self.__master_payment = None
        self.__segment = self.__sub_segment = None
        self.__st = None
        self.__payments = self.__sub_payments = None
        self.__master_payments = None
        self.__database_name = None
        self.__st = None
        self.__final_report = None
        self.__create_excel_sheet = False
        self.__bpr_id_payment = None
        self.__bpr_id_master_payment = None
        self.__data_provider_edi_file = None
        self.__file_name_excel = None
        self.__line_charge = self.__line_paid_amount = self.__adjustment_amount = \
            self.__patient_responsibility = self.__allowed_amount = Decimal128('0.00')

        self.__line_charge_total = self.__line_paid_amount_total = self.__adjustment_amount_total = \
            self.__patient_responsibility_total = self.__allowed_amount_total = float()
        self.__excel_header = ['Header Number', 'Visit ID', 'Payer Claim Control Number', 'Line Item Control Number',
                               'Service Date', 'POS', 'Procedure Code', 'Units', 'Line Charge', 'Allowed Amount', ]
        self.__excel_header_master = [
            'Visit ID'
            'Service Date',
            'POS',
            'Procedure Code',
            'Units',
            'Total Charge',
            'Allowed Amount',
            'Ins.Adjustment',
            'Insurance Payment',
            'Patient Responsibility']
        self.__visit_header = [
            'Patient Balance',
            'Patient Payment',
            'Visit Balance',
            'Visit Status',
        ]
        self.__payment_header_section = [
            'Check Amount', 'Payment Method', 'Check Date', '# Claims', 'Payee Name Identifier Code',
            'NPI', 'Payer Name Identifier Code', 'Payer Address', 'Payer City', 'Payer State',
            'Payer Zip', 'Payer Contact Phone']
        self.__claim_header_section = [
            'DOS', 'POS', 'Patient ID', 'Patient Last Name', 'Patient First Name',
            'Charged', 'Paid', 'Allowed']
        self.__claim_header_section_visit = ['Visit ID', 'Payer Control Number',
                                             'Claim Received Date', 'Rendering Provider NPI', 'Status Code',
                                             'Frequency Type Code', 'Remark Note']
        self.__svc_header_section = ['DOS', 'CPT', 'MOD', 'Units', 'Charged', 'Allowed', 'Paid',
                                     'Adjustment Amount/ Patient Responsibility']
        self.__svc_header_section_visit = ['Control Number', 'Remark Note']
        self.__svc_allowed_amount = self.__svc_line_paid_amount = self.__svc_line_balance = None
        self.__excel_header_values = []
        self.__is_header_written = self.__is_claim_written = self.__is_svc_written = False
        self.__excel_data_frame = {}
        self.__excel_data_frame_master = {}
        self.__svc_status = self.__visit_id = None
        self.__data_frame  =None
        self.__number_of_claims = 0
        self.__svc_balance_list = []
        self.__svc_balance_summation = 0
        self.__count_row =  self.__tmp_svc_count_row_begin = self.__trn_count_row_begin = 1
        self.__count_row_legend = 0
        self.__workbook, self.__sheet = None, None
        Path("final_reports_files/final_reports").mkdir(parents=True, exist_ok=True)
        Path("final_reports_files/sent").mkdir(parents=True, exist_ok=True)
        self.__claims_rejected = []
        self.__send_email = None
        self.__svc_count = 0
        self.__global_var = GlobalVariables()
        self.__connection_dev = ConnectMongoDB('devDB')
        self.__connection_dev.connect_to_collection('Specification835')
        self.__specification835 = self.__connection_dev.find_from_collection_by_key("header_section.835_id", 5642377247)
        self.__connection = ConnectMongoDB('client_2731928905_DB')
        self.__connection.connect_to_collection('visitsColl')
        self.__common_method = CommonMethodUsed()

    def check_credentials_code(self):
        if self.__credentials_code == "":
            self.__credential = True
            return True
        else:
            return False

    def __fill_final_report(self, edi_file):
        self.__edi_file = edi_file
        if self.__credential:
            self.__data_provider_edi_file = DataProvider835ById(self.__edi_file)
            self.__data_provider_edi_file.build_body_data_provider(self.__st)
            self.__data_provider_edi_file.payment_data_provider_by_bpr(self.__payment)

            # Header section text file
            self.__write_to_final_report_header_section(
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[4: 6] + '/' +
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[6: 8] + '/' +
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[0: 4],
                self.__data_provider_edi_file.st_data_provider.get_by_id_repeated_once('1000A', 'N1', '89_02'),
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('31') + '-' +
                self.__data_provider_edi_file.bpr_data_provider.get_bpr04_description(),
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('30') + '-' +
                self.__data_provider_edi_file.bpr_data_provider.get_bpr03_description(),
                self.__data_provider_edi_file.bpr_data_provider.get_trn_element_by_id('51'),
                self.__data_provider_edi_file.bpr_data_provider.get_trn_element_by_id('50'),
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('29'))
            # Header section text file

            for loop in self.__st:
                if loop.split('-')[0] == "2000":
                    self.__line_charge_total = self.__line_paid_amount_total = self.__adjustment_amount_total = \
                        self.__patient_responsibility_total = self.__allowed_amount_total = float()
                    self.__svc_count = 0
                    self.__data_provider_edi_file.build_claim_data_provider(self.__st.get(loop), self.__final_report,
                                                                            self.__st)
                    self.__number_of_claims += 1
                    self.__write_new_line()
                    self.__write_new_line()
                    self.__is_claim_written = False
                    self.__is_svc_written = False
                    self.__trn_count_row_begin = self.__count_row
                    self.__final_report.write(f"Claim# {self.__number_of_claims}:")

                    self.__excel_data_frame.update(
                        {"Check Amount":
                             self.__append_currency_to_amount(self.__common_method.convert_float_string(
                                 self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('29')))
                         })
                    self.__excel_data_frame.update(
                        {"Payment Method":
                             self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('31')})

                    self.__excel_data_frame.update(
                        {"Check Date":
                             self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[4: 6] + '/' +
                             self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[6: 8] + '/' +
                             self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[0: 4],
                         })

                    self.__excel_data_frame.update(
                        {"# Claims":
                             self.__data_provider_edi_file.claim_data_provider.get_count_clp()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000B', 'N1', '134',
                                                                                            is_by_code=False, code='PE'
                                                                                            ,
                                                                                            request_other_data_element_id_in_segment='135')
                    self.__excel_data_frame.update(
                        {"Payee Name Identifier Code":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000B', 'N1', '137')

                    self.__excel_data_frame.update(
                        {"NPI":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000A', 'N1', '88',
                                                                                            is_by_code=False, code='PR'
                                                                                            ,
                                                                                            request_other_data_element_id_in_segment='89')

                    self.__excel_data_frame.update(
                        {"Payer Name Identifier Code":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000A', 'N3', '94')

                    self.__excel_data_frame.update(
                        {"Payer Address":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000A', 'N4', '96')

                    self.__excel_data_frame.update(
                        {"Payer City":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000A', 'N4', '97')

                    self.__excel_data_frame.update(
                        {"Payer State":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000A', 'N4', '98')

                    self.__excel_data_frame.update(
                        {"Payer Zip":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'PER', '378',
                                                                                            is_by_code=True, code='CX')
                    phone_number = ""
                    if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                        self.__check_rules('2100', 'PER', '378')
                    else:
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'PER', '378',
                                                                                                is_by_code=False,
                                                                                                code='CX',
                                                                                                request_other_data_element_id_in_segment='381')
                    phone_number += self.__data_provider_edi_file.claim_data_provider.get_data_element_value()

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'PER', '378',
                                                                                            is_by_code=False,
                                                                                            code='CX',
                                                                                            request_other_data_element_id_in_segment='381')

                    self.__excel_data_frame.update({
                        'Payer Contact Phone': self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})
                    self.__setup_excel_sheet()
                    self.__write_to_excel_header_section()
                    self.__write_payment()
                    self.__write_payment_header_section()
                    self.__excel_data_frame = {}
                    self.__count_row += 1
                    self.__write_claim_header_section()

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'DTM', '361')

                    self.__excel_data_frame.update(
                        {"DOS":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'TS3', '160')

                    if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                        self.__check_rules('2000', 'TS3', '160')
                    self.__excel_data_frame.update(
                        {"POS":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '243',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Patient ID":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '237',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Patient Last Name":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '238',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Patient First Name":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '204',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Charged":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '205',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Paid":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'AMT', '443',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Allowed": self.__data_provider_edi_file.claim_data_provider.get_data_element_value()}
                    )

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '202',
                                                                                            is_set_specific_data_element=True)
                    self.__excel_data_frame.update(
                        {"Visit ID":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__visit_id = self.__data_provider_edi_file.claim_data_provider.get_data_element_value()

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '208',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Payer Control Number":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'DTM', '373',
                                                                                            is_set_specific_data_element=True)

                    self.__excel_data_frame.update(
                        {"Claim Received Date":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '278',
                                                                                            is_by_code=False, code='XX'
                                                                                            ,
                                                                                            request_other_data_element_id_in_segment='279')

                    self.__excel_data_frame.update(
                        {"Rendering Provider NPI":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '203')

                    self.__legend_data_frame.update({
                        "Claim Status Code":
                            self.__data_provider_edi_file.claim_data_provider.get_data_element_value() + '-' +
                            self.__data_provider_edi_file.claim_data_provider.get_code_description()
                    })

                    self.__excel_data_frame.update(
                        {"Status Code":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '210',
                                                                                            is_set_specific_data_element=True)

                    if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                        self.__check_rules('2100', 'CLP', '210')

                    self.__excel_data_frame.update(
                        {"Frequency Type Code":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '210',
                                                                                            is_set_specific_data_element=True)

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'MOA', '343')
                    if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                        self.__check_rules('2100', 'MOA', '343')

                    self.__excel_data_frame.update(
                        {"Remark Note":
                             self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})
                    self.__setup_excel_sheet()
                    self.__write_claim()

                    self.__count_row += 1
                    self.__tmp_svc_count_row_begin = self.__count_row

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'LX', '158')

                    self.__write_new_line_and_tap()

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'LX', '158')

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', None)

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '235',
                                                                                            is_by_code=True, code='QC')
                    self.__write_new_line()
                    self.__write_new_tap()

                    self.__write_svc_header_section()
                    self.__count_row += 1

                    while self.__data_provider_edi_file.claim_data_provider.get_number_of_svc() > 0:
                        self.__excel_data_frame = {}
                        self.__svc_count += 1
                        self.__final_report.write(f"Service line# {self.__svc_count}:")
                        self.__write_new_line_and_tap()
                        svc = str(self.__svc_count)

                        # self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'LX', '158',
                        #                                                                         is_set_specific_data_element=True)  # Header Number
                        # self.__append_to_excel_sheet_data_frame()
                        #
                        # self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '202',
                        #                                                                         is_set_specific_data_element=True)  # Visit Id
                        # self.__visit_id = self.__data_provider_edi_file.claim_data_provider.get_data_element_value()
                        #
                        #     self.__append_to_excel_sheet_data_frame()
                        #     self.__excel_data_frame_master.update(
                        #         {self.__data_provider_edi_file.claim_data_provider.get_data_element_label():
                        #              self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})
                        #
                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '208',
                        #                                                                             is_set_specific_data_element=True)  # Payer Claim Control Number
                        #     self.__append_to_excel_sheet_data_frame()
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '431',
                        #                                                                             is_set_specific_data_element=True,
                        #                                                                             is_svc=True)  # Line Item Control Number
                        #     self.__append_to_excel_sheet_data_frame()
                        #     self.__data_provider_edi_file.claim_data_provider.append_svc_line_id(svc)
                        #     self.__svc_id = self.__data_provider_edi_file.claim_data_provider.get_svc_id(svc)
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'DTM', '402',
                                                                                                is_set_specific_data_element=True)  # Service Date

                        if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                            self.__check_rules('2110', 'DTM', '402')

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_label('DOS')
                        self.__append_to_excel_sheet_data_frame()

                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '209',
                        #                                                                             is_set_specific_data_element=True)  # POS
                        #     if self.__data_provider_edi_file.claim_data_provider.get_data_element_label() is None:
                        #         self.__data_provider_edi_file.claim_data_provider.set_data_element_label('POS')
                        #     self.__append_to_excel_sheet_data_frame()
                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '394',
                                                                                                is_sub=True,
                                                                                                is_svc=True)

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_value_label(
                            'CPT',
                            self.__data_provider_edi_file.claim_data_provider.get_from_svc(svc, 'Procedure Code'))

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_value_label(
                            'MOD',
                            self.__data_provider_edi_file.claim_data_provider.get_from_svc(svc, 'MOD'))
                        self.__append_to_excel_sheet_data_frame()

                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '398',
                                                                                                is_set_specific_data_element=True,
                                                                                                is_svc=True)

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_label('Number of Units')
                        if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                            self.__check_rules('2110', 'SVC', '398')

                        self.__append_to_excel_sheet_data_frame()

                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '395',
                                                                                                is_svc=True)  # Line charge

                        self.__line_charge_total += self.__common_method.convert_string_float_num(
                            self.__data_provider_edi_file.claim_data_provider.get_data_element_value())

                        self.__append_to_excel_sheet_data_frame()

                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'AMT', '443',
                                                                                                is_svc=True)  # Allowed amount

                        if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                            self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                'Allowed Amount:0.00')
                        self.__allowed_amount_total += self.__common_method.convert_string_float_num(
                            self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == '0.00':
                            self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                'Allowed Amount:$0.00')
                        self.__append_to_excel_sheet_data_frame()

                        #     self.__append_to_excel_sheet_data_frame_master(
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                        #         self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'DTM', '402',
                        #                                                                             is_svc=True)
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'CAS', None,
                        #                                                                             is_write_one_line=True,
                        #                                                                             is_svc=True)
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'CAS', '409',
                        #                                                                             is_set_specific_data_element=True,
                        #                                                                             is_svc=True)
                        #     self.__append_to_excel_sheet_data_frame()
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'CLP', '205',
                        #                                                                             is_set_specific_data_element=True)
                        #     self.__append_to_excel_sheet_data_frame()
                        #
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '430',
                        #                                                                             is_svc=True)
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '431',
                        #                                                                             is_svc=True)
                        #     self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'AMT', '443',
                        #                                                                             is_svc=True)
                        #     self.__svc_allowed_amount = self.__data_provider_edi_file.claim_data_provider.get_data_element_value()
                        #
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '396',
                                                                                                is_svc=True)

                        self.__svc_line_paid_amount = self.__data_provider_edi_file.claim_data_provider.get_data_element_value()
                        self.__line_paid_amount_total += self.__common_method.convert_string_float_num(
                            self.__svc_line_paid_amount)

                        self.__append_to_excel_sheet_data_frame()

                        self.__merge_and_write()
                        self.__write_deductible(svc)
                        self.__write_coins(svc)
                        self.__write_copay(svc)
                        self.__write_co_oa_pi_amount(svc)
                        self.__write_co_oa_pi(svc)
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '431',
                                                                                                is_svc=True)
                        self.__write_control_number()
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'LQ', '449')
                        if self.__data_provider_edi_file.claim_data_provider.get_data_element_value() == 'NP':
                            self.__check_rules('2110', 'LQ', '449')

                        self.__write_svc_remark()
                        self.__setup_excel_sheet()

                        # self.__write_to_excel_sheet()
                        # self.__write_to_excel_header_section()
                        #     self.__write_in_specific_position(19)
                        #     self.__write_in_specific_position(37)
                        #     self.__calc_write_svc_line_balance(38)
                        #     self.__write_svc_line_status(39)
                        #     self.__write_amounts(svc)
                        #     # self.__check_patient_payment_service_line_visit(self.__visit_id, self.__svc_id)
                        self.__data_provider_edi_file.claim_data_provider.decrement_number_of_svc()
                    self.__write_svc()
                    self.__write_check_number(
                        self.__data_provider_edi_file.bpr_data_provider.get_trn_element_by_id('50'))
                    self.__write_totals()
                    self.__excel_header_values.clear()
                    self.__final_report.write('-' * 100)
                    self.__write_new_line()

            self.__setup_legend_excel_sheet()
                    # self.__calc_write_claim_balance(41)

    def __write_to_final_report_header_section(self, check_date, payer_name, payment_method, flag_code,
                                               originating_company, check_number, check_amount):
        self.__write_new_line()
        self.__final_report.write(f"Payer Type: Insurance")
        self.__write_new_line()
        self.__final_report.write(f"Payer Name: {payer_name}")
        self.__write_new_line()
        self.__final_report.write(f"Payment Method: {payment_method}")
        self.__write_new_line()
        self.__final_report.write(f"Credit or Debit Flag Code: {flag_code}")
        self.__write_new_line()
        self.__final_report.write(f"Originating Company: {originating_company}")
        self.__write_new_line()
        self.__final_report.write(f"Check Number: {check_number}")
        self.__write_new_line()
        self.__final_report.write(f"Check Date: {check_date}")
        self.__write_new_line()
        self.__final_report.write(f"Check Amount: ${check_amount}")

    def __write_header_section(self):
        self.__final_report.write(f"FINAL REPORT\n\n".center(100))
        self.__final_report.write(f"\n835 File Name: {self.__master_payment.get('header_section').get('file_name')}")
        self.__final_report.write(f"\nThis file has {self.__number_of_payments} payment(s)\n")
        self.__final_report.write('-' * 100 + "\n\n")

    def __create_file_name_and_open(self):
        self.__file_name = self.__database_name + '_' + \
                           self.__master_payment.get('header_section').get('file_name') + \
                           '.txt'
        self.__file_name_excel = self.__database_name + '_' + \
                                 self.__master_payment.get('header_section').get('file_name') + \
                                 '.xlsx'

        self.__final_report = open(f"final_reports_files/final_reports/{self.__file_name}", 'w')
        self.__writer = pd.ExcelWriter(f"final_reports_files/final_reports/{self.__file_name_excel}",
                                       engine='xlsxwriter')

    def process_payment(self, master_payment, sub_payments, db_name):
        self.__sub_payments = sub_payments
        self.__database_name = db_name
        self.__master_payment = master_payment
        for self.__segment in self.__master_payment:
            if self.__segment.split('-')[0] == 'ST':
                self.__sub_payments.rewind()
                for self.__sub_segment in self.__master_payment.get(self.__segment):
                    if self.__sub_segment.split('-')[0] == 'BPR':
                        self.__bpr_id_master_payment = self.__master_payment.get(self.__segment).get(
                            self.__sub_segment).get('bpr_id')

                        if self.__bpr_id_master_payment != 1236078867:  # remove when complete test
                            return
                        self.__st = self.__master_payment.get(self.__segment)
                        self.__payment = self.__get_sub_payment()
                        self.__create_file_name_and_open()  # should move below self__master_payments
                        self.__write_header_section()
                        self.__fill_final_report(self.__master_payment)
                        self.__final_report.close()
                        self.__writer.save()
                        # self.__files = []
                        # self.__files.append(os.path.abspath(self.__final_report.name))
                        # self.__files.append(os.path.abspath(self.__writer))
                        # self.__send_email = SendEmail(self.__global_var.get_text(), self.__global_var.get_html())
                        # self.__send_email.send_email_multi_attachment(self.__files)

    def __get_sub_payment(self):
        for payment in self.__sub_payments:
            if payment.get('header_section').get('bpr_id') == self.__bpr_id_master_payment:
                self.__number_of_payments += 1
                return payment

    def __write_new_line(self):
        self.__final_report.write('\n')

    def __write_new_line_and_tap(self):
        self.__final_report.write('\n\t')

    def __write_new_tap(self):
        self.__final_report.write('\t')

    def __setup_legend_excel_sheet(self):
        self.__count_row_legend += 1
        self.__excel_legend_data_frame = pd.DataFrame(self.__legend_data_frame, index=[0], dtype=None)
        self.__excel_legend_data_frame.to_excel(self.__writer, sheet_name='Legend-Table', index=False,startrow=self.__count_row_legend, startcol=1, header=True)



    def __setup_excel_sheet(self):
        self.__count_row += 1
        self.__data_frame = pd.DataFrame(self.__excel_data_frame, index=[0], dtype=None)
        self.__data_frame_2 = pd.DataFrame(self.__excel_data_frame_master, index=[0], dtype=None)

        self.__data_frame.to_excel(self.__writer, sheet_name='Tabular', index=False,
                                   startrow=self.__count_row, startcol=2, header=False)


        # self.__data_frame_2.to_excel(self.__writer, sheet_name='info_from_835', index=False,
        #                              startrow=self.__count_row, startcol=22, header=False)

        self.__workbook = self.__writer.book
        self.__worksheet = self.__workbook.get_worksheet_by_name('Tabular')
        self.__general_format = self.__workbook.add_format({'border': 2, 'valign': 'center',
                                                            'bold': True, 'font_size': 14})
        self.__header_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'valign': 'center',
            'fg_color': '#D7E4BC'
        })
        self.__payment_header_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'valign': 'center',
            # 'valign': 'top',
            'fg_color': '#B1A0C7',
            'text_wrap': True
        })
        self.__total_row_format = self.__workbook.add_format({'bold': True, 'font_color': 'red'})
        self.__wrap_format = self.__workbook.add_format({'text_wrap': True})

        self.__currency_format = self.__workbook.add_format(
            {'bold': True, 'font_color': 'red', 'num_format': '$#,##0.00'})
        # Create a format to use in the merged range.
        self.__merge_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#D7E4BC',
            'text_wrap': True
        })
        self.__payment_header_section_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#DDD9C4',
            'text_wrap': True
        })
        self.__claim_header_section_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#BF9A78',
            'text_wrap': True
        })

        self.__claim_header_section_format_visit = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#7C8EA0',
            'text_wrap': True
        })

        self.__svc_header_section_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#F2E8B3',
            'text_wrap': True
        })

        self.__rotation_format_payment = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#DDD9C4',
            'text_wrap': True
        })
        self.__rotation_format_claim = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#BF9A78',
            'text_wrap': True
        })
        self.__rotation_format_svc = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'align': 'center',
            'fg_color': '#F2E8B3',
            'text_wrap': True
        })
        self.__rotation_format_payment.set_rotation(90)
        self.__rotation_format_payment.set_align('center')
        self.__rotation_format_payment.set_align('vcenter')
        self.__rotation_format_claim.set_rotation(90)
        self.__rotation_format_claim.set_align('center')
        self.__rotation_format_claim.set_align('vcenter')
        self.__rotation_format_svc.set_rotation(90)
        self.__rotation_format_svc.set_align('center')
        self.__rotation_format_svc.set_align('vcenter')
        self.__my_format = self.__workbook.add_format({'num_format': '0.00'})
        self.__cell_format = self.__workbook.add_format()
        self.__cell_format.set_align('center')
        self.__cell_format.set_align('vcenter')
        self.__worksheet.set_default_row(35)
        self.__worksheet.set_column('A:AV', 25, self.__cell_format)

    def __append_to_excel_sheet_data_frame(self):
        self.__excel_data_frame.update({self.__data_provider_edi_file.claim_data_provider.get_data_element_label():
                                            self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

    def __write_to_excel_sheet(self):
        self.__setup_excel_sheet()
        if not self.__is_claim_written:
            self.__count_row_visit = self.__count_row
            self.__worksheet.write(self.__count_row_visit, 0, f'Claim Number {self.__number_of_claims}',
                                   self.__total_row_format)
            self.__is_claim_written = True
        self.__worksheet.write(self.__count_row, 0, f'Service Line {self.__svc_count}', self.__total_row_format)
        self.__set_column_width()

    def __write_to_excel_header_section(self):
        if not self.__is_header_written:
            self.__worksheet.merge_range(first_row=0, first_col=0, last_row=0, last_col=16,
                                         data='Info of 835 EDI File',
                                         cell_format=self.__general_format)

            # self.__worksheet.merge_range(first_row=0, first_col=22, last_row=0, last_col=39,
            #                              data='Intended visit in our system that represents the respective claim',
            #                              cell_format=self.__general_format)
            #
            # self.__worksheet.merge_range(first_row=0, first_col=22, last_row=0, last_col=39,
            #                              data='Intended visit in our system that represents the respective claim',
            #                              cell_format=self.__general_format)
            #
            # self.__worksheet.merge_range(first_row=1, first_col=11, last_row=1, last_col=12,
            #                              data='Adjustment Amount\n Contractual Obligations',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=13, last_row=1, last_col=14,
            #                              data='Adjustment Amount\n Patient Responsibility',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=15, last_row=1, last_col=16,
            #                              data='Adjustment Amount\n Other Adjustment',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=17, last_row=1, last_col=18,
            #                              data='Adjustment Amount\n Payor Initiated Reductions',
            #                              cell_format=self.__header_format)
            # self.__worksheet.write(2, 11, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 12, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 13, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 14, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 15, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 16, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 17, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 18, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(1, 19, 'Service Line\n Paid Amount', self.__header_format)
            # self.__worksheet.write(1, 37, 'Service Line\n Paid Amount', self.__header_format)
            # self.__worksheet.write(1, 38, 'Service Line Balance', self.__header_format)
            # self.__worksheet.write(1, 39, 'Service Line Status', self.__header_format)
            #
            # self.__worksheet.merge_range(first_row=1, first_col=29, last_row=1, last_col=30,
            #                              data='Adjustment Amount\n Contractual Obligations',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=31, last_row=1, last_col=32,
            #                              data='Adjustment Amount\n Patient Responsibility',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=33, last_row=1, last_col=34,
            #                              data='Adjustment Amount\n Other Adjustment',
            #                              cell_format=self.__header_format)
            # self.__worksheet.merge_range(first_row=1, first_col=35, last_row=1, last_col=36,
            #                              data='Adjustment Amount\n Payor Initiated Reductions',
            #                              cell_format=self.__header_format)
            # self.__worksheet.write(2, 29, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 30, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 31, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 32, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 33, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 34, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write(2, 35, 'Reason Code', self.__header_format)
            # self.__worksheet.write(2, 36, 'Adjustment Amount', self.__header_format)
            # self.__worksheet.write_row(1, 1, tuple(self.__excel_header), self.__header_format)
            # self.__worksheet.write_row(1, 22, tuple(self.__excel_data_frame_master), self.__header_format)
            # self.__worksheet.write_row(1, 41, tuple(self.__visit_header), self.__payment_header_format)
            self.__is_header_written = True

    def __append_to_excel_sheet_data_frame_master(self, key, value):
        self.__excel_data_frame_master.update({key: value})

    # def __close_claim(self):
    #     self.__connection.update_status_for_visits_collection(int(self.__excel_data_frame.get('Visit ID')))
    #     self.__connection.update_visit_current_status(int(self.__excel_data_frame.get('Visit ID')))

    def __set_column_width(self):
        for self.__column in self.__data_frame:
            if self.__column is None:
                continue
            self.__column_width = 30
            self.__col_idx = self.__data_frame.columns.get_loc(self.__column)
            self.__writer.sheets['info_from_835'].set_column(self.__col_idx + 1,
                                                             self.__col_idx + 1,
                                                             self.__column_width)
        for self.__column1 in self.__data_frame_2:
            if self.__column1 is None:
                continue
            self.__column_width = 30
            self.__col_idx = self.__data_frame_2.columns.get_loc(self.__column1)
            self.__writer.sheets['info_from_835'].set_column(self.__col_idx + 1,
                                                             self.__col_idx + 1,
                                                             self.__column_width)

    def __check_rules(self, loop, segment, data_element):
        match loop:
            case '2000':
                match segment:
                    case 'TS3':
                        match data_element:
                            case '160':
                                self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP',
                                                                                                        '209',
                                                                                                        is_set_specific_data_element=True)  # POS
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_label('POS')
                                self.__append_to_excel_sheet_data_frame()
                                # self.__append_to_excel_sheet_data_frame_master(
                                #     self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                                #     self.__data_provider_edi_file.claim_data_provider.get_data_element_value())

            case '2100':
                match segment:
                    case 'CLP':
                        match data_element:
                            case '210':
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                    'Frequency Type Code:1')

                    case 'PER':
                        match data_element:
                            case '378':
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                    'Payer Contact Phone:NP')

                    case 'MOA':
                        match data_element:
                            case '343':
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                    'Remark Note: NP')

            case '2110':
                match segment:
                    case 'DTM':
                        match data_element:
                            case '402':
                                self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'DTM',
                                                                                                        '361',
                                                                                                        is_set_specific_data_element=True)  # Service Date
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_label('DOS')
                                self.__append_to_excel_sheet_data_frame()
                                self.__append_to_excel_sheet_data_frame_master(
                                    self.__data_provider_edi_file.claim_data_provider.get_data_element_label(),
                                    self.__data_provider_edi_file.claim_data_provider.get_data_element_value())
                    case 'SVC':
                        match data_element:
                            case '398':
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                    'Number of Units:1')

                    case 'LQ':
                        match data_element:
                            case '449':
                                self.__data_provider_edi_file.claim_data_provider.set_data_element_value(
                                    'Remark Note:NP')

            # case '1000B':
            #     match segment:
            #         case 'N1':
            #             match data_element:
            #                 case '134':
            #                     self.__data_provider_edi_file.claim_data_provider.write_to_final_report('1000B', 'N1', '135',
            #                                                                                             is_by_code=False,
            #                                                                                             code='PE')

            # Add rules to master template
            # data element
            # DTM 442

    def __write_amounts(self, svc):
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_co_list(svc):
            for key, value in item.items():
                self.__worksheet.write(self.__count_row, 11, str(key))
                self.__worksheet.write(self.__count_row, 29, str(key))
                value = format(float(str(value)), '.2f')
                self.__worksheet.write(self.__count_row, 12, str('$') + str(value), self.__currency_format)
                self.__worksheet.write(self.__count_row, 30, str('$') + str(value), self.__currency_format)
            self.__count_row += 1

        self.__count_row = count_row_tmp
        for item in self.__data_provider_edi_file.claim_data_provider.get_pr_list(svc):
            for key, value in item.items():
                self.__worksheet.write(self.__count_row, 13, str(key))
                self.__worksheet.write(self.__count_row, 31, str(key))
                value = format(float(str(value)), '.2f')
                self.__worksheet.write(self.__count_row, 14, str('$') + str(value), self.__currency_format)
                self.__worksheet.write(self.__count_row, 32, str('$') + str(value), self.__currency_format)
            self.__count_row += 1

    def __write_in_specific_position(self, col):
        self.__worksheet.write(self.__count_row, col,
                               self.__data_provider_edi_file.claim_data_provider.get_data_element_value()
                               , self.__currency_format)

    def __calc_write_svc_line_balance(self, col):
        self.__svc_line_balance = self.__common_method.convert_string_float_num(
            self.__svc_allowed_amount) - self.__common_method.convert_string_float_num(self.__svc_line_paid_amount)
        self.__worksheet.write(self.__count_row, col,
                               self.__svc_line_balance
                               , self.__currency_format)
        self.__svc_balance_list.append(self.__svc_line_balance)

    def __write_svc_line_status(self, col):
        if self.__common_method.convert_string_float_num(self.__svc_line_balance) > 0:
            self.__svc_status = self.__global_var.get_service_line_status_pr()
        else:
            self.__svc_status = self.__global_var.get_service_line_status_closed()

        self.__worksheet.write(self.__count_row, col, self.__svc_status)

    def __calc_write_claim_balance(self, col):
        self.__svc_balance_summation = sum(self.__svc_balance_list)
        self.__worksheet.write(self.__count_row_visit, col, self.__svc_balance_summation, self.__currency_format)

    # def __check_patient_payment_service_line_visit(self, visit_id, svc_id):
    #     self.__connection.connect_to_collection('visitsColl')
    #     visit = self.__connection.find_from_collection_by_key('header_section.visit_id', int(visit_id))
    #     service_lines = visit.get('service_line')
    #     for service_line in service_lines:
    #         if str(service_line.get('line_number_control')) == str(svc_id):
    #             self.__calc_visit_balance(service_line.get('payment').get('patient'))
    #             return self.__check_patient_payment_patient_payment(service_line.get('payment').get('patient')
    #                                                                 , self.__svc_balance_summation)
    #
    #     return self.__common_method.convert_string_float_num(0)
    #
    # def __check_patient_payment_patient_payment(self, patient_payment, patient_balance):
    #     if self.__common_method.convert_string_float_num(patient_balance) == 0:
    #         return self.__common_method.convert_string_float_num(patient_payment)
    #     else:
    #         if self.__common_method.convert_string_float_num(patient_balance) > 0:
    #             return self.__common_method.convert_string_float_num(
    #                 patient_balance) if self.__common_method.convert_string_float_num(
    #                 patient_balance) != self.__common_method.convert_string_float_num(
    #                 patient_payment) else self.__common_method.convert_string_float_num(patient_payment)
    #
    # def __calc_visit_balance(self, patient_payment):
    #     self.__visit_balance = self.__svc_balance_summation - patient_payment
    #
    #     if self.__common_method.convert_string_float_num(self.__svc_balance_summation) == 0 \
    #             and self.__common_method.convert_string_float_num(patient_payment) == 0:
    #         self.__visit_balance = 0
    #
    #     if self.__common_method.convert_string_float_num(self.__svc_balance_summation) > 0:
    #         self.__visit_balance = self.__common_method.convert_string_float_num(self.__svc_balance_summation)

    def __write_totals(self):
        self.__count_row += 1
        self.__total_col = self.__data_frame.columns.get_loc('Line Paid Amount')
        self.__worksheet.write(self.__count_row, 0, 'Totals', self.__currency_format)
        self.__worksheet.write(self.__count_row, self.__total_col, self.__line_charge_total, self.__currency_format)
        self.__total_col += 1
        self.__worksheet.write(self.__count_row, self.__total_col, self.__allowed_amount_total, self.__currency_format)
        self.__total_col += 1
        self.__worksheet.write(self.__count_row, self.__total_col,
                               self.__line_paid_amount_total
                               , self.__currency_format)
        self.__total_col += 1
        self.__worksheet.write_row(self.__count_row, self.__total_col,
                                   tuple(self.__data_provider_edi_file.claim_data_provider.get_patient_totals()),
                                   self.__currency_format)
        self.__total_col += 4
        self.__worksheet.write(self.__count_row, self.__total_col,
                               self.__data_provider_edi_file.claim_data_provider.get_insurance_responsibility_total()
                               , self.__currency_format)
        self.__count_row += 1

    def __write_payment_header_section(self):
        self.__worksheet.write_row(self.__count_row - 1, 2, tuple(self.__payment_header_section),
                                   self.__payment_header_section_format)

    def __write_claim_header_section(self):
        self.__worksheet.write_row(self.__count_row, 2, tuple(self.__claim_header_section),
                                   self.__claim_header_section_format)
        self.__worksheet.write_row(self.__count_row, 10, tuple(self.__claim_header_section_visit),
                                   self.__claim_header_section_format_visit)

    def __write_svc_header_section(self):
        self.__worksheet.write_row(self.__count_row, 2, tuple(self.__svc_header_section),
                                   self.__svc_header_section_format)

    def __append_currency_to_amount(self, amount_to_append):
        return self.__global_var.get_currency() + str(amount_to_append)

    def __write_payment(self):
        first_row = 'A' + str(self.__count_row)
        next_row = 'A' + str(self.__count_row + 1)
        self.__worksheet.merge_range(f'{first_row}:{next_row}', 'Payment', self.__rotation_format_payment)

    def __write_claim(self):
        first_row = 'A' + str(self.__count_row)
        next_row = 'A' + str(self.__count_row + 1)
        self.__worksheet.merge_range(f'{first_row}:{next_row}', 'Claim', self.__rotation_format_claim)

    def __write_svc(self):
        first_row = 'A' + str(self.__tmp_svc_count_row_begin + 1)
        next_row = 'A' + str(self.__count_row + 1)
        self.__worksheet.merge_range(f'{first_row}:{next_row}', 'Service line/s', self.__rotation_format_svc)

    def __merge_and_write(self):
        if not self.__is_svc_written:
            self.__start_col_merge = 9
            self.__worksheet.merge_range(first_row=self.__count_row - 1,
                                         first_col=self.__start_col_merge,
                                         last_row=self.__count_row - 1,
                                         last_col=self.__start_col_merge + 3,
                                         data='Adjustment Amount/ Patient Responsibility',
                                         cell_format=self.__svc_header_section_format)
            self.__worksheet.write(self.__count_row, self.__start_col_merge, 'Deductible',
                                   self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row, self.__start_col_merge, 'Coins', self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row, self.__start_col_merge, 'Copay', self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row, self.__start_col_merge, 'Other', self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row - 1, self.__start_col_merge, 'Adjustment Amount',
                                   self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row - 1, self.__start_col_merge, 'Adjustment Code',
                                   self.__svc_header_section_format)
            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row - 1, self.__start_col_merge, 'Control Number',
                                   self.__claim_header_section_format_visit)

            self.__start_col_merge += 1
            self.__worksheet.write(self.__count_row - 1, self.__start_col_merge, 'Remark Note',
                                   self.__claim_header_section_format_visit)
            self.__is_svc_written = True

    def __write_deductible(self, svc):
        amount = ""
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_pr_deductible_list(svc):
            for key, value in item.items():
                value = self.__append_currency_to_amount(self.__common_method.convert_float_string(value))
                amount += '\n' + value
        self.__worksheet.write(self.__count_row + 1, 9, amount, self.__wrap_format)
        self.__count_row = count_row_tmp

    def __write_coins(self, svc):
        amount = ""
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_pr_coins_list(svc):
            for key, value in item.items():
                value = self.__append_currency_to_amount(self.__common_method.convert_string_float_num(value))
                amount += '\n' + value
        self.__worksheet.write(self.__count_row + 1, 10, amount, self.__wrap_format)
        self.__count_row = count_row_tmp

    def __write_copay(self, svc):
        amount = ""
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_pr_copay_list(svc):
            for key, value in item.items():
                value = self.__append_currency_to_amount(self.__common_method.convert_float_string(value))
                # value = self.__append_currency_to_amount(self.__common_method.convert_string_float_num(value))
                amount += '\n' + value
        self.__worksheet.write(self.__count_row + 1, 11, amount, self.__wrap_format)
        self.__count_row = count_row_tmp

    def __write_other(self, svc):
        amount = ""
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_pr_other_list(svc):
            for key, value in item.items():
                value = self.__append_currency_to_amount(self.__common_method.convert_float_string(value))
                amount += '\n' + value
        self.__worksheet.write(self.__count_row + 1, 12, amount, self.__wrap_format)
        self.__count_row = count_row_tmp

    def __write_co_oa_pi_amount(self, svc):
        amount = ""
        wrap_format = self.__workbook.add_format({'text_wrap': True})
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_co_list(svc):
            for key, value in item.items():
                value = self.__append_currency_to_amount(self.__common_method.convert_float_string(value))
                amount += '\n' + value
        self.__worksheet.write(self.__count_row + 1, 13, amount, wrap_format)
        self.__count_row = count_row_tmp

    def __write_co_oa_pi(self, svc):
        code_description = ""
        wrap_format = self.__workbook.add_format({'text_wrap': True})
        count_row_tmp = self.__count_row
        for item in self.__data_provider_edi_file.claim_data_provider.get_co_oa_pi_list(svc):
            for key, value in item.items():
                code_description += '\n' + key + '-' + value
        self.__worksheet.write(self.__count_row + 1, 14, code_description, wrap_format)
        self.__count_row = count_row_tmp

    def __write_control_number(self):
        self.__worksheet.write(self.__count_row + 1, 15,
                               self.__data_provider_edi_file.claim_data_provider.get_data_element_value())

    def __write_svc_remark(self):
        self.__worksheet.write(self.__count_row + 1, 16,
                               self.__data_provider_edi_file.claim_data_provider.get_data_element_value())

    def __write_check_number(self, check_number):
        first_row = 'B' + str(self.__trn_count_row_begin + 1)
        next_row = 'B' + str(self.__count_row + 1)
        self.__worksheet.merge_range(f'{first_row}:{next_row}', 'Check # /EFT \n' + check_number,
                                     self.__rotation_format_claim)
