def get_loop2200d_svc(__loop2220d):
    __svc = {}
    for segment in __loop2220d:
        if segment == '2200D':
            for seg in __loop2220d.get(segment):
                if seg == '2220D':
                    for s in __loop2220d.get(segment).get(seg):
                        if s.split('-')[0] == 'SVC':
                            __svc = __loop2220d.get(segment).get(seg).get(s)
                            return __svc


def get_loop2200d_stc(__loop2220d):
    __stc = {}
    for segment in __loop2220d:
        if segment == '2200D':
            for seg in __loop2220d.get(segment):
                if seg == '2220D':
                    for s in __loop2220d.get(segment).get(seg):
                        if s.split('-')[0] == 'STC':
                            __stc = __loop2220d.get(segment).get(seg).get(s)
                            return __stc


def get_loop2200d_dtp(__loop2220d):
    __dtp = {}
    for segment in __loop2220d:
        if segment == '2200D':
            for seg in __loop2220d.get(segment):
                if seg == '2220D':
                    for s in __loop2220d.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __dtp = __loop2220d.get(segment).get(seg).get(s)
                            return __dtp