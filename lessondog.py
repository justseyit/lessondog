from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import asyncio
import time

class Lesson:
    def __init__(self, lessonName, lessonDate, lessonLink, lessonTime, lessonLecturer):
        self.lessonName = lessonName
        self.lessonDate = lessonDate
        self.lessonLink = lessonLink
        self.lessonTime = lessonTime
        self.lessonLecturer = lessonLecturer
    
    def showInfo(self):
        print('Lesson Name: '+ str(self.lessonName))
        print('Lesson Date: '+ str(self.lessonDate))
        print('Lesson Time: '+ str(self.lessonTime))
        print('Lesson Link: '+ str(self.lessonLink))
        print('Lesson Lecturer: '+ str(self.lessonLecturer))
        print(' ')
        print(' ')


lessons=[]

print('Welcome to LessonDog!')
print('Enter how many lessons you have: ', end='')
lessonsAmount= int(input())
driver = webdriver.Chrome('./chromedriver.exe')
usernameStr = 'username'
passwordStr = 'password'
driver.get(('http://193.255.242.2/'))
username = driver.find_element_by_id('ctl02_ASPxTextBox1_I')
username.send_keys(usernameStr)
password = driver.find_element_by_id('ctl02_ASPxTextBox2_I')
password.send_keys(passwordStr)
loginButton = driver.find_element_by_id('ctl02_ctl06_CD')
loginButton.click()
activeLessons=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'ASPxSplitter1_ASPxRibbon2_T2G0I1_LI')))
activeLessons=driver.find_element_by_id('ASPxSplitter1_ASPxRibbon2_T2G0I1_LI')
activeLessons.click()
frame = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'ASPxSplitter1_1_CC')))
frame = driver.find_element_by_id('ASPxSplitter1_1_CC')
driver.switch_to.frame(frame)
frame = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'ASPxSplitter1_1_CC')))

def GetLessonInfo():
    for i in range(lessonsAmount):

        idlesson=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'ASPxSplitter1_aspmenu_DXI'+str(i)+'_T')))
        idlesson='ASPxSplitter1_aspmenu_DXI'+str(i)+'_T'
        clickLesson=driver.find_element_by_id(idlesson)
        clickLesson.click()
        time.sleep(2)

        try:
            checkLesson=driver.find_element_by_id("ASPxSplitter1_ASPxCardView1_DXEmptyCard")
            print('Current lesson has no data. Skipping...')
        except selenium.common.exceptions.NoSuchElementException:
            try:
                print('-Start of lesson data-')
                lessonNameElement=driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[3]/td[2]')
                lessonName = lessonNameElement[0].text
                print(lessonName)
                lessonDateElement=driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[2]')
                lessonDate = lessonDateElement[0].text
                lessondate = re.findall(r"[\d]{1,2}.[\d]{1,2}.[\d]{4}", lessonDate)[0]
                print(str(lessondate))
                lessonLinkElement=driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[6]/td[2]')
                lessonLink = lessonLinkElement[0].text
                print(lessonLink)
                lessonTimeElement=driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[2]')
                lessonTime = lessonTimeElement[0].text
                lessontime = re.findall(r"(?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$", lessonTime)[0]
                lessontime = str(lessontime).replace('(', '')
                lessontime = lessontime.replace(')', '')
                lessontime = lessontime.replace("'", '')
                lessontime = lessontime.replace(',', ':')
                lessontime = lessontime.replace(' ', '')
                print(str(lessontime))
                lessonLecturerElement=driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[3]')
                lessonLecturer = lessonLecturerElement[0].text
                print(lessonLecturer)
                lesson = Lesson(lessonName, lessondate, lessonLink, lessontime, lessonLecturer)
                lessons.append(lesson)
                print('-End of lesson data-')
            except Exception as ex:
                print('An unknown error occoured. Skipping...')


GetLessonInfo()


    

print('Lessons:')
for lesson in lessons:
    lesson.showInfo()