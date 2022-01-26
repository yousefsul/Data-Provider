import datetime
import json
from pathlib import Path
from application.GlobalVariables import GlobalVariables
from application.send_email.SendEmail import SendEmail
from data_provider.data_provider_835 import DataProvider835
from data_provider.data_provider_835_by_id import DataProvider835ById
from application.ConnectMongoDB import ConnectMongoDB
from tabulate import tabulate
import pandas as pd
import xlsxwriter


class Consumer835:
    def __init__(self, credentials_code):
        self.__credentials_code = credentials_code
        self.__credential = False
        self.__config_file = None
        self.__number_of_payments = 0
        self.__edi_file = None
        self.__payment = None
        self.__master_payment = None
        self.__segment = None
        self.__st = None
        self.__payments = None
        self.__master_payments = None
        self.__database_name = None
        self.__st = None
        self.__final_report = None
        self.__create_excel_sheet = False
        self.__table = None
        self.__last_report = None
        self.__bpr_id_payment = None
        self.__bpr_id_master_payment = None
        self.__data_provider_edi_file = None
        self.__number_of_claims = 0
        Path("final_reports").mkdir(parents=True, exist_ok=True)
        self.__claims_rejected = []
        self.__send_email = None
        self.__global_var = GlobalVariables()
        self.__connection_dev = ConnectMongoDB('devDB')
        self.__connection_dev.connect_to_collection('referenceTables')

    def check_credentials_code(self):
        if self.__credentials_code == "":
            self.__credential = True
            return True
        else:
            return False

    def __fill_final_report(self, edi_file, payment):
        self.__edi_file = edi_file
        self.__payment = payment
        if self.__credential:
            self.__data_provider_edi_file = DataProvider835ById(self.__edi_file)
            self.__data_provider_edi_file.build_body_data_provider(self.__st)
            self.__data_provider_edi_file.payment_data_provider_by_bpr(self.__payment)
            # self.__write_to_final_report_header_section(
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[4: 6] + '/' +
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[6: 8] + '/' +
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[0: 4],
            #     self.__data_provider_edi_file.st_data_provider.get_by_id_repeated_once('1000A', 'N1', '89_02'),
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('31') + '-' +
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr04_description(),
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('30') + '-' +
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr03_description(),
            #     self.__data_provider_edi_file.bpr_data_provider.get_trn_element_by_id('51'),
            #     self.__data_provider_edi_file.bpr_data_provider.get_trn_element_by_id('50'),
            #     self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('29')
            # )
            for loop in self.__st:
                if loop.split('-')[0] == "2000":
                    self.__data_provider_edi_file.build_claim_data_provider(self.__st.get(loop), self.__final_report)

                    if self.__create_excel_sheet:
                        writer = pd.ExcelWriter(f'final_reports/{self.__file_name}', engine='xlsxwriter')
                        df = pd.DataFrame({
                                'Visit ID': self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100',
                                                                                                                 'CLP',
                                                                                                                 '202',
                                                                                                                 "Visit ID: "),

                                'Claim 1': self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100',
                                                                                                                'CLP',
                                                                                                                '208',
                                                                                                                "Payer internal control "
                                                                                                                "number: "),

                                'Service line control 1': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2110', 'REF',
                                    '431',
                                    "Service line control: "),

                                'DOS': self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[
                                       4: 6] + '/' +
                                       self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[
                                       6: 8] + '/' +
                                       self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('43')[
                                       0: 4],

                                'CPT': 90837,

                                'Total Charge': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2110', 'SVC', '395',
                                    "Charge amount: "),

                                'Allowed Amount': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2110', 'SVC', '396',
                                    "Payment amount: "),

                                'Insurance Adjustment': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2110', 'CAS', '409',
                                    "Adjustment amount: "),

                                'Insurance Payment': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2100', 'CLP', '205',
                                    "Total payment amount: "),

                                'Patient Responsibility': self.__data_provider_edi_file.claim_data_provider.write_all_segments(
                                    '2100', 'CLP', '206',
                                    "Total patient responsibility: ")
                            }, index=[0])

                        df.to_excel(writer, sheet_name='Info from 835', index=False)
                        for column in df:
                            column_width = max(df[column].astype(str).map(len).max(), len(column))
                            col_idx = df.columns.get_loc(column)
                            writer.sheets['Info from 835'].set_column(col_idx, col_idx, column_width)

                        writer.save()
                        break
                    self.__number_of_claims += 1
                    self.__write_new_line()
                    self.__write_new_line_and_tap()
                    self.__final_report.write(f"Claim {self.__number_of_claims}")
                    self.__write_new_line_and_tap()
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2000', 'LX', '158',
                                                                                         "Transaction set assigned "
                                                                                         "number: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '202',
                                                                                         "Visit ID: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '203',
                                                                                         "Claim status: ", "", True)
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '204',
                                                                                         "Total charge amount: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '205',
                                                                                         "Total payment amount: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '206',
                                                                                         "Total patient responsibility: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '207',
                                                                                         "Plan type: ", "", True)
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '208',
                                                                                         "Payer internal control "
                                                                                         "number: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '209',
                                                                                         "Facility type code: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'CLP', '210',
                                                                                         "Frequency type code: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '235',
                                                                                         "Entity identifier code: ",
                                                                                         "", True)
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '236',
                                                                                         "Entity type qualifier: ",
                                                                                         "", True)
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '237',
                                                                                         "Patient last name: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '238',
                                                                                         "Patient first name: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '239',
                                                                                         "Patient Middle/Initial name: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '241',
                                                                                         "Patient name suffix: ")
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '242',
                                                                                         "Identification code "
                                                                                         "qualifier: ",
                                                                                         "", True)
                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2100', 'NM1', '243',
                                                                                         "Identification code: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'SVC', '394',
                                                                                         "Product or service ID "
                                                                                         "qualifier: ", True,
                                                                                         "", True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'SVC', '395',
                                                                                         "Charge amount: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'SVC', '396',
                                                                                         "Payment amount: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'DTM', '401',
                                                                                         "Date/Time qualifier: ",
                                                                                         "", True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'DTM', '402',
                                                                                         "Service date: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'CAS', '407',
                                                                                         "Adjustment group code: ",
                                                                                         "", True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'CAS', '408',
                                                                                         "Adjustment reason code: ",
                                                                                         "", True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'CAS', '409',
                                                                                         "Adjustment amount: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'REF', '430',
                                                                                         "Reference identification "
                                                                                         "qualifier: ", "",
                                                                                         True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'REF', '431',
                                                                                         "Line item control number: ")

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'AMT', '442',
                                                                                         "Amount qualifier code: ",
                                                                                         "", True)

                    self.__data_provider_edi_file.claim_data_provider.write_all_segments('2110', 'AMT', '443',
                                                                                         "Service supplemental amount: ")

                    self.__final_report.write('-' * 100)
                    break
        # self.__final_report.close()
        # self.__send_email = SendEmail(self.__global_var.get_text(), self.__global_var.get_html())
        # self.__send_email.send_email(f'final_reports/{self.__file_name}')

    def __write_to_final_report_header_section(self, payment_date, payer_name, payment_method, flag_code,
                                               originating_company, check_number, payment_amount):
        self.__write_new_line()
        self.__final_report.write(f"Payment Date {payment_date}")
        self.__write_new_line()
        self.__final_report.write(f"Payer Type Insurance")
        self.__write_new_line()
        self.__final_report.write(f"Payer Name {payer_name}")
        self.__write_new_line()
        self.__final_report.write(f"Payment Method {payment_method}")
        self.__write_new_line()
        self.__final_report.write(f"Credit or Debit Flag Code {flag_code}")
        self.__write_new_line()
        self.__final_report.write(f"Originating Company {originating_company}")
        self.__write_new_line()
        self.__final_report.write(f"Check Number {check_number}")
        self.__write_new_line()
        self.__final_report.write(f"Payment Amount {payment_amount}")

    def __write_header_section(self):
        self.__final_report.write(f"FINAL REPORT\n\n".center(100))
        self.__final_report.write(f"\n835 File Name: {self.__master_payment.get('header_section').get('file_name')}")
        self.__final_report.write(f"\nThis file has {self.__number_of_payments} payment(s)\n")
        self.__final_report.write('-' * 100 + "\n\n")

    def __create_file_name_and_open(self):
        # self.__file_name = self.__database_name + '_' + \
        #                    datetime.datetime.now().date().strftime("%Y%m%d") + '_' + \
        #                    datetime.datetime.now().time().strftime("%H%M%S") + \
        #                    '.txt'
        self.__file_name = self.__database_name + '_' + \
                           datetime.datetime.now().date().strftime("%Y%m%d") + '_' + \
                           datetime.datetime.now().time().strftime("%H%M%S") + \
                           '.xlsx'
        # self.__final_report = open(f"final_reports/{self.__file_name}", 'w')

    def process_payment(self, payments, master_payments, db_name):
        self.__payments = payments
        self.__master_payment = master_payments
        self.__create_excel_sheet = True
        for payment in self.__payments:
            if payment.get('header_section').get('bpr_id') == 2849300528:
                self.__bpr_id_payment = payment.get('header_section').get('bpr_id')
                self.__master_payment = self.__get_master_payment()
                if self.__master_payment is None:
                    return
                self.__database_name = db_name
                self.__create_file_name_and_open()
                self.__number_of_payments += 1
                # self.__write_header_section()
                self.__fill_final_report(self.__master_payment, payment)

    def __get_master_payment(self):
        for segment in self.__master_payment:
            if segment.split('-')[0] == 'ST':
                for sub_segment in self.__master_payment.get(segment):
                    if sub_segment.split('-')[0] == 'BPR':
                        self.__bpr_id_master_payment = self.__master_payment.get(segment).get(sub_segment).get('bpr_id')
                        if self.__bpr_id_master_payment == self.__bpr_id_payment:
                            self.__number_of_payments += 1
                            self.__st = self.__master_payment.get(segment)
                            return self.__master_payment

    def __write_new_line(self):
        self.__final_report.write('\n')

    def __write_new_line_and_tap(self):
        self.__final_report.write('\n\t')

    # def __write_to_final_report_body_section(self, transaction_set_assigned_number, visit_id, claim_status,
    #                                          total_charge_amount, total_payment_amount, total_patient_responsibility,
    #                                          plan_type, payer_internal_control_number, facility_type, frequency_type,
    #                                          entity_identifier, entity_type, patient_last_name, patient_first_name,
    #                                          patient_middle_name, patient_suffix_name, identification_code,
    #                                          identification_code_qualifier):
    #     with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
    #         self.__final_report.write(f"\n\tClaim {self.__number_of_claims}")
    #         self.__final_report.write(f"\n\tTransaction set Assigned number {transaction_set_assigned_number}")
    #         self.__final_report.write(f"\n\tVisit ID {visit_id}")
    #         self.__final_report.write(f"\n\tClaim Status {claim_status}")
    #         self.__final_report.write(f"\n\tTotal Charge Amount {total_charge_amount}")
    #         self.__final_report.write(f"\n\tTotal Payment Amount {total_payment_amount}")
    #         self.__final_report.write(f"\n\tTotal Patient Responsibility {total_patient_responsibility}")
    #         self.__final_report.write(f"\n\tPlan Type {plan_type}")
    #         self.__final_report.write(f"\n\tPayer Internal Control Number {payer_internal_control_number}")
    #         self.__final_report.write(f"\n\tFacility Type Code {facility_type}")
    #         self.__final_report.write(f"\n\tFrequency Type Code {frequency_type}")
    #         self.__final_report.write(f"\n\tEntity Identifier Code {entity_identifier}")
    #         self.__final_report.write(f"\n\tEntity Type Qualifier {entity_type}")
    #         self.__final_report.write(f"\n\tPatient Last Name {patient_last_name}")
    #         self.__final_report.write(f"\n\tPatient First Name {patient_first_name}")
    #         self.__final_report.write(f"\n\tPatient Middle/Initial Name {patient_middle_name}")
    #         self.__final_report.write(f"\n\tPatient Name Suffix {patient_suffix_name}")
    #         self.__final_report.write(f"\n\tIdentification Code Qualifier {identification_code}")
    #         self.__final_report.write(f"\n\tIdentification Code {identification_code_qualifier}")
    #         self.__final_report.write(f"\n" + '-' * 100)
