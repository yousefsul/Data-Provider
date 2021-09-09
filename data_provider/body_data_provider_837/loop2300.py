def get_clm(__st):
    __clm = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'CLM':
                    __clm = __st.get(segment).get(seg)
                    return __clm


def get_hi(__st):
    __hi = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'HI':
                    __hi = __st.get(segment).get(seg)
                    return __hi


def get_loop2310b_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2310B':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'NM1':
                            __nm1 = __st.get(segment).get(seg).get(s)
                            return __nm1


def get_loop2310b_prv(__st):
    __prv = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2310B':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'PRV':
                            __prv = __st.get(segment).get(seg).get(s)
                            return __prv


def get_loop2310c_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2310C':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'NM1':
                            __nm1 = __st.get(segment).get(seg).get(s)
                            return __nm1


def get_loop2310c_n3(__st):
    __n3 = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2310C':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N3':
                            __n3 = __st.get(segment).get(seg).get(s)
                            return __n3


def get_loop2310c_n4(__st):
    __n4 = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2310C':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N4':
                            __n4 = __st.get(segment).get(seg).get(s)
                            return __n4


def get_loop2400_lx(__st):
    __lx = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2400':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'LX':
                            __lx = __st.get(segment).get(seg).get(s)
                            return __lx


def get_loop2400_sv1(__st):
    __sv1 = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2400':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'SV1':
                            __sv1 = __st.get(segment).get(seg).get(s)
                            return __sv1


def get_loop2400_dtp(__st):
    __dtp = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2400':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'DTP':
                            __dtp = __st.get(segment).get(seg).get(s)
                            return __dtp


def get_loop2400_ref(__st):
    __ref = {}
    for segment in __st:
        if segment == '2300':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2400':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'REF':
                            __ref = __st.get(segment).get(seg).get(s)
                            return __ref
