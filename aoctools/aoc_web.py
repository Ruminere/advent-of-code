import argparse
from datetime import datetime, timezone
import requests
import sys
import time

SESSION = ''

parser = argparse.ArgumentParser(description='Automatically retrieve your Advent of Code input. Supply your own cookie: Inspect Element -> Application -> Cookies -> session')
parser.add_argument('--year', '-y', type=int, default=2024)
parser.add_argument('--day', '-d', type=int, choices=range(1,26), metavar="(1 to 25)", default=datetime.now(timezone.utc).day)
args = parser.parse_args()

def wait_input(year, day):
    '''
    Waits until 00:00:00 EST or later to pull the day's input.
    '''
    early = datetime(year,12,day,4,50,tzinfo=timezone.utc).timestamp()
    goal = datetime(year,12,day,5,tzinfo=timezone.utc).timestamp()
    while True:
        current = datetime.now().timestamp()
        if current < early:
            print(f"You are too early. Run the program at least 10 minutes before {year} day {day} starts.")
            sys.exit()
        if current >= goal:
            return
        time.sleep(0.1)

def get_input(year, day):
    '''
    Retrieves the input.
    '''
    if not SESSION:
        print("You need to include a cookie.")
        sys.exit()
    
    inp = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={'session':SESSION}).text
    inp_fh = open('actual.in', 'w+')
    inp_fh.write(inp)

wait_input(args.year, args.day)
get_input(args.year, args.day)
