
import urllib.request

import requests
from bs4 import BeautifulSoup
import lxml
import selenium
from selenium import webdriver
from pyvirtualdisplay import Display
import time
import threading

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

print("Start Program")
#t = urllib.request.urlopen("http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action")
#print(t)
#a = urllib.request.urlopen("http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action")
#print(a.read().decode("utf-8"))


SY_URL = "http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action"
DATA1 ={'search_subj_class_cde':'CLTR086001'}
SU_URL = 'http://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action'
DATA2 = {'user.stu_nbr':'','user.usr_id':'','user.passwd':''}
"""
session = requests.Session()
html1 = session.post(url=SY_URL, data=DATA1)
#html2 = get_html(SU_URL)
soup1 = BeautifulSoup(html1.text, 'html.parser')
#soup2 = BeautifulSoup(html2, 'html.parser')
result1 = soup1.find('table', {'class':'resultT form'}).find('td', {'class':'lect_req_cnt'})
"""
#===============================================
"""
session = requests.Session()
r = session.get(SY_URL)

#print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
lecture_code_url = soup.find('table', class_='search form').find('td', id='search_subj_class_code')
sess_result = session.post(SY_URL, data=DATA1, headers=dict(referer=SY_URL))

#R = session.post(lecture_code_url, data=DATA1)
"""
#===============================================
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver2 = webdriver.Chrome(executable_path="D:\Programs\chromedriver.exe",chrome_options=chrome_options)
driver2.get('http://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action')
"""
driver = webdriver.Chrome(executable_path="D:\Programs\chromedriver.exe")
driver.get(SY_URL)
elem = driver.find_element_by_id(id_='search_subj_class_cde')
elem.send_keys("CLTR086001")
#driver.switch_to.frame("")

#display = Display(visible=0, size=(800, 600))
#display.start()

while True :
   elem = driver.find_element_by_tag_name(name='button')
   elem.click()
   #count = driver.find_element_by_class_name("lect_req_cnt")
   soup = BeautifulSoup(driver.page_source, 'html.parser')
   result1 = soup.find('table', {'class':'resultT form'}).find('td', {'class':'lect_req_cnt'})
   if int(result1.text) < 200 :
      break
   time.sleep(0.7)
"""
snum = YOUR_STUDENT_NUMBER
id = YOUR_ID
pswd = YOUR_PASSWORD

elem_snum = driver2.find_element_by_id(id_='user.stu_nbr')
elem_id = driver2.find_element_by_id(id_='user.usr_id')
elem_pswd = driver2.find_element_by_id(id_='user.passwd')

elem_login = driver2.find_element_by_class_name(name='login')

elem_snum.send_keys(snum)
elem_id.send_keys(id)
elem_pswd.send_keys(pswd)

elem_login.click()


#elem_time = driver2.find_element_by_id(id_='timeStatus')
#elem_result = driver2.find_element_by_class_name(name='lect_req_cnt')
elem_logout = driver2.find_element_by_class_name(name='stop')
elem_do = driver2.find_element_by_link_text(link_text='신청')

timer = 0
def counter() :
   global timer
   timer = timer + 1
   threading.Timer(1, counter).start()

counter()
while True :
   #relogin
   if timer > 1000 :
      elem_logout.click()
      elem_snum = driver2.find_element_by_id(id_='user.stu_nbr')
      elem_id = driver2.find_element_by_id(id_='user.usr_id')
      elem_pswd = driver2.find_element_by_id(id_='user.passwd')
      elem_login = driver2.find_element_by_class_name(name='login')
      elem_snum.send_keys(snum)
      elem_id.send_keys(id)
      elem_pswd.send_keys(pswd)
      elem_login.click()
      time.sleep(0.3)
      elem_logout = driver2.find_element_by_class_name(name='stop')
      elem_do = driver2.find_element_by_link_text(link_text='신청')
      print('relogin success')
      timer = 0

   print(timer)
   soup = BeautifulSoup(driver2.page_source, 'html.parser')
   current_count = soup.find('tr', {'id': 'lectPackReqGrid_0'}).find('td', {'class': 'lect_req_cnt'})

   if int(current_count.text) < 200 :
      elem_do.click()
      break
   time.sleep(0.5)

#print(r.text)
#soup = BeautifulSoup(r.text, 'html.parser')
#lecture_code_url = soup.find('table', class_='search form').find('td', id='search_subj_class_code')
#sess_result = session.post(SY_URL, data=DATA1, headers=dict(referer=SY_URL))

#R = session.post(lecture_code_url, data=DATA1)

#driver2 = webdriver.Chrome(executable_path="D:\Programs\chromedriver.exe")
#driver2.get(SU_URL)
#elem = driver2.find_element_by_id()

print("End Program")

#driver.quit()
#display.stop()
