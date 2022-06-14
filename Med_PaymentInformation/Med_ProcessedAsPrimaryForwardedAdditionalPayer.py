from medvertex_rcm.Med_Services.Med_PaymentInformation import MainPaymentInformation


class ProcessedAsPrimaryForwardedAdditionalPayer(MainPaymentInformation):
    def __init__(self, claim_status_code, claim_frequency_type_code):
        super().__init__(claim_status_code, claim_frequency_type_code)
