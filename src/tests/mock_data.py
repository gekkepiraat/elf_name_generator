"""Mock test data."""
from collections import namedtuple

ElfNameMock = namedtuple('ElfNameMock',
                         'first_part last_part t2_data t3_data')

elf_name1 = ElfNameMock(
    [79, 49],
    [99, [85, 70]],
    {
        79: {
            'She': {
                'suffix': [],
                'meaning': ['age', 'time']}
        },
        99: {
            'Za': {
                'suffix': [],
                'meaning': ['royal']}
        }
    },
    {
        49: {
            'lian': {
                'suffix': ['lia'],
                'meaning': ['master', 'mistress']}
        },
        70: {
            'ro': {
                'suffix': ['ri', 'ron'],
                'meaning': ['walker', 'walks']}
        },
        85: {
            'thus': {
                'suffix': ['thas', 'aethus', 'aethas'],
                'meaning': ['harp', 'harper']}
        }
    },
)


elf_name2 = ElfNameMock(
    [27, 65],
    None,
    {
        27: {
            'Eil': {
                'suffix': [],
                'meaning': ['azure', 'blue']}
        }
    },
    {
        65: {
            'rah': {
                'suffix': ['rae', 'raee'],
                'meaning': ['beast']}
        },
    },
)


def table2_line():
    row1 = '{93} Ty (Try): crystal'
    row2 = '{94} Uth : wizard'
    row3 = '{95} Ver : peace'
    row4 = '{96} Vil : finger, point'
    row5 = '{97} Von : ice'
    row6 = '{98} Ya : bridge, path, way'
    row7 = '{99} Za : royal'
    return list(locals().values())


def table2_parsed_line():
    row1 = {
        'Ty': {
            'meaning': ['crystal'],
            'prefix': ['Try']
        }
    }
    row2 = {
        'Uth': {
            'meaning': ['wizard'],
            'prefix': []
        }
    }
    row3 = {
        'Ver': {
            'meaning': ['peace'],
            'prefix': []
        }
    }
    row4 = {
        'Vil': {
            'meaning': ['finger', 'point'],
            'prefix': []
        }
    }
    row5 = {
        'Von': {
            'meaning': ['ice'],
            'prefix': []
        }
    }
    row6 = {
        'Ya': {
            'meaning': ['bridge', 'path', 'way'],
            'prefix': []
        }
    }
    row7 = {
        'Za': {
            'meaning': ['royal'],
            'prefix': []
        }
    }
    return list(locals().values())


def table3_line():
    row1 = '{70} -ro (-ri; -ron) : walker, walks\n'
    row2 = '{71} -ruil (-aruil; -eruil) : noble\n'
    row3 = '{72} -sal (-isal; -sali) : honey, sweet\n'
    row4 = '{73} -san : drink, wine\n'
    row5 = '{77} -spar : fist\n'
    row6 = '{78} -tae (-itae) : beloved, love\n'
    row7 = '{81} -thal /-tha (-ethal / -etha) : heal, healer, healing'
    return list(locals().values())


def table3_parsed_line():
    row1 = {
        'ro': {
            'meaning': ['walker', 'walks'],
            'suffix': ['ri', 'ron']
        }
    }
    row2 = {
        'ruil': {
            'meaning': ['noble'],
            'suffix': ['aruil', 'eruil']
        }
    }
    row3 = {
        'sal': {
            'meaning': ['honey', 'sweet'],
            'suffix': ['isal', 'sali']
        }
    }
    row4 = {
        'san': {
            'meaning': ['drink', 'wine'],
            'suffix': []
        }
    }
    row5 = {
        'spar': {
            'meaning': ['fist'],
            'suffix': []
        }
    }
    row6 = {
        'tae': {
            'meaning': ['beloved', 'love'],
            'suffix': ['itae']
        }
    }
    row7 = {
        'thal': {
            'meaning': ['heal', 'healer', 'healing'],
            'suffix': ['tha', 'ethal', 'etha']
        }
    }
    return list(locals().values())
