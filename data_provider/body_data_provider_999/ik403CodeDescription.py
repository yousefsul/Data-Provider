def get_ik403_definition(code_element):
    if code_element == '':
        return ' '

    ik403_def = {
        "1": "Required Data Element Missing",

        "2": "Conditional Required Data Element Missing",

        "3": "Too Many Data Elements",

        "4": " Data Element Too Short",

        "5": "Data Element Too Long",

        "6": "Invalid Character In Data Element",

        "7": "Invalid Code Valuee",

        "8": "Invalid Date",

        "9": "Invalid Time",

        "10": "Exclusion Condition Violated",

        "12": "Too Many Repetitions",

        'I10': "Implementation “Not Used” Data Element Present",

        'I11': "Implementation Too Few Repetitions",

        'I12': " Implementation Pattern Match Failure",

        'I13': "Implementation Dependent “Not Used” Data Element Present",

        "I6": "Code Value Not Used in Implementation",

        "I9": "Implementation Dependent Data Element Missing",

    }
    return ik403_def[code_element]
