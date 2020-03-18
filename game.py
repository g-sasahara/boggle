import argparse
import random
import sys
import time

"""
Set up dice and field
"""
dice = {'de':
            [tuple('ABTIRL'), tuple('NETGIV'), tuple('NOTKUE'), tuple('LETSUP'),
             tuple('AOETAI'), tuple('GUNLEY'), tuple('ADZVEN'), tuple('NESHIR'),
             tuple('SERCAL'), tuple('LEUWIR'), tuple('BAMQOJ'), tuple('PEMDAC'),
             tuple('TENDOS'), tuple('MAISOR'), tuple('FIEHES'), tuple('FOARIX')],
        'en':
            [tuple('AACIOT'), tuple('ABILTY'), tuple('ACDEMP'), tuple('ACELRS'),
             tuple('ADENVZ'), tuple('AHMORS'), tuple('BIFORX'), tuple('DENOSW'),
             tuple('DKNOTU'), tuple('EEFHIY'), tuple('EGKLUY'), tuple('EGINTV'),
             tuple('EHINPS'), tuple('ELPSTU'), tuple('GILRUW'), ('A', 'B', 'J', 'M', 'O', 'Qu')]
        }
size = {'width': 4, 'height': 4}


def throw_dice(seed, lang):
    """
    Generates playing field
    """
    if seed:
        random.seed(seed)
    # Side of each die
    sides = [random.randint(0, 5) for i in range(len(dice[lang]))]
    # Pick letters according to dice sides
    letters = [dice[lang][i][sides[i]] for i in range(len(dice[lang]))]
    # Permutation of dice
    random.shuffle(letters)
    return letters


def print_field(letters):
    print('\n')
    for i in range(len(letters)):
        if i % size['width'] == 0:
            print('\t', end="")
        if i % size['width'] == 3:
            end = '\n'
        else:
            end = '  '
        print(letters[i], end=end)


def countdown(t):
    print('')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('\r' + timeformat, end='')
        time.sleep(1)
        t -= 1
    print('\rTime up!')


def parse_args():
    parser = argparse.ArgumentParser(description='Boggle game.')
    parser.add_argument('-s', metavar='seed', help='Seed for random generation of board')
    parser.add_argument('-d', metavar='duration', default=180, help='Duration of the game in seconds (default: 180)')
    parser.add_argument('-l', metavar='language', default='de', help='Language: \'de\' or \'en\' (default: \'de\')')
    return parser.parse_args()

"""
Run the game
"""
args = parse_args()
current_seed = int(args.s) if args.s is not None else None
duration = int(args.d)
language = args.l
print_field(throw_dice(current_seed, language))
countdown(duration)
