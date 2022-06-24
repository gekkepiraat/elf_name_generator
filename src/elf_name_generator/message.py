"""Display message of a chosen rule of name generator."""


def display_d10(dice_number: int) -> str:
    """Display sentence of what to do for D10 algorithm.

    E.g.:
        1-4 Roll once on T2 and once on T3.
        5-7 Roll once on T2 and twice on T3.
        8-9 Roll once on T2 and once on T3 for a first name, then once on T2
            and twice on T3 for a second name.
        10 Roll once on Table 3, add an apostrophe, then roll once on Table 2
            and twice on Table 3
    """
    msg = "{prx} once on T2 and {num} on T3{sfx}"
    dn = str(dice_number)
    attrs = dict(prx='Roll', num='once', sfx='.')
    if dn in '1234':
        pass
    elif dn in '567':
        attrs = dict(prx='Roll', num='twice', sfx='.')
    elif dn in '89':
        prx = msg.format(prx='Roll', num='once', sfx=' for a first name, then')
        attrs = dict(prx=prx, num='twice', sfx=' for a second name.')
    elif dn in '10':
        attrs = dict(prx="Roll once on T3, add an apostrophe, then roll",
                     num='twice', sfx='.')

    return msg.format(**attrs)
