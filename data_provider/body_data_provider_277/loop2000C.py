def get_hl(__loop2000c):
    __hl = {}
    for segment in __loop2000c:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000c.get(segment)
            return __hl


