import datetime
from pathlib import Path
from data_provider.data_provider_837 import DataProvider837
from data_provider.data_provider_999 import DataProvider999


class Consumer:
    def __init__(self, credentials_code):
        self.__credentials_code = credentials_code
        self.__credential = False
        self.__config_file = None
        self.__loop_count = 0
        self.__edi_file = None
        self.__ack_file = None
        self.__segment = None
        self.__rejected = 0
        self.__accepted = 0
        self.__final_report = None
        Path("final_reports").mkdir(parents=True, exist_ok=True)
        self.__claims_rejected = []

    def check_credentials_code(self):
        if self.__credentials_code == "":
            self.__credential = True
            return True
        else:
            return False

    def check_ack_file(self, edi_file, ack_file):
        self.__edi_file = edi_file
        self.__ack_file = ack_file
        if self.__credential:
            self.__data_provider_edi_file = DataProvider837(self.__edi_file)
            self.__data_provider_ack_file = DataProvider999(self.__ack_file)
            self.__create_the_file()
            self.__data_provider_edi_file.get_count_body_segments()
            self.__write_header_section()
            self.__loop_count = self.__data_provider_edi_file.get_count_body_segments()
            # if self.__data_provider_ack_file.ta1_data_provider.get_ta104() == 'R':
            #     self.__write_to_final_report_ta1_error()
            #     return
            # self.__write_header_section()

            while self.__loop_count > 0:
                for self.__ack_segment in self.__edi_file:
                    self.__segment = self.__ack_segment.split('-')[0]
                    if self.__segment == 'ST':
                        self.__data_provider_edi_file.bulid_body_data_provider(self.__edi_file.get(self.__ack_segment))
                        self.__data_provider_ack_file.bulid_body_data_provider(
                            self.__data_provider_edi_file.st_data_provider.get_st02())
                        self.__write_to_final_report(self.__data_provider_edi_file.st_data_provider.get_st02(),
                                                     self.__data_provider_ack_file.ak2_data_provider.get_ik501())
                    self.__loop_count -= 1
            self.__write_trailer_section()

    def __write_to_final_report(self, claim_num, response):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            if response == 'A':
                self.__accepted += 1
                self.__final_report.write(f"\nClaim with number {claim_num} is Accepted\n\n")
                self.__final_report.write('-' * 75)
            if response == 'R':
                self.__rejected += 1
                self.__claims_rejected.append(self.__data_provider_ack_file.ak2_data_provider.get_ak202())
                self.__final_report.write(f"\nClaim with number {claim_num} is Rejected\n")
                self.__final_report.write("Rejected because of :\n")
                self.__final_report.write(
                    f"Segment Error {self.__data_provider_ack_file.ak2_data_provider.get_ik301()}\n"
                    f"Position in transaction set {self.__data_provider_ack_file.ak2_data_provider.get_ik302()}\n"
                    f"Loop Number {self.__data_provider_ack_file.ak2_data_provider.get_ik303()}\n"
                    f"The Error is {self.__data_provider_ack_file.ak2_data_provider.get_ik304_definition()}\n"
                    f"Business Unit Field Location {self.__data_provider_ack_file.ak2_data_provider.get_ik3_context_01()}\n"
                    f"Data Element Position in Segment {self.__data_provider_ack_file.ak2_data_provider.get_ik401()}\n"
                    f"Data Element Reference Number {self.__data_provider_ack_file.ak2_data_provider.get_ik402()}\n"
                    f"The Syntax Error is {self.__data_provider_ack_file.ak2_data_provider.get_ik403_definition()}\n")
                self.__final_report.write(self.__data_provider_ack_file.ak2_data_provider.get_ik502_definition() + '\n')
                self.__final_report.write(self.__data_provider_ack_file.ak2_data_provider.get_ik304_definition() + '\n')
                self.__final_report.write('-' * 75)


    def __write_header_section(self):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            self.__final_report.write(
                f"FINAL REPORT\n\n".center(100))
            self.__final_report.write(
                f"\nEdi File Name: {self.__data_provider_edi_file.get_edi_file_name()} \n"
                f"Acknowledgement File Name: {self.__data_provider_ack_file.get_ack_file_name()}\n"
                f"This file have {self.__loop_count} claims\n"
                f"This file is {self.__data_provider_ack_file.ak9_data_provider.get_ak901_definition()}\n\n")
            self.__final_report.write('-' * 100 + "\n\n")

    def __write_trailer_section(self):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            self.__final_report.write(
                f"\n\nNumber of claims accepted {self.__accepted}\nNumber of claims rejected {self.__rejected}\n"
                f"The claims rejected numbers {self.__claims_rejected}\n")
            self.__final_report.write('-' * 100 + "\n\n")

    def __write_to_final_report_ta1_error(self):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            self.__final_report.write(
                f"FINAL REPORT\n\n".center(100))
            self.__final_report.write("\nFile have interchange level error \n"
                                      f"The Error is "
                                      f"{self.__data_provider_ack_file.ta1_data_provider.get_ta105_definition()}\n"
                                      "Fix the error and resubmit the file to the payer ... \n")
            self.__final_report.write('-' * 100 + "\n\n")

    def __create_the_file(self):
        self.__file_name = self.__data_provider_ack_file.get_database_name() + '_' + \
                           datetime.datetime.now().date().strftime("%Y%m%d") + '_' + \
                           datetime.datetime.now().time().strftime("%H%M%S") + '_' + \
                           self.__data_provider_ack_file.gs_data_provider.get_gs04() + '_' + \
                           self.__data_provider_ack_file.isa_data_provider.get_isa06().strip() + '.txt'





