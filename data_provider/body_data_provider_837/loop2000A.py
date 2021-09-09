def get_hl(__st):
    __hl = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'HL':
                    __hl = __st.get(segment).get(seg)
                    return __hl


def get_loop2010aa_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010AA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'NM1':
                            __nm1 = __st.get(segment).get(seg).get(s)
                            return __nm1


def get_loop2010aa_n3(__st):
    __n3 = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010AA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N3':
                            __n3 = __st.get(segment).get(seg).get(s)
                            return __n3


def get_loop2010aa_n4(__st):
    __n4 = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010AA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N4':
                            __n4 = __st.get(segment).get(seg).get(s)
                            return __n4


def get_loop2010aa_ref(__st):
    __ref = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010AA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'REF':
                            __ref = __st.get(segment).get(seg).get(s)
                            return __ref


def get_loop2010aa_per(__st):
    __per = {}
    for segment in __st:
        if segment == '2000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010AA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'PER':
                            __per = __st.get(segment).get(seg).get(s)
                            return __per

