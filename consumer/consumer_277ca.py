from data_provider.data_provider_277CA import DataProvider277CA


class Consumer277CA:
    def __init__(self):
        self.__ack_file = None
        self.__file_name = None

    def check_ack_file(self, ack_file):
        self.__ack_file = ack_file
        self.__file_name = self.__ack_file.get('header_section').get('file_name')

        self.__write_header_section()
        self.__data_provider_ack_file = DataProvider277CA(self.__ack_file)
        self.__data_provider_ack_file.bulid_body_data_provider()
        print(self.__ack_file)
        self.__write_to_final_report()

    def __write_to_final_report(self):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            if self.__data_provider_ack_file.body_data_provider.get_loop2200b_stc03() == 'WQ':
                self.__final_report.write(f"\nClaim with Originator Application Transaction Identifier "
                                          f"{self.__data_provider_ack_file.bht_data_provider.get_bht03()}"
                                          f" is Accepted\n\n")
                self.__final_report.write('-' * 75)
            if self.__data_provider_ack_file.body_data_provider.get_loop2200b_stc03() == 'U':
                self.__final_report.write(f"\nClaim with Originator Application Transaction Identifier "
                                          f"{self.__data_provider_ack_file.bht_data_provider.get_bht03()}"
                                          f" is Rejected\n\n")

    def __write_header_section(self):
        with open(f"final_reports/{self.__file_name}", 'a') as self.__final_report:
            self.__final_report.write(
                f"FINAL REPORT\n\n".center(100))
            self.__final_report.write(
                f"\nEdi File Name: {self.__file_name} \n"
                f"This file is {self.__file_name.split('.')[-1]}\n\n")
            self.__final_report.write('-' * 100 + "\n\n")
    # if response == 'A':
    #     self.__accepted += 1
    #     self.__final_report.write(f"\nClaim with number {claim_num} is Accepted\n\n")
    #     self.__final_report.write('-' * 75)
    # if response == 'R':
    #     self.__rejected += 1
    #     self.__claims_rejected.append(self.__data_provider_ack_file.ak2_data_provider.get_ak202())
    #     self.__final_report.write(f"\nClaim with number {claim_num} is Rejected\n")
    #     self.__final_report.write("Rejected because of :\n")
    #     self.__final_report.write(
    #         f"Segment Error {self.__data_provider_ack_file.ak2_data_provider.get_ik301()}\n"
    #         f"Position in transaction set {self.__data_provider_ack_file.ak2_data_provider.get_ik302()}\n"
    #         f"Loop Number {self.__data_provider_ack_file.ak2_data_provider.get_ik303()}\n"
    #         f"The Error is {self.__data_provider_ack_file.ak2_data_provider.get_ik304_definition()}\n"
    #         f"Business Unit Field Location {self.__data_provider_ack_file.ak2_data_provider.get_ik3_context_01()}\n"
    #         f"Data Element Position in Segment {self.__data_provider_ack_file.ak2_data_provider.get_ik401()}\n"
    #         f"Data Element Reference Number {self.__data_provider_ack_file.ak2_data_provider.get_ik402()}\n"
    #         f"The Syntax Error is {self.__data_provider_ack_file.ak2_data_provider.get_ik403_definition()}\n")
    #     self.__final_report.write(self.__data_provider_ack_file.ak2_data_provider.get_ik502_definition() + '\n')
    #     self.__final_report.write(self.__data_provider_ack_file.ak2_data_provider.get_ik304_definition() + '\n')
    #     self.__final_report.write('-' * 75)
