import browser_cookie3
from datetime import datetime, timedelta, timezone
import json
import pathlib
import pytz
import requests


def download_leaderboard(url, filename):
    cookies = browser_cookie3.chrome(domain_name='.adventofcode.com')
    response = requests.get(url, cookies=cookies)

    with open(filename, mode='w') as f:
        f.write(response.text)


def display_leaderboard(filename):
    rank_width = 6
    name_width = 20
    elapsed_width = 20
    interval_width = 20
    leader_width = 20

    col_format = f'{{:<{rank_width}}}{{:<{name_width}}}{{:>{elapsed_width}}}{{:>{interval_width}}}{{:>{leader_width}}}'

    with open(filename) as f:
        leaderboard = json.load(f)

        for day_int in range(1, 26):
            for star_int in range(1, 3):
                member_list = []
                day = str(day_int)
                star = str(star_int)

                for _, member in leaderboard['members'].items():
                    if day in member['completion_day_level'] and star in member['completion_day_level'][day]:
                        member_list.append((int(member['completion_day_level'][day][star]['get_star_ts']), member['name']))

                if not member_list:
                    continue

                member_list.sort()
                eastern_timezone = pytz.timezone('us/eastern')
                start_time = eastern_timezone.localize(datetime(2021, 12, day_int))
                leader_time = prev_time = datetime.fromtimestamp(member_list[0][0], timezone.utc).astimezone(eastern_timezone)

                print(f'Day {day}, Star {star}')
                print(col_format.format('Place', 'Name', 'Elapsed', 'Interval', 'Leader'))

                for i in range(len(member_list)):
                    my_time = datetime.fromtimestamp(member_list[i][0], timezone.utc).astimezone(eastern_timezone)
                    cols = [
                        str(i + 1),
                        member_list[i][1],
                        str(my_time - start_time),
                        str(my_time - prev_time),
                        str(my_time - leader_time),
                    ]
                    prev_time = my_time

                    print(col_format.format(*cols))
                print()


if __name__ == '__main__':
    saved_leaderboard_path = ''  # where should we save the downloaded leaderboard JSON?
    url = ''  # URL of the leaderboard JSON

    p = pathlib.Path(saved_leaderboard_path)
    if not p.exists() or datetime.fromtimestamp(p.stat().st_mtime) < datetime.now() - timedelta(minutes=16):
        download_leaderboard(url, saved_leaderboard_path)
    display_leaderboard(saved_leaderboard_path)
