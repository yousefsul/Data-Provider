def get_hl(__loop2000d):
    __hl = {}
    for segment in __loop2000d:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000d.get(segment)
            return __hl


def get_loop2100d_nm1(__loop2100d):
    __nm1 = {}
    for segment in __loop2100d:
        if segment == '2100D':
            for seg in __loop2100d.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100d.get(segment).get(seg)
                    return __nm1


def get_loop2200d_trn(__loop2200d):
    __trn = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'TRN':
                            __trn = __loop2200d.get(segment).get(seg).get(s)
                            return __trn


def get_loop2200d_stc(__loop2000d):
    __stc = {}
    for segment in __loop2000d:
        if segment == '2100D':
            for seg in __loop2000d.get(segment):
                if seg == '2200D':
                    for s in __loop2000d.get(segment).get(seg):
                        if s.split('-')[0] == 'STC':
                            __stc = __loop2000d.get(segment).get(seg).get(s)
                            return __stc


def get_loop2200d_ref(__loop2000d):
    __ref = {}
    for segment in __loop2000d:
        if segment == '2100D':
            for seg in __loop2000d.get(segment):
                if seg == '2200D':
                    for s in __loop2000d.get(segment).get(seg):
                        if s.split('-')[0] == 'REF':
                            __ref = __loop2000d.get(segment).get(seg).get(s)
                            return __ref


def get_loop2200d_dtp(__loop2200d):
    __first_dtp = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __first_dtp = __loop2200d.get(segment).get(seg).get(s)
                            return __first_dtp
