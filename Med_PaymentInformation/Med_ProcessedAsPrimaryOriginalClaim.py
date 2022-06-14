from Med_PaymentInformation import MainPaymentInformation


class ProcessedAsPrimaryOriginalClaim(MainPaymentInformation):
    def __init__(self, claim_status_code, claim_frequency_type_code, svc, visit_id):
        super().__init__(claim_status_code, claim_frequency_type_code, svc, visit_id)

    def print_hello(self):
        print("Hello world from ProcessedAsPrimary")

    # def calculate_total_service_line_adjustment(self):
    #     for segment in self._svc:
    #         if segment.split('-')[0] == 'SVC':
    #             self._svc02 = self.__check_value(self._svc.get('395'))
    #         print(segment)
    #     # self._tsla = svc02 - svc03
    #
    # def validate_service_line(self):
    #     pass
    #
    # def __check_value(self, amount):
    #     return
    #     # return True if payment_posting_object is not None else False
