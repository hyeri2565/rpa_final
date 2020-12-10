import pyautogui as gui
import pyperclip as clip
import pygetwindow as win
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def copy(img):
    location=gui.locateOnScreen(img)
    center=gui.center(location)
    return center

print(copy('contents003.png'))
gui.click(copy('contents003.png').x+400,copy('contents003.png').y)
gui.hotkey('ctrl','a')
gui.hotkey('ctrl','c')
Win=win.getWindowsWithTitle('PyCharm')[0]
Win.activate()
data_origin=clip.paste()

#데이터 정규화 시작
print(data_origin)

fix_fax = ['02-2689-8664', '02-3666-0647', '02-3666-0953', '02-4062-0355', '02-2066-0909', '02-3666-9714']
data_integration = data_origin.replace(' ', '')
print(data_integration)
count1 = 1
fax_list = []
customer_num = []
cus_name = ''
hash_fax = {'1구역': fix_fax[0], '2구역': fix_fax[3], '4구역': fix_fax[1], '5구역': fix_fax[4], '8,9구역': fix_fax[2],
            '10구역': fix_fax[5]}
print(hash_fax)
id_num = ''

for i in hash_fax:
    if data_integration.find(i) != -1:
        fax_list.append(data_integration[data_integration.find(i):len(i)])
        break
print("팩스번호:", hash_fax[fax_list[0]])
# 팩스 번호를 구하고 난뒤에 팩스리스트가 비어있지않다면 고객번호로 추정한 후 추출
if len(fax_list) != 0:
    regex = re.compile(r'02-\d\d\d\d-\d\d\d\d')
    customer_num = regex.findall(data_integration)

print("고객번호:", customer_num)

# 신청자 이름찾기
str_list = []
data_split = data_integration.split('/')
print(data_split)

remove_rule = '^[0-9]'
for split in range(len(data_split)):
    # 숫자로 시작하는 리스트 요소 제거하기 위한 정규표현식
    find_num = re.findall(remove_rule, data_split[split])
    if len(find_num) == 0:  # 숫자로 시작하지 않는 요소만 str_list에 붙여넣기
        str_list.append(data_split[split])
print(str_list)
for st3 in str_list:
    if len(st3) == 3:
        cus_name += st3
print("신청자 이름:", cus_name)

# 주민번호찾기
data_split2 = data_split.copy()
for split in data_split:
    for_split_index = data_split.index(split)
    for num in customer_num:  # 고객번호를 출력해서 해당하는 번호가 있으면 제거하라는 알고리즘
        if split.find(num) != -1:
            s_index = split.find(num)
            e_index = s_index + 12

            data_split2[for_split_index] = split.replace(split[s_index:e_index], '')

            split = data_split2[for_split_index]
# print(data_split2)  <- 주민등록번호 추출을 위해 옆에 붙은 고객번호 삭제된 리스트

# data_split2에서 주민번호 옆에 붙은 내방을 빼고 가져오기 위해 데이터정규 표현식 이용
for split2 in data_split2:
    id_rule = '\d{13}'

    id = re.findall(id_rule, split2)
    if len(id) != 0:  # findall로 찾은 값도 리스트로 반환
        print(id)
        id_num = id[0][:6] + '-' + id[0][6:]
print("주민등록번호:", id_num)


#데이터 정규화 완료
driver = webdriver.Chrome()
ur1 = "http://127.0.0.1:8000/Kepco_RPA/step1/"
driver.get(ur1)
action = ActionChains(driver)

driver.find_element_by_css_selector('input#cusnum').click()
time.sleep(1)
action.send_keys(customer_num[0]).perform()
time.sleep(1)
driver.find_element_by_css_selector('input#print2').click()
time.sleep(1)


ur2 = "http://127.0.0.1:8000/Kepco_RPA/step2/"
driver.get(ur2)
action = ActionChains(driver)
driver.maximize_window()

driver.find_element_by_css_selector('input#cusnum.cusnum').click()
(action.send_keys(customer_num[0]).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).
 key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).
 key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).
 key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).
 send_keys(cus_name).key_down(Keys.TAB).key_down(Keys.TAB).send_keys(id_num).perform())


# .pause(1).key_down(Keys.TAB).key_down(Keys.TAB).send_keys(id_num[0])
# .perform())

#신청인 정보 버튼 클릭 매크로 3단계
Win=win.getWindowsWithTitle('PyCharm')[0]
Win.activate()

a=gui.locateOnScreen('combo1.png')
center1=gui.center(a)
print(center1)
gui.click(center1.x-89,center1.y)

Win=win.getWindowsWithTitle('PyCharm')[0]
Win.activate()

b=gui.locateOnScreen('combo2.png')
center2=gui.center(b)
print(center2)
gui.click(center2.x-119,center2.y)

Win=win.getWindowsWithTitle('PyCharm')[0]
Win.activate()

c=gui.locateOnScreen('print.png')
center3=gui.center(c)
print(center3)
gui.doubleClick(center3)




