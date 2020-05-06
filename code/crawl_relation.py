import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.122 Safari/537.36 '
}


def get_team():
    team_file = open('team.csv', 'r', encoding='utf-8')
    next(team_file)
    reader = csv.reader(team_file)
    reader = list(reader)
    # team_lst
    team_lst = []
    for item in reader:
        team_lst.append(item[2])
    team_file.close()
    return team_lst


def crawl_player(i):
    player_lst = []
    url = 'https://nba.hupu.com/players/{}'.format(i)
    res = requests.get(url, headers=headers)
    html = BeautifulSoup(res.text, 'html.parser')
    players = html.select('.players_table tr')
    players.remove(players[0])
    for player in players:
        try:
            player = player.select('td')
            player.remove(player[0])
            player_cn_name = player[0].select_one('a').text.strip()
            print(player[0].select_one('a').text.strip())
            player_lst.append(player_cn_name)
        except:
            continue
    return player_lst


if __name__ == '__main__':
    file = open('realtion.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['player_cn_name', 'Relation', 'team_en_name'])
    team_lst = get_team()
    for team in team_lst:
        print("Team", team)
        lst = crawl_player(team)
        for item in lst:
            writer.writerow([item, 'WorkFor', team])
        print()
