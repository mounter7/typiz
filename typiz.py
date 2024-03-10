import argparse
import time

import pyautogui as p

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--msg', help='The message that you want to displayed.')
parser.add_argument('-v', '--version', action='store_true', help='The version.')
parser.add_argument('-n', '--numbers', type=int, help='The number of times to be displayed the message.')
parser.add_argument('-t', '--times', type=int, help='Delay time in seconds.')
parser.add_argument('--debug', action='store_true', help='Enable debug mode.')

args = parser.parse_args()

if args.debug:
    start = time.perf_counter()

if args.msg:
    n = args.numbers
    t = args.times
    time.sleep(t)
    for i in range(0, n, 1):
        p.write(f'{args.msg}')
        p.press('enter')  # Press enter after the text is written

# if args.numbers is not None:
#     print(sum(args.numbers))

# if args.times is not None:
#     print(sum(args.times))



if args.version:
    print('Typiz')
    print('Version: 1.0')
    print('Created by Ravindu Madhushankha.\n')

if args.debug:
    end = time.perf_counter()
    print(f'\n{end - start}')
