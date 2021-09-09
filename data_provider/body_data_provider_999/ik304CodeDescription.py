def get_ik304_definition(code_element):
    if code_element == '':
        return ' '

    ik304_def = {
        "1": "Unrecognized segment ID",

        "2": "Unexpected segment",

        "3": "Required Segment Missing",

        "4": "Loop Occurs Over Maximum Times",

        "5": "Segment Exceeds Maximum Use",

        "6": "Segment Not in Defined Transaction Set",

        "7": "Segment Not in Proper Sequence",

        "8": "Segment Has Data Element Errors",

        "14": "Implementation “Not Used” Segment Present",

        "16": "Implementation Dependent Segment Missing",

        "17": "Implementation Loop Occurs Under Minimum Times",

        "18": "Implementation Segment Below Minimum Use",

        "19": "Implementation Dependent “Not Used” Segment Present",

    }
    return ik304_def[code_element]
