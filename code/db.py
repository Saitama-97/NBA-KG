import csv
from py2neo import Graph, Node, Relationship

graph = Graph('bolt://localhost:7687', username='neo4j', password='root')

file = open('realtion.csv', 'r', encoding='utf-8')
reader = csv.reader(file)
lst = list(reader)
for i in lst:
    print(i)
    str = "match(m:Player),(n:Team) where m.player_cn_name ='{}' and n.team_en_name = '{}' " \
          "create (m)-[r:WorkFor]->(n)".format(i[0], i[2])
    # print(str)
    graph.run(str)
