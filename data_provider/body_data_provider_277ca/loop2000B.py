def get_hl(__loop2000b):
    __hl = {}
    for segment in __loop2000b:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000b.get(segment)
            return __hl


def get_loop2100b_nm1(__loop2000b):
    __nm1 = {}
    for segment in __loop2000b:
        if segment == '2100B':
            for seg in __loop2000b.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2000b.get(segment).get(seg)
                    return __nm1


def get_loop2200b_trn(__loop2000b):
    __trn = {}
    for segment in __loop2000b:
        if segment == '2100B':
            for seg in __loop2000b.get(segment):
                if seg == '2200B':
                    for s in __loop2000b.get(segment).get(seg):
                        if s.split('-')[0] == 'TRN':
                            __trn = __loop2000b.get(segment).get(seg).get(s)
                            return __trn


def get_loop2200b_stc(__loop2000b):
    __stc = {}
    for segment in __loop2000b:
        if segment == '2100B':
            for seg in __loop2000b.get(segment):
                if seg == '2200B':
                    for s in __loop2000b.get(segment).get(seg):
                        if s.split('-')[0] == 'STC':
                            __stc = __loop2000b.get(segment).get(seg).get(s)
                            return __stc


def get_loop2200b_qty(__loop2000b):
    __qty = {}
    for segment in __loop2000b:
        if segment == '2100B':
            for seg in __loop2000b.get(segment):
                if seg == '2200B':
                    for s in __loop2000b.get(segment).get(seg):
                        if s.split('-')[0] == 'QTY':
                            __qty = __loop2000b.get(segment).get(seg).get(s)
                            return __qty


def get_loop2200b_amt(__loop2000b):
    __amt = {}
    for segment in __loop2000b:
        if segment == '2100B':
            for seg in __loop2000b.get(segment):
                if seg == '2200B':
                    for s in __loop2000b.get(segment).get(seg):
                        if s.split('-')[0] == 'AMT':
                            __amt = __loop2000b.get(segment).get(seg).get(s)
                            return __amt
