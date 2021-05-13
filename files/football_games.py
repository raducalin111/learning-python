import datetime
import csv
from enum import Enum


class GameFilter(Enum):
    APPROVED = 'approved'
    PENDING = 'pending'
    ALL = 'all'


class FootballGame:
    def __init__(self, date, home_team, away_team, home_goals, away_goals):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals

    def get_date(self):
        return self.date

    def __iter__(self):
        return iter([self.date, self.home_team, self.away_team, self.home_goals, self.away_goals])

    def __str__(self) -> str:
        return f'{self.date.isoformat()} {self.home_team} - {self.away_team} {self.home_goals}-{self.away_goals}'


def read_games_from_file(file_name, date: datetime.date = None):
    results = []
    try:
        csv_file = open(file_name, newline='')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            game_date = datetime.date.fromisoformat(line[0])
            if date is None or game_date.__eq__(date):
                results.append(FootballGame(game_date, line[1], line[2], line[3], line[4]))
    except FileNotFoundError:
        print(f'File {file_name} was not found!')
    else:
        return results


def append_to_file(file_name, games):
    with open(file_name, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        for game in games:
            csv_writer.writerow(game)


def write_to_file(file_name, games):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        for game in games:
            csv_writer.writerow(game)


def read_pending_games(date: datetime.date = None) -> list:
    return read_games_from_file('files/pending.csv', date)


def read_approved_games(date: datetime.date = None) -> list:
    return read_games_from_file('files/approved.csv', date)


def read_games(date: datetime.date = None, game_filter: GameFilter = GameFilter.ALL) -> list:
    if game_filter == GameFilter.PENDING:
        return read_pending_games(date)
    elif game_filter == GameFilter.APPROVED:
        return read_approved_games(date)
    else:
        return read_pending_games(date) + read_approved_games(date)


def read_date() -> datetime.date:
    while True:
        try:
            input_date = datetime.date.fromisoformat(input('Enter date in format YYYY-MM-DD: '))
            break
        except ValueError:
            print('Invalid date!')
    return input_date


def read_command():
    input_date = read_date()
    while True:
        option = input("Select what type of games to show\n1. Approved\n2. Pending\n3. All\nSelect: ")
        input_filter = GameFilter.APPROVED if option == '1' else GameFilter.PENDING if option == '2' else GameFilter.ALL if option == '3' else None
        if input_filter is not None:
            break
        else:
            print('Invalid option!')

    game_list = read_games(input_date, input_filter)

    print('The list of games filtered is:')
    for game in game_list:
        print(game)


def approve_command():
    input_date = read_date()
    pending_games = read_pending_games()
    to_remove = []
    for game in pending_games:
        if game.get_date().__eq__(input_date):
            to_remove.append(game)
    still_pending = [i for i in pending_games if i not in to_remove]

    append_to_file('files/approved.csv', to_remove)
    write_to_file('files/pending.csv', still_pending)


approve_command()


