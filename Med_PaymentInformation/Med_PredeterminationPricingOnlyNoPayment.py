from medvertex_rcm.Med_Services.Med_PaymentInformation import MainPaymentInformation


class PredeterminationPricingOnlyNoPayment(MainPaymentInformation):
    def __init__(self, claim_status_code):
        super().__init__(claim_status_code)



    def print_hello(self):
        print("Hello world from PredeterminationPricingOnlyNoPayment")