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


def crawl_player_salary(href):
    i = requests.get(href, headers=headers)
    j = BeautifulSoup(i.text, 'html.parser')
    try:
        k = j.select_one('.team_data .content .content_a .font')
        m = int(k.select('p')[-2].text.split('：')[-1].split('万')[0])
    except:
        m = 'null'
    return m


def crawl_player(i):
    url = 'https://nba.hupu.com/players/{}'.format(i)
    res = requests.get(url, headers=headers)
    html = BeautifulSoup(res.text, 'html.parser')
    players = html.select('.players_table tr')
    players.remove(players[0])
    for player in players:
        try:
            player = player.select('td')
            player.remove(player[0])

            player_href = player[0].select_one('a')['href']
            print(player[0].select_one('a')['href'])
            player_cn_name = player[0].select_one('a').text.strip()
            print(player[0].select_one('a').text.strip())
            player_en_name = player[0].select_one('p').text.replace('(', '').replace(')', '').strip()
            print(player[0].select_one('p').text.replace('(', '').replace(')', '').strip())
            player_number = player[1].text
            print(player[1].text)
            player_position = player[2].text
            print(player[2].text)
            player_height = float(player[3].text.split('米')[0])
            print(float(player[3].text.split('米')[0]))
            player_weight = int(player[4].text.split('公斤')[0])
            print(int(player[4].text.split('公斤')[0]))
            player_birth = player[5].text
            print(player[5].text)
            player_salary = crawl_player_salary(player[0].select_one('a')['href'])
            print(crawl_player_salary(player[0].select_one('a')['href']))
            writer.writerow(
                [player_cn_name, player_en_name, player_number, player_position, player_height, player_weight,
                 player_birth, player_salary])
            print()
        except:
            continue


if __name__ == '__main__':
    team_lst = get_team()
    file = open('player.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(
        ['player_cn_name', 'player_en_name', 'player_number', 'player_position', 'player_height', 'player_weight',
         'player_birth', 'player_salary'])
    for item in team_lst:
        crawl_player(item)
