def get_loop2100c_nm1(__loop2100c):
    __nm1 = {}
    for segment in __loop2100c:
        if segment == '2100C':
            for seg in __loop2100c.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100c.get(segment).get(seg)
                    return __nm1