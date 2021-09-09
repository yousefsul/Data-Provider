def get_loop2000d_hl(__loop2000d):
    __hl = {}
    for segment in __loop2000d:
        if segment.split('-')[0] == 'HL':
            __hl = __loop2000d.get(segment)
            return __hl

def get_loop2000d_dmg(__loop2000d):
    __dmg = {}
    for segment in __loop2000d:
        if segment.split('-')[0] == 'DMG':
            __dmg = __loop2000d.get(segment)
            return __dmg



