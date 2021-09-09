def get_loop2100b_nm1(__loop2100b):
    __nm1 = {}
    for segment in __loop2100b:
        if segment == '2100B':
            for seg in __loop2100b.get(segment):
                if seg.split('-')[0] == 'NM1':
                    __nm1 = __loop2100b.get(segment).get(seg)
                    return __nm1