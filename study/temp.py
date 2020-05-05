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

# print("Enter celsius value: ")
# celsius = float(input())
# fahrenheit = cvt.convert_c_to_f(celsius)
# print("converted : " + str(fahrenheit))


'''
import urllib.request
response = urllib.request.urlopen("http://localhost:5000")
print(response.read())
'''

'''
# exception
for i in range(10):
    try:
        result = 10 / i
    except Exception:
        print("divided by zero")
    # exception 이 일어나지 않으면 -> 정상 실행되면
    else:
        print(10 / i)
'''

'''
# file
import os

print(os.getcwd())
f = open("temp.txt", "a") # w대신 a로 하면 맨 뒤에 추가
f.write("Life is short?")
f.close()


# directory 확인 후 만들기
if not os.path.isdir("study"):
    os.mkdir("study")
else:
    print("already exists")

with open("mainController.py", "r") as file:
    # content = file.readlines()
    # print(content)

    
    i = 0
    while 1:
        line = file.readline().replace("\n", "")
        if line.strip() == "":
            continue
        if not line:
            break
        print(str(i) + " === " + line)
        i += 1
    

    content = file.read()
    word_list = content.split(" ")
    line_list = content.split("\n")

    print(word_list)
    print(line_list)
'''

'''
# logging
import logging
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
'''

'''
# csv file

line_counter = 0
data_header = []
customer_list = []

with open("study/customers.csv") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0:  # 첫 줄 = 해더
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))
        line_counter += 1
print("Header:\t ", data_header)
for data in customer_list:
    print("Data:\t", data)
print(len(customer_list))

with open("customer_custom.csv", "w") as customer_custom:
    customer_custom.write(",".join(data_header).strip('\n')+"\n")
    for data in customer_list:
        customer_custom.write(",".join(data).strip('\n')+"\n")
'''


'''
# 정규식 https://regexr.com
import re
import urllib.request


message = "AAabcdefg word check"
# [abc] -> a, b, c 중 하나가 있다.    [a-z] -> a~z까지 중 하나가 있다.
result = re.findall(r"[a-z]", message)
resulttemp = re.findall(r"\w", message)
print(resulttemp)
print(result)

#url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"
#html = urllib.request.urlopen(url)
#html_contents = str(html.read().decode("utf8"))

#url_list = re.findall(r"(http)(.+)(zip)", html_contents)
#for url in url_list:
#    #print(url)
#    print("".join(url))

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]
samsung_index = samsung_stock[1]
#print(samsung_stock)
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
'''


# JSON
import json


with open("study/json_example.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["employees"])
    for employee in json_data["employees"]:
        print(employee)

dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_data)

with open("study/data.json", "w") as file:
    json.dump(dict_data, file)