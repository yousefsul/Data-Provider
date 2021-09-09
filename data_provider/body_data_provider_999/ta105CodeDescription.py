def get_ta105_definition(code_element):
    if code_element == '':
        return ' '

    ta105_def = {
        "000": "No error",
        "001": "The interchange control number in the header and trailer do not match",
        "002": "The standard as noted in the control standards identifier is not supported",
        "003": "This version of the controls is not supported",
        "004": "The segment terminator is invalid",
        "005": "Invalid interchange ID qualifier for sender",
        "006": "Invalid interchange sender ID",
        "007": "Invalid interchange ID qualifier for receiver",
        "008": "Invalid interchange receiver ID",
        "009": "Unknown interchange receiver ID",
        "010": "Invalid authorization information qualifier value",
        "011": "Invalid authorization information value",
        "012": "Invalid security information qualifier value",
        "013": "Invalid security information value",
        "014": "Invalid interchange date value",
        "015": "Invalid interchange time value",
        "016": "Invalid interchange standards identifier value",
        "017": "Invalid interchange version ID value",
        "018": "Invalid interchange control number value",
        "019": "Invalid acknowledgement requested value",
        "020": "Invalid test indicator value",
        "021": "Invalid number of included groups value",
        "022": "Invalid control structure",
        "023": "Improper (premature) end-of-file (transmission)",
        "024": "Invalid interchange content (e.g. invalid GS segment)",
        "025": "Duplicate interchange control number",
        "026": "Invalid data element separator",
        "027": "Invalid component element separator",
        "028": "Invalid delivery date in deferred delivery request",
        "029": "Invalid delivery time in deferred delivery request",
        "030": "Invalid deliver time code in deferred delivery request",
        "031": "Invalid grade of service code",
    }
    return ta105_def[code_element]
