def get_hl(__loop2000b):
    __hl = {}
    for segment in __loop2000b:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000b.get(segment)
            return __hl


