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


def get_loop2200d_amt(__loop2200d):
    __amt = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'AMT':
                            __amt = __loop2200d.get(segment).get(seg).get(s)
                            return __amt


def get_loop2200d_dtp(__loop2200d):
    __dtp = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __dtp = __loop2200d.get(segment).get(seg).get(s)
                            return __dtp
