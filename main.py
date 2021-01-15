import json
import requests
from bs4 import BeautifulSoup

jsonFile = open("./JSESSIONID.json")

jsonParsed = json.load(jsonFile)

cookies = jsonParsed

htmlRaw = requests.get("https://sms.schoolsoft.se/nti/jsp/student/right_student_schedule.jsp?term=2&requestid=-2", cookies=cookies).text

soup = BeautifulSoup(htmlRaw, features="html5lib")

for a in soup.find_all('a', {'class': 'schedule'}, href=True ):
    """var lesson = 0;
    var week = 0;
    var classId = 0;
    try {
     lesson = $(this).attr('href').match(/lesson\=([0-9]+)/)[1];
    } catch (exc) {}
    try {
        classId = $(this).attr('href').match(/requestid\=([0-9]+)/)[1];
    } catch (exc) {}
    try {
     week = $(this).attr('href').match(/term\=([0-9]+)/)[1];
    } catch (exc) {}"""

    classRequest = requests.get("https://sms.schoolsoft.se/n2ti/jsp/student/" + a.attrs['href'], cookies=cookies).text

    print(classRequest)

    for span in a.find_all('span'):
        # className = str(span)[6:].split("<")[0]
        # classTime = str(span)[6:].split(">")[1]

        

        # print(className + " " + classTime[:-4])

        print()
