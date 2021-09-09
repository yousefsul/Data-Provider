def get_loop2100a_nm1(__loop2100a):
    __nm1 = {}
    print(__loop2100a)
    for segment in __loop2100a:
        if segment == '2100A':
            for seg in __loop2100a.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100a.get(segment).get(seg)
                    return __nm1