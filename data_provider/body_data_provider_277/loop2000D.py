def get_hl(__loop2000d):
    __hl = {}
    for segment in __loop2000d:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000d.get(segment)
            return __hl
