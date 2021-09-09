def get_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '1000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __st.get(segment).get(seg)
                    return __nm1


def get_per(__st):
    __per = {}
    for segment in __st:
        if segment == '1000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'PER':
                    __per = __st.get(segment).get(seg)
                    return __per

