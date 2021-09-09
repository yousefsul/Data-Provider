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


def get_loop2200d_stc(__loop2200d):
    __stc = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'STC':
                            __stc = __loop2200d.get(segment).get(seg).get(s)
                            return __stc


def get_loop2200d_ref_1k(__loop2200d):
    __ref_1k = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'REF':
                            __ref_1k = __loop2200d.get(segment).get(seg).get(s)
                            return __ref_1k


def get_loop2200d_ref_ej(__loop2200d):
    __ref_EJ = {}
    for segment in __loop2200d:
        if segment == '2100D':
            for seg in __loop2200d.get(segment):
                if seg == '2200D':
                    for s in __loop2200d.get(segment).get(seg):
                        if s.split('-')[0] == 'REF':
                            __ref_EJ = __loop2200d.get(segment).get(seg).get(s)
                            return __ref_EJ


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
