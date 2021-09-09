def get_ak901_definition(code_element):
    if code_element == '':
        return ' '

    ak901_def = {
        "P": "partially accepted",

        "A": "fully accepted",

        "R": "fully rejected",

    }
    return ak901_def[code_element]
