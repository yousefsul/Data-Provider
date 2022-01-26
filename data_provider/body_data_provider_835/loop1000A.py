def get_n1(__st):
    __n1 = {}
    for segment in __st:
        if segment == '1000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'N1':
                    __n1 = __st.get(segment).get(seg)
                    return __n1


def get_per(__st):
    __per = {}
    for segment in __st:
        if segment == '1000A':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'PER':
                    __per = __st.get(segment).get(seg)
                    return __per

