def get_loop2100d_nm1(__loop2100d):
    __nm1 = {}
    for segment in __loop2100d:
        if segment == '2100D':
            for seg in __loop2100d.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100d.get(segment).get(seg)
                    return __nm1