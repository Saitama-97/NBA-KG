import requests
import time
import csv
from bs4 import BeautifulSoup


headers = {
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.122 Safari/537.36 '
}

file = open('team.csv', 'w', encoding='utf-8')
header = ['team_cn_name', 'city', 'team_en_name', 'enterTime', 'homeland', 'division', 'coach', 'website']
writer = csv.DictWriter(file, header)
writer.writeheader()


def crawl_team_info(ref):
    item1 = requests.get(url=ref, headers=headers)
    item2 = BeautifulSoup(item1.text, 'html.parser')
    item3 = item2.select_one('.content_a').select_one('.font').select('p')
    # 球队英文名
    team_en_name = item2.select_one('.team_data .title-text').text.strip().split('（')[1].split(' ')[1].replace('）', '')
    # 球队所在城市
    city = item2.select_one('.team_data .title-text').text.strip().split('（')[1].split(' ')[0]
    # 进入联盟时间
    enterTime = item3[0].text.strip().split('：')[1]
    # 主场
    homeland = item3[1].text.strip().split("\xa0")[0].split('：')[1]
    # 赛区
    division = item3[1].text.strip().split("\xa0")[1].split('：')[1]
    # 官网
    website = item3[2].select_one('a').text.strip()
    # 主教练
    coach = item3[3].text.strip().split('：')[1]

    print('team_en_name', team_en_name)
    print('city', city)
    print('enterTime', enterTime)
    print('homeland', homeland)
    print('division', division)
    print('website', website)
    print('coach', coach)

    return team_en_name, city, enterTime, homeland, division, website, coach


def crawl_team():
    url = 'https://nba.hupu.com/teams'
    item1 = requests.get(url, headers=headers)
    item2 = BeautifulSoup(item1.text, 'html.parser')
    teams = item2.select('.a_teamlink')

    for team in teams:
        print('team_cn_name', team.select_one('h2').text.strip())
        # 球队中文名
        team_cn_name = team.select_one('h2').text.strip()
        print('ref', team['href'].strip())
        ref = team['href'].strip()
        team_en_name, city, enterTime, homeland, division, website, coach = crawl_team_info(team['href'].strip())
        writer.writerow({'team_cn_name': team_cn_name,
                         'city': city,
                         'team_en_name': team_en_name,
                         'enterTime': enterTime,
                         'homeland': homeland,
                         'division': division,
                         'coach': coach,
                         'website': website
                         })
        print()


if __name__ == '__main__':
    crawl_team()
