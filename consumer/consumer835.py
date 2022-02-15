import datetime
import glob
import json
import os
import pathlib
from dataclasses import dataclass
from pathlib import Path

import babel as babel
import numpy as np
import pandas
import xlsxwriter
from application.GlobalVariables import GlobalVariables
from application.send_email.SendEmail import SendEmail
from bson import Decimal128
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment
from xlsxwriter.format import Format

from data_provider.data_provider_835 import DataProvider835
from data_provider.data_provider_835_by_id import DataProvider835ById
from application.ConnectMongoDB import ConnectMongoDB
import pandas as pd
import xlwings as xw
from re import sub
from decimal import Decimal


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
        self.__file_name_excel = None
        self.__line_charge = self.__line_paid_amount = self.__adjustment_amount = \
            self.__patient_responsibility = self.__allowed_amount = "{:.2f}".format(0.00)

        # Decimal128(str('0.00'))
        self.__line_charge_total = self.__line_paid_amount_total = self.__adjustment_amount_total = \
            self.__patient_responsibility_total = self.__allowed_amount_total = "{:.2f}".format(0.00)

        self.__excel_data_frame = {}
        self.__data_frame = None
        self.__number_of_claims = 0
        self.__count_row = 0
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
                self.__data_provider_edi_file.bpr_data_provider.get_bpr_element_by_id('29')
            )
            for loop in self.__st:
                if loop.split('-')[0] == "2000":
                    self.__svc_count = 0
                    self.__data_provider_edi_file.build_claim_data_provider(self.__st.get(loop), self.__final_report)
                    self.__number_of_claims += 1
                    self.__write_new_line()
                    self.__write_new_line()
                    self.__final_report.write(f"Claim# {self.__number_of_claims}:")
                    self.__write_new_line_and_tap()

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'LX', '158')

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', None)

                    self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'NM1', '235',
                                                                                            is_by_code=True, code='QC')
                    self.__write_new_line()
                    self.__write_new_tap()

                    while self.__data_provider_edi_file.claim_data_provider.get_number_of_svc() > 0:
                        self.__excel_data_frame = {}
                        self.__svc_count += 1

                        self.__final_report.write(f"Service line# {self.__svc_count}:")

                        self.__write_new_line_and_tap()

                        svc = str(self.__svc_count)

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2000', 'LX', '158',
                                                                                                is_set_specific_data_element=True
                                                                                                )  # Header Number

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '202',
                                                                                                is_set_specific_data_element=True)  # Visit Id
                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2100', 'CLP', '208',
                                                                                                is_set_specific_data_element=True)  # Payer Claim Control Number
                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'REF', '431',
                                                                                                is_set_specific_data_element=True) # Line Item Control Number

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'DTM', '402',
                                                                                                is_set_specific_data_element=True) # Service Date

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '394',
                                                                                                is_sub=True,
                                                                                                is_svc=True)

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_value_label(
                            'Procedure Code',
                            self.__data_provider_edi_file.claim_data_provider.get_from_svc(svc, 'Procedure Code'))

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '395',
                                                                                                is_svc=True)
                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'SVC', '396',
                                                                                                is_svc=True)
                        self.__data_provider_edi_file.claim_data_provider.set_data_element_label(
                            'Allowed Amount'
                        )

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_label(
                            'Line Paid Amount'
                        )

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'DTM', '402',
                                                                                                is_svc=True)

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'CAS', None,
                                                                                                is_write_one_line=True,
                                                                                                is_svc=True)

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'CAS', '409',
                                                                                                is_set_specific_data_element=True,
                                                                                                is_svc=True)
                        self.__append_to_excel_sheet_data_frame()
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report('2110', 'CLP', '205',
                                                                                                is_set_specific_data_element=True)
                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.set_data_element_value_label(
                            'Patient Responsibility',
                            self.__data_provider_edi_file.claim_data_provider.get_from_svc(svc,
                                                                                           'patient_responsibility'))

                        self.__append_to_excel_sheet_data_frame()

                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '430',
                                                                                                is_svc=True)
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'REF', '431',
                                                                                                is_svc=True)
                        self.__data_provider_edi_file.claim_data_provider.write_to_final_report(svc, 'AMT', '443',
                                                                                                is_svc=True)
                        self.__write_to_excel_sheet()

                        self.__data_provider_edi_file.claim_data_provider.decrement_number_of_svc()

                    self.__final_report.write('-' * 100)
                    self.__write_new_line()
        self.__final_report.close()
        self.__write_to_excel_sheet_totals()
        self.__writer.save()
        self.__files = []
        self.__files.append(os.path.abspath(self.__final_report.name))
        self.__files.append(os.path.abspath(self.__writer))
        # self.__send_email = SendEmail(self.__global_var.get_text(), self.__global_var.get_html())
        # self.__send_email.send_email_multi_attachment(self.__files)

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
                           datetime.datetime.now().date().strftime("%Y%m%d") + '_' + \
                           datetime.datetime.now().time().strftime("%H%M%S") + \
                           '.txt'
        self.__file_name_excel = self.__database_name + '_' + \
                                 datetime.datetime.now().date().strftime("%Y%m%d") + '_' + \
                                 datetime.datetime.now().time().strftime("%H%M%S") + \
                                 '.xlsx'

        self.__final_report = open(f"final_reports_files/final_reports/{self.__file_name}", 'w')
        self.__writer = pd.ExcelWriter(f"final_reports_files/final_reports/{self.__file_name_excel}",
                                       engine='xlsxwriter')

    def process_payment(self, payments, master_payments, db_name):
        self.__payments = payments
        self.__master_payment = master_payments
        self.__create_excel_sheet = True
        for payment in self.__payments:
            if payment.get('header_section').get('bpr_id') == 7756516398:
                self.__bpr_id_payment = payment.get('header_section').get('bpr_id')
                self.__master_payment = self.__get_master_payment()
                if self.__master_payment is None:
                    return
                self.__database_name = db_name
                self.__create_file_name_and_open()
                self.__write_header_section()
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

    def __write_new_tap(self):
        self.__final_report.write('\t')

    def __setup_excel_sheet(self):
        self.__data_frame = pd.DataFrame(self.__excel_data_frame, index=[0], dtype=None)
        self.__data_frame.to_excel(self.__writer, sheet_name='info_from_835', index=False,
                                   startrow=self.__count_row * 4, startcol=1)
        self.__workbook = self.__writer.book
        self.__worksheet = self.__workbook.get_worksheet_by_name('info_from_835')
        self.__general_format = self.__workbook.add_format({'border': 2})
        self.__header_format = self.__workbook.add_format({
            'bold': True,
            'border': 2,
            'valign': 'top',
            'fg_color': '#D7E4BC'})
        self.__total_row_format = self.__workbook.add_format({'bold': True, 'font_color': 'red'})
        self.__currency_format = self.__workbook.add_format(
            {'bold': True, 'font_color': 'red', 'num_format': '$#,##0.00'})

        for self.__column in self.__data_frame:
            self.__column_width = max(self.__data_frame[self.__column].astype(str).map(len).max(), len(self.__column))
            self.__col_idx = self.__data_frame.columns.get_loc(self.__column)
            self.__writer.sheets['info_from_835'].set_column(self.__col_idx + 1,
                                                             self.__col_idx + 1,
                                                             self.__column_width)

        for self.__col_num, value in enumerate(self.__data_frame.columns.values):
            self.__worksheet.write(self.__count_row * 4, self.__col_num + 1, value, self.__header_format)

        self.__count_row += 1

    def __append_to_excel_sheet_data_frame(self):
        self.__excel_data_frame.update({self.__data_provider_edi_file.claim_data_provider.get_data_element_label():
                                            self.__data_provider_edi_file.claim_data_provider.get_data_element_value()})

    def __write_to_excel_sheet(self):
        self.__setup_excel_sheet()
        self.__get_sum_of_values()
        self._total_row = self.__data_frame.shape[0] + 1
        self.__total_col = self.__data_frame.columns.get_loc('Line Charge') + 1

        row_values = [self.__line_charge, self.__allowed_amount, self.__line_paid_amount, self.__adjustment_amount,
                      self.__patient_responsibility]

        self.__worksheet.write((self.__count_row * 4) - 4, 0, f'Claim {self.__number_of_claims}', self.__total_row_format)
        self.__worksheet.write((self.__count_row * 4) - 3, 0, f'Service Line {self.__svc_count}', self.__total_row_format)

        self.__worksheet.write((self.__count_row * 4) - 2, 0, 'Totals', self.__total_row_format)

        self.__worksheet.write_row((self.__count_row * 4) - 2, self.__total_col, tuple(row_values),
                                   self.__currency_format)

    def __get_sum_of_values(self):
        for self.__col in self.__data_frame:
            tmp_value = Decimal128('0.00')
            if self.__col == 'Line Charge':
                self.__line_charge = self.__data_frame.get(self.__col).item()
                # tmp_string = str(self.__data_frame.get(self.__col).item()).replace('$', '')
                # tmp_value = Decimal128(tmp_string)
                # self.__line_charge = self.__line_charge.to_decimal() + tmp_value.to_decimal()

            if self.__col == 'Line Paid Amount':
                self.__line_paid_amount = self.__data_frame.get(self.__col).item()
                # tmp_string = str(self.__data_frame.get(self.__col).item()).replace('$', '')
                # tmp_value = Decimal128(tmp_string)
                # self.__line_paid_amount = self.__line_paid_amount.to_decimal() + tmp_value.to_decimal()

            if self.__col == 'Allowed Amount':
                self.__allowed_amount = self.__data_frame.get(self.__col).item()

                # tmp_string = str(self.__data_frame.get(self.__col).item()).replace('$', '')
                # tmp_value = Decimal128(tmp_string)
                # self.__line_paid_amount = self.__line_paid_amount.to_decimal() + tmp_value.to_decimal()

            if self.__col == 'Adjustment Amount':
                self.__adjustment_amount = self.__data_frame.get(self.__col).item()

                # tmp_string = str(self.__data_frame.get(self.__col).item()).replace('$', '')
                # tmp_value = Decimal128(tmp_string)
                # self.__adjustment_amount = self.__adjustment_amount.to_decimal() + tmp_value.to_decimal()

            if self.__col == 'Patient Responsibility':
                self.__patient_responsibility = self.__data_frame.get(self.__col).item()

                # tmp_string = str(self.__data_frame.get(self.__col).item()).replace('$', '')
                # tmp_value = Decimal128(tmp_string)
                # self.__patient_responsibility = self.__patient_responsibility.to_decimal() + tmp_value.to_decimal()

        # self.__line_charge_idx = self.__data_frame.columns.get_loc('Line Charge') + 1
        # strx = xlsxwriter.utility.xl_col_to_name(self.__line_charge_idx)
        # xx = f'{strx}:{strx}'
        # self.__line_paid_amount_idx = self.__data_frame.columns.get_loc('Line Paid Amount') + 1
        # self.__adjustment_amount_idx = self.__data_frame.columns.get_loc('Adjustment Amount') + 1
        # self.__patient_responsibility_idx = self.__data_frame.columns.get_loc('Patient Responsibility') + 1

        # self.__worksheet.set_column(xx, None, self.__currency_format)
        # self.__worksheet.set_column(self.__line_paid_amount_idx, None, self.__currency_format)
        # self.__worksheet.set_column(self.__adjustment_amount_idx, None, self.__currency_format)
        # self.__worksheet.set_column(self.__patient_responsibility_idx, None, self.__currency_format)

    def __write_to_excel_sheet_totals(self):
        print(dir(self.__data_frame))
        print(self.__data_frame.to_string())

