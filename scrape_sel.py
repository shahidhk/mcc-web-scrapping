import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

colleges = [] 
 
def init_driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
def lookup(driver):
    delay = 60 
    driver.get('http://www.mcc.nic.in/MCCRes/Institute-Profile')
    time.sleep(1)
    links = driver.find_elements_by_xpath("""//*/td[2]/span/a""")
    print len(links)
    global colleges
    counter = 0
    total = len(links)
    for link in links:
        counter+=1
        print "Procession link ", counter, " of ", total, "..." 
        print "Opening ", link.get_attribute('href')
        try:
            link.click()
        except ElementNotVisibleException:
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_Medical"]/div/span[2]""").click()
            link.click()
        time.sleep(2)    
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(5)
        try:
            element_present = EC.presence_of_element_located((By.XPATH, """//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[7]/td[3]/div"""))
            WebDriverWait(driver, delay).until(element_present)
            print "Page is ready!"
            try:
                college = [
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[4]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[2]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[3]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[5]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[6]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[7]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[8]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[9]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[10]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[11]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[12]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[13]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[14]/td[3]/div""").text,
                    driver.find_element_by_xpath("""//*/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[3]/table/tbody/tr[15]/td[3]/div""").text
                ]
                print "Saving ", college[1]
                colleges.append(college)
                write_to_file(college)
            except NoSuchElementException:
                print "Error at ", counter
                pass
            except Exception, e:
                print "Error at ", counter
                pass
        except TimeoutException:
            print "Loading took too much time!"
        driver.close()
        print "closed"
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[0])

def write_to_file(data):
    with open('colleges.csv', 'a') as f:
        f.write((",".join([u'"{0}"'.format(x) for x in data]) + '\n').encode('utf8'))
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()
