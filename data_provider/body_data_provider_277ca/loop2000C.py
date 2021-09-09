def get_hl(__loop2000c):
    __hl = {}
    for segment in __loop2000c:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000c.get(segment)
            return __hl


def get_loop2100c_nm1(__loop2100c):
    __nm1 = {}
    for segment in __loop2100c:
        if segment == '2100C':
            for seg in __loop2100c.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100c.get(segment).get(seg)
                    return __nm1


def get_loop2200c_trn(__loop2200c):
    __trn = {}
    for segment in __loop2200c:
        if segment == '2100C':
            for seg in __loop2200c.get(segment):
                if seg == '2200C':
                    for s in __loop2200c.get(segment).get(seg):
                        if s.split('-')[0] == 'TRN':
                            __trn = __loop2200c.get(segment).get(seg).get(s)
                            return __trn


def get_loop2200c_stc(__loop2000c):
    __stc = {}
    for segment in __loop2000c:
        if segment == '2100C':
            for seg in __loop2000c.get(segment):
                if seg == '2200C':
                    for s in __loop2000c.get(segment).get(seg):
                        if s.split('-')[0] == 'STC':
                            __stc = __loop2000c.get(segment).get(seg).get(s)
                            return __stc


def get_loop2200c_qty(__loop2000c):
    __qty = {}
    for segment in __loop2000c:
        if segment == '2100C':
            for seg in __loop2000c.get(segment):
                if seg == '2200C':
                    for s in __loop2000c.get(segment).get(seg):
                        if s.split('-')[0] == 'QTY':
                            __qty = __loop2000c.get(segment).get(seg).get(s)
                            return __qty


def get_loop2200c_amt(__loop2000c):
    __amt = {}
    for segment in __loop2000c:
        if segment == '2100C':
            for seg in __loop2000c.get(segment):
                if seg == '2200C':
                    for s in __loop2000c.get(segment).get(seg):
                        if s.split('-')[0] == 'AMT':
                            __amt = __loop2000c.get(segment).get(seg).get(s)
                            return __amt


def get_loop2200c_first_dtp(__loop2200a):
    __first_dtp = {}
    for segment in __loop2200a:
        if segment == '2100C':
            for seg in __loop2200a.get(segment):
                if seg == '2200C':
                    for s in __loop2200a.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __first_dtp = __loop2200a.get(segment).get(seg).get(s)
                            return __first_dtp


def get_loop2200c_second_dtp(__loop2200a):
    __second_dtp = {}
    for segment in __loop2200a:
        if segment == '2100C':
            for seg in __loop2200a.get(segment):
                if seg == '2200C':
                    for s in __loop2200a.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __second_dtp = __loop2200a.get(segment).get(seg).get(s)
                            return __second_dtp
