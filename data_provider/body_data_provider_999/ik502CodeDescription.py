def get_ik502_definition(code_element):
    if code_element == '':
        return ' '

    ik502_def = {
        "1": "Transaction Set Not Supported",

        "2": "Transaction Set Trailer Missing",

        "3": "Transaction Set Control Number in Header and Trailer Do Not Match",

        "4": "Number of Included Segments Does Not Match Actual Count",

        "5": "One or More Segments in Error",

        "6": "Missing or Invalid Transaction Set Identifier",

        "7": "Missing or Invalid Transaction Set Control Number",

        "8": "Authentication Key Name Unknown",

        "9": "Encryption Key Name Unknown",

        "10": "Requested Service (Authentication or Encrypted) Not Available",

        "11": "Unknown Security Recipient",

        "12": "Incorrect Message Length (Encryption Only)",

        "13": "Message Authentication Code Failed",

        "15": "Unknown Security Originator",

        "16": "Syntax Error in Decrypted Text",

        "17": "Security Not Supported",

        "18": "Transaction Set not in Functional Group",

        "19": "Invalid Transaction Set Implementation Convention Reference",

        "23": " Transaction Set Control Number Not Unique within theFunctional Group",

        "24": "S3E Security End Segment Missing for S3S Security StartSegment",

        "25": "S3S Security Start Segment Missing for S3E Security End Segment",

        "26": "S4E Security End Segment Missing for S4S Security Start Segment",

        "27": "S4S Security Start Segment Missing for S4E Security End Segment",

        'I5': "Implementation One or More Segments in Error",

        'I6': "Implementation Convention Not Supported",

    }
    return ik502_def[code_element]
