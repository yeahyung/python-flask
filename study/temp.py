import sys
import csv

from study.Employee import Employee
from study.SoccerPlayer import SoccerPlayer


## Dictionary
from study.first import first

'''
code = {} # Dictionary
code = {"America": 1, "korea": 82, "Japan": 85}
# code.keys(), code.values(), code.items()
for keys in code.keys():
    print(keys + " : " + str(code[keys]))

# 위에꺼 쉽게할려면 그냥
for keys, values in code.items():
    print(keys + " : " + str(values))
'''

## CSV File
'''
def getKey(item):
    return item[1]


command_data = []

with open("command_data.csv", "r") as csvfile:
    # csv file line 별로 읽고
    fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in fileReader:
        # print(row)
        command_data.append(row)

## csv file 읽고(첫 데이터는 명령어, 두번째는 명령어 실행한 아이디)
## 명령어를 가장 많이 실행한 유저 찾


command_counter = {}
for data in command_data:
    ## 해당 id가 이미 command_counter 에 있으면
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

dictlist = []
for key, value in command_counter.items():
    temp = [key, value]
    dictlist.append(temp)


sorted_dict = sorted(dictlist, key=getKey, reverse=True)
print(sorted_dict[:10])
'''

## List & split & zip
'''
words = 'The quick sadasd my name is '.split()
print(words)
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]
result = [i + j for i in case_1 for j in case_2]
print(result)

## zip => 2개의 list 에서 값을 각각 추출, 3개 이상도 가능
for a, b in zip(case_1, case_2):
    print(a,b)
'''

## Class
'''
park = SoccerPlayer("Park", "MF", 10)
print(park)
print(park.backNumber)

park.change_back_number(12)
print(park.backNumber)

names = ["Jin", "Sungchul", "Ronaldo", "Hong", "Seo"]
positions = ["MF","DF", "CF", "WF", "GK"]
numbers = [10, 15, 20, 3, 1]

players = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(players)
for player in players:
    print(player)
    

temp = first("yes")
# temp.name = "yes"
print(temp.name)
temp.name = "change"
print(temp.name)


me = Employee("yea", 15, "M", 100)
me.about_me()
me.do_work()
'''

## Module & Namespace
from study import converter as cvt
from study.converter import convert_c_to_f

#print("Enter celsius value: ")
#celsius = float(input())
#fahrenheit = cvt.convert_c_to_f(celsius)
#print("converted : " + str(fahrenheit))


'''
import urllib.request
response = urllib.request.urlopen("http://localhost:5000")
print(response.read())
'''



