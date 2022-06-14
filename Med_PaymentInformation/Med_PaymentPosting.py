from application.ConnectMongoDB import ConnectMongoDB
from application.GlobalVariables import GlobalVariables


class PaymentPosting:
    def __init__(self, claim_status_code, claim_frequency_type_code, svc, visit_id):
        self._claim_status_code_835 = claim_status_code  # clp02
        self._claim_frequency_type_code = claim_frequency_type_code  # clp09
        self.__document = None
        self.__count = 0
        self._svc = svc
        self._visit_id = visit_id
        self._tsla = self._svc02 = self._svc03 = float()
        self.__global_var = GlobalVariables()
        self.__payment_status = None
        self.__connection = ConnectMongoDB(self.__global_var.get_main_db_name())
        self.__connection.connect_to_collection('referenceTables')
        self.__reference_tables_collection = self.__connection.find_from_collection()
        self.__claim_status_code = self.__get_claim_status_code()
        self.__claim_status_code_keys = list(dict.keys(self.__claim_status_code))
        self.__claim_status_code_keys_len = len(self.__claim_status_code_keys) - 1
        self.__payment_status = self.__payment_processing()

    def __payment_processing(self):
        match self._claim_status_code_835:  # Send Empty parameter to subclasses for break infinite loop
            case '1':
                return self.__processed_as_primary()
            # case '2':
            #     from Med_PaymentInformation.Med_ProcessedAsSecondary import ProcessedAsSecondary
            #     self.__payment_status = ProcessedAsSecondary('')
            #     return self.__payment_status
            #
            # case '3':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_ProcessedAsTertiary import \
            #         ProcessedAsTertiary
            #     self.__payment_status = ProcessedAsTertiary('')
            #     return self.__payment_status
            #
            # case '4':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_Denied import Denied
            #     self.__payment_status = Denied('')
            #     return self.__payment_status
            #
            # case '19':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_ProcessedAsPrimaryForwardedAdditionalPayer import \
            #         ProcessedAsPrimaryForwardedAdditionalPayer
            #     self.__payment_status = ProcessedAsPrimaryForwardedAdditionalPayer('')
            #     return self.__payment_status
            #
            # case '20':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_ProcessedAsSecondaryForwardedAdditionalPayer import \
            #         ProcessedAsSecondaryForwardedAdditionalPayer
            #     self.__payment_status = ProcessedAsSecondaryForwardedAdditionalPayer('')
            #     return self.__payment_status
            #
            # case '21':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_ProcessedAsTertiaryForwardedAdditionalPayer import \
            #         ProcessedAsTertiaryForwardedAdditionalPayer
            #     self.__payment_status = ProcessedAsTertiaryForwardedAdditionalPayer('')
            #     return self.__payment_status
            #
            # case '22':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_ReversalOfPreviousPayment import \
            #         ReversalOfPreviousPayment
            #     self.__payment_status = ReversalOfPreviousPayment('')
            #     return self.__payment_status
            #
            # case '23':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_NotOurClaimForwardedAdditionalPayer import \
            #         NotOurClaimForwardedAdditionalPayer
            #     self.__payment_status = NotOurClaimForwardedAdditionalPayer('')
            #     return self.__payment_status
            #
            # case '25':
            #     from medvertex_rcm.Med_Services.Med_PaymentInformation.Med_PredeterminationPricingOnlyNoPayment import \
            #         PredeterminationPricingOnlyNoPayment
            #     self.__payment_status = PredeterminationPricingOnlyNoPayment('')
            #     return self.__payment_status

    def __get_claim_status_code(self):
        for self.__document in self.__reference_tables_collection:
            if self.__document.get('Claim Status Code') is not None:
                return self.__document.get('Claim Status Code')

    def __get_status_code(self):
        self.__claim_status_code_tmp = self.__claim_status_code_keys[self.__claim_status_code_keys_len]
        self.__claim_status_code_keys_len -= 1
        return self.__claim_status_code_tmp

    def get_payment_status(self):
        return self.__payment_status

    def print_hello(self):
        pass

    def __processed_as_primary(self):
        match self._claim_frequency_type_code:
            case '1':
                from Med_PaymentInformation.Med_ProcessedAsPrimaryOriginalClaim import ProcessedAsPrimaryOriginalClaim
                self.__payment_status = ProcessedAsPrimaryOriginalClaim('', '', '', '')
                return self.__payment_status
            case _:
                print("There are no match")
        # payment {
        #   1,
        #   2,
        #   multi threading 3
        #
        # }
        #
        # 3
        #  the first thread calling the payment posting and send param the payment  ----> payment posting 3 svc will create thread
        #  the second thread write to template
