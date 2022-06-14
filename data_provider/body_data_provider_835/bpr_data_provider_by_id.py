class BprDataProviderById:
    def __init__(self, payment):
        self.__payment = payment
        self.__bpr_id = None
        self.__trn_id = None
        self.__bpr03_description = {
            "C": "Credit",
            "D": "Debit",
            "NP": "Not Provided",
        }
        self.__bpr04_description = {
            "ACH": "Automated Clearing House",
            "BOP": "Financial Institution Option",
            "CHK": "Check",
            "FWT": "Federal Reserve Funds/Wire Transfer - Nonrepetitive",
            "NON": "Non-Payment Data",
            "NP": "Not Provided",
        }
        self.__bpr_tmp = {}
        self.__bpr = {}
        self.__build_bpr_dashed()
        self.__build_bpr()
        self.__np = 'NP'
        self.__trn_tmp = {}
        self.__trn = {}
        self.__build_trn_dashed()
        self.__build_trn()
        self.__plb_tmp = {}
        self.__plb = {}
        self.__build_plb_dashed()
        self.__build_plb()


    def __build_bpr_dashed(self):
        for segment in self.__payment:
            if segment == 'BPR':
                self.__bpr_tmp = self.__payment.get(segment)

    def __build_trn_dashed(self):
        for segment in self.__payment:
            if segment == 'TRN':
                self.__trn_tmp = self.__payment.get(segment)

    def get_bpr_element_by_id(self, data_element_id):
        self.__bpr_id = data_element_id
        return self.__bpr.get(self.__bpr_id)

    def get_trn_element_by_id(self, data_element_id):
        self.__trn_id = data_element_id
        return self.__trn.get(self.__trn_id)

    def get_bpr03_description(self):
        return self.__bpr03_description.get(self.__bpr.get(self.__bpr_id))

    def get_bpr04_description(self):
        return self.__bpr04_description.get(self.__bpr.get(self.__bpr_id))

    def __build_bpr(self):
        for data_element in self.__bpr_tmp:
            self.__bpr.update({data_element.split('_')[0]: self.__bpr_tmp.get(data_element)})

    def __build_trn(self):
        for data_element in self.__trn_tmp:
            self.__trn.update({data_element.split('_')[0]: self.__trn_tmp.get(data_element)})

    def __build_plb(self):
        for data_element in self.__plb_tmp:
            self.__plb.update({data_element.split('_')[0]: self.__plb_tmp.get(data_element)})

    def __build_plb_dashed(self):
        for segment in self.__payment:
            if segment == 'PLB':
                self.__plb_tmp = self.__payment.get(segment)
