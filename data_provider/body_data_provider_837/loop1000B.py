def get_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '1000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __st.get(segment).get(seg)
                    return __nm1
