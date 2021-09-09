def get_hl(__st):
    __hl = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'HL':
                    __hl = __st.get(segment).get(seg)
                    return __hl


def get_sbr(__st):
    __sbr = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == 'SBR':
                    __sbr = __st.get(segment).get(seg)
                    return __sbr


def get_loop2010ba_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'NM1':
                            __nm1 = __st.get(segment).get(seg).get(s)
                            return __nm1


def get_loop2010ba_n3(__st):
    __n3 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N3':
                            __n3 = __st.get(segment).get(seg).get(s)
                            return __n3


def get_loop2010ba_n4(__st):
    __n4 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N4':
                            __n4 = __st.get(segment).get(seg).get(s)
                            return __n4


def get_loop2010ba_dmg(__st):
    __dmg = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BA':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'DMG':
                            __dmg = __st.get(segment).get(seg).get(s)
                            return __dmg


def get_loop2010bb_nm1(__st):
    __nm1 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BB':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'NM1':
                            __nm1 = __st.get(segment).get(seg).get(s)
                            return __nm1


def get_loop2010bb_n3(__st):
    __n3 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BB':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N3':
                            __n3 = __st.get(segment).get(seg).get(s)
                            return __n3


def get_loop2010bb_n4(__st):
    __n4 = {}
    for segment in __st:
        if segment == '2000B':
            for seg in __st.get(segment):
                if seg.split('-')[0] == '2010BB':
                    for s in __st.get(segment).get(seg):
                        if s.split('-')[0] == 'N4':
                            __n4 = __st.get(segment).get(seg).get(s)
                            return __n4
