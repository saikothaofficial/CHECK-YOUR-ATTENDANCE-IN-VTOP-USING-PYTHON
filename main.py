from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

try:
    d = {}
    with open('details.txt') as f:
        for line in f:
            key,val = line.split()
            d[key] = val



    driver = webdriver.Chrome()
    driver.get('http://vtopcc.vit.ac.in:8080/vtop/initialProcess')

    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/a').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[3]/div/button').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[2]/form/div[1]/input').send_keys(d['username'])
    driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[2]/form/div[2]/input').send_keys(d['password'])



    captcha = input('enter the captcha :')

    driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[2]/form/div[3]/div/div/input').send_keys(captcha)

    driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div[2]/form/div[4]/div[2]/button').click()

    academics = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[2]/aside/section/div/div[4]/a')
    attendance = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[2]/aside/section/div/div[4]/div/div/div/div[2]/div/ul/li[11]/a')

    actions = ActionChains(driver)
    actions.move_to_element(academics)
    actions.click(attendance)
    actions.perform()


    select = Select(driver.find_element_by_id('semesterSubId'))
    select.select_by_value('CH2020211')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/section/div/div/div[2]/form/div[2]/div/button').click()


    table = driver.find_element_by_class_name('table')
    rows = table.find_elements_by_tag_name('tr')

    for i in range(1,len(rows)-1):
        data = rows[i].find_elements_by_tag_name('td')[11].text
        subject = rows[i].find_elements_by_tag_name('td')[2].text
        print(subject,end=' -> ')
        print(data)
        print('-' * 30)



except IndexError:
    print('IndexOutOfBounds')
except NoSuchElementException:
    print('NoSuchElementFound')
