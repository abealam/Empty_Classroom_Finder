from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://csprd-web.psg.umbc.edu/psc/ps/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?')

checkboxes = driver.find_elements(By.TAG_NAME, "span")
for checkbox in checkboxes:
    if checkbox.text == "Show Open Classes Only":
        checkbox.click()

button = driver.find_elements(By.TAG_NAME, "button")

# if needed, add main campus filter to lessen load

for b in button:
    if b.text == "Search":
        b.click()

time.sleep(3)

# scrolling (needs to be tested)
count = 0
while count != 200:
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    count += 1
    if count % 11 == 0:
        time.sleep(5)


link = driver.find_elements(By.CLASS_NAME, "sr-only")
link = link[3:]

blankList = []


# blankList contains indexes of lines that are just "blank" spaces since "Actions" is the last text in the
# webscraping of each class
for i in range(len(link)):
    if link[i].text == "Actions":
        blankList.append(i+1)

# this bit of code creates a list of lists, where the sublists contain all of the sections for one class
allClasses = []
sectionsOfClass = []

for i in range(len(link)):
    if i in blankList:
        allClasses.append(sectionsOfClass)
        sectionsOfClass = []
    else:
        sectionsOfClass.append(link[i].text)

# to store needed data about class times in one list "bigList"
bigList = []
for sections in allClasses:
    for index in range(len(sections)):
        if index % 9 == 2 and sections[index] != "-":
            bigList.append(sections[index])
        if index % 9 == 3 and sections[index] != "-":
            bigList.append(sections[index])
        if index % 9 == 4 and sections[index] != "-":
            bigList.append(sections[index])
        if index % 9 == 5 and sections[index] != "-":
            bigList.append(sections[index])

        if index % 9 == 0 and index > 2:
            bigList.append("new entry")


# creating "newEntryList" to find places to splice data
newEntryList = []
for e in range(len(bigList)):
    if bigList[e] == "new entry":
        newEntryList.append(e)


# cleaning up data -- removing "WEB" classes and weird data like start/end at the same time
a = []
b = []

for i in range(len(bigList)):
    if i in newEntryList:
        if len(b) == 4:
            if b[3] != "WEB" and len(b[2]) <= 8:
                a.append(b)
                b = []
            else:
                b = []
        else:
            b = []
    else:
        b.append(bigList[i])


def militaryTime(str):
    newStr = []
    for char in str[0:-2]:
        if char != ":":
            newStr.append(char)

    return int("".join(newStr))


# reformatting for database
for line in a:
    for x in range(len(line)):
        # following chunk reformats days to numbers
        if line[x] == "Monday":
            line[x] = "2"
        if line[x] == "Tuesday":
            line[x] = "3"
        if line[x] == "Wednesday":
            line[x] = "4"
        if line[x] == "Thursday":
            line[x] = "5"
        if line[x] == "Friday":
            line[x] = "6"
        if line[x] == "Monday Wednesday":
            line[x] = "2, 4"
        if line[x] == "Tuesday Thursday":
            line[x] = "3, 5"
        if line[x] == "Monday Wednesday Friday":
            line[x] = "2, 4, 6"

        # time reformatting needed here
        print(line)
        if x % 4 == 1 and len(line[x]) > 1:
            startTime = line[x]
            pmCheck = startTime[-2] + startTime[-1]
            startTimeInt = militaryTime(startTime)

            if pmCheck == "pm" and startTimeInt > 100:
                startTimeInt += 1200

            line[x] = str(startTimeInt)

        if x % 4 == 2 and len(line[x]) > 1:
            pmCheck = line[x][-2] + line[x][-1]
            endTimeInt = militaryTime(line[x])

            if pmCheck == "pm" and endTimeInt > 100:
                endTimeInt += 1200

            line[x] = str(endTimeInt)


try:
    with open('mysite/main/static/test.txt', 'w') as file:
        for line in a:
            for x in line:
                file.write(f'{x}, ')
            file.write("\n")
except FileNotFoundError:
    print("The file was not created.")


# output below
# ['3, 5', '1300', '1415', 'Fine Arts 015']
# ['2, 4', '1430', '1545', 'Fine Arts 303']
# ['2, 4', '1300', '1415', 'Fine Arts 001']
# ['3, 5', '1000', '1115', 'Information Technology 456']
# ['3, 5', '1000', '1115', 'Janet & Walter Sondheim 203']
# ['3, 5', '1300', '1415', 'Fine Arts 006']
# ['3', '1630', '1900', 'Fine Arts 015']
# ['2, 4', '1430', '1545', 'Sherman Hall 151']
# ['3, 5', '1700', '1815', 'Fine Arts 018']
# ['2, 4', '1500', '1615', 'Fine Arts 559']
# ['5', '1600', '1830', 'Fine Arts 424']
# ['2, 4', '1430', '1545', 'Fine Arts 427']
# ['2, 4', '1600', '1715', 'Fine Arts 427']
# ['2, 4', '1300', '1415', 'Fine Arts 306']
# ['4', '1630', '1900', 'Math & Psychology 106']
# ['3, 5', '1300', '1415', 'Physics 201']
# ['4', '1630', '1900', 'Fine Arts 001']
# ['3, 5', '1000', '1115', 'Math & Psychology 101']
# ['2, 4', '1000', '1115', 'Performing Arts & Humani 107']
# ['2, 4', '1000', '1115', 'Interdisciplinary Life S 237']
# ['2, 4', '1130', '2445', 'Interdisciplinary Life S 237']
# ['3, 5', '1000', '1115', 'Performing Arts & Humani 108']
# ['3, 5', '1300', '1415', 'Performing Arts & Humani 108']
# ['3, 5', '1130', '2445', 'Fine Arts 559']
# ['3', '1630', '1900', 'Performing Arts & Humani 107']
# ['4', '1300', '1530', 'Shady Grove Building III 3219']
# ['2, 4', '1000', '1115', 'Performing Arts & Humani 108']
# ['3, 5', '1300', '1415', 'Janet & Walter Sondheim 101']
# ['2', '1430', '1700', 'Fine Arts 558']
# ['2', '1430', '1700', 'Fine Arts 558']
# ['3, 5', '1430', '1545', 'Information Technology 231']
# ['4', '1430', '1545', 'Sherman Hall 145']
# ['3, 5', '1430', '1545', 'Information Technology 231']
# ['5', '1600', '1715', 'Engineering 027']
# ['4', '1600', '1715', 'Physics 101']
# ['3, 5', '1300', '1415', 'Biological Sciences 120']
# ['3, 5', '1130', '2445', 'Fine Arts 011']

driver.quit()