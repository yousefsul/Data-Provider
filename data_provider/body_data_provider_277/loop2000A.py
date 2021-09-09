def get_hl(__loop2000a):
    __hl = {}
    for segment in __loop2000a:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000a.get(segment)
            return __hl


