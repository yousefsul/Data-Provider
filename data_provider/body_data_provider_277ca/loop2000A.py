def get_hl(__loop2000a):
    __hl = {}
    for segment in __loop2000a:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000a.get(segment)
            return __hl


def get_loop2100a_nm1(__loop2100a):
    __nm1 = {}
    for segment in __loop2100a:
        if segment == '2100A':
            for seg in __loop2100a.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100a.get(segment).get(seg)
                    return __nm1


def get_loop2200a_trn(__loop2200a):
    __trn = {}
    for segment in __loop2200a:
        if segment == '2100A':
            for seg in __loop2200a.get(segment):
                if seg == '2200A':
                    for s in __loop2200a.get(segment).get(seg):
                        if s.split('-')[0] == 'TRN':
                            __trn = __loop2200a.get(segment).get(seg).get(s)
                            return __trn


def get_loop2200a_first_dtp(__loop2200a):
    __first_dtp = {}
    for segment in __loop2200a:
        if segment == '2100A':
            for seg in __loop2200a.get(segment):
                if seg == '2200A':
                    for s in __loop2200a.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __first_dtp = __loop2200a.get(segment).get(seg).get(s)
                            return __first_dtp


def get_loop2200a_second_dtp(__loop2200a):
    __second_dtp = {}
    for segment in __loop2200a:
        if segment == '2100A':
            for seg in __loop2200a.get(segment):
                if seg == '2200A':
                    for s in __loop2200a.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __second_dtp = __loop2200a.get(segment).get(seg).get(s)
                            return __second_dtp
