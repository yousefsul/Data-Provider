from Med_PaymentInformation.Med_PaymentPosting import PaymentPosting


def __is_object_filled(payment_posting_object):
    return True if payment_posting_object is not None else False


if __name__ == "__main__":  # Added by yousef task CLP02 processing

    visit_id = ""
    svc = {
            "SVC-60": {
                "394": "HC:99214",
                "395": "270",
                "396": "44"
            },
            "DTM-61": {
                "401": "472",
                "402": "20200224"
            },
            "CAS-62": {
                "407": "PR",
                "408": "3",
                "409": "25"
            },
            "CAS-63": {
                "407": "CO",
                "408": "45",
                "409": "201"
            },
            "REF-64": {
                "430": "6R",
                "431": "756974415L758159402"
            },
            "AMT-65": {
                "442": "B6",
                "443": "69"
            }

    }
    ## svc
    ## amt
    main_payment_information = PaymentPosting('1', '1', svc, visit_id)
    payment_posting_object = main_payment_information.get_payment_status()
    if __is_object_filled(payment_posting_object):
        payment_posting_object.print_hello()
        payment_posting_object.calculate_total_service_line_adjustment()
    else:
        print('No Match')

    # main_payment_information = MainPaymentInformation('1', '19',svc, visit_id)
    # payment_posting_object = main_payment_information.get_payment_status()
    # if __is_object_filled(payment_posting_object):
    #     payment_posting_object.print_hello()
    # else:
    #     print('No Match')

    # main_payment_information = MainPaymentInformation('1', '1')
    # x = main_payment_information.get_payment_status()
    # print(x)
    # x.print_hello()
    #
    # main_payment_information = MainPaymentInformation('1', '19')
    # x = main_payment_information.get_payment_status()
    # print(x)
    # x.print_hello()

    # main_payment_information = MainPaymentInformation('25', '0')
    # x = main_payment_information.get_payment_status()
    # print(x)
    # x.print_hello()
