from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from database import answer_database

# Network Latency
LATENCY = 3

# Get driver
def init_driver():
    driver = webdriver.Chrome("./chromedriver")
    print("[+] Loaded Chrome webdriver")
    return driver

def enter_education(driver, ID, PW):
    # Log in portal
    print("[*] Logging in portal... ", end='')
    driver.get("https://portal.korea.ac.kr")
    driver.find_element_by_name("id").send_keys(ID)
    driver.find_element_by_name("pw").send_keys(PW)
    driver.find_element_by_xpath("//*[@id=\"loginform\"]/input").click()
    print("Done.")

    # Enter education
    print("[*] Accessing education page... ", end='') 
    sleep(LATENCY)
    driver.execute_script("moveComponent('http://infodepot.korea.ac.kr', '2', '/common/FMSLogin3.jsp', '86', '3000', 'S')")

    # Switch to new tab
    sleep(LATENCY)
    driver.switch_to.window(driver.window_handles[-1])

    # Select Identification
    driver.find_element_by_xpath("//input[@value='선택']").click();

    # Finally enter education page
    sleep(LATENCY)
    driver.get("http://cafm.korea.ac.kr/archibus/safety_edu/selec_req_list.jsp")
    print("Done.")



# Enrolling logic for each class
def enroll(driver, idx):
    '''
    [Requirement]
    driver should be in education page!
    '''
    print(f"[+] Enrolling class #{idx}... ", end='')
    driver.execute_script(f"se_event('{idx}')")
    sleep(LATENCY)
    driver.switch_to.alert.accept()
    print("Done.")

#Automatic Enrolling
def auto_enroll(driver, idxs):
    print(f"[*] Automatically enrolling class #{idxs}...")
    for idx in idxs:
        enroll(driver, idx)
    print("[+] Enrolled.")


def solve_test(driver, idx):
    sleep(LATENCY)
    # Enter test
    print(f"[+] Automatically solving test of class #{idx}...", end='')
    driver.execute_script(f"test_event('{idx}', 'kor')")
    driver.switch_to.alert.accept()
    sleep(LATENCY*2)

    # Switch tab
    driver.switch_to.window(driver.window_handles[-1])

    # import database
    answer = answer_database[idx]
    
    # Solve question with answer
    for num in range(len(answer)):
        if answer[num] is -1:
            continue
        driver.find_element_by_id(f"ans_{num+1}_{answer[num]}").click()
    
    # Submit    
    driver.execute_script("submitPage()")
    sleep(LATENCY)
    driver.switch_to.alert.accept()
    driver.switch_to.window(driver.window_handles[1])
    print("Done.")


def auto_solve_test(driver, idxs):
    print(f"[*] Automatically taking test(s) of class #{idxs}...")
    driver.get(r"http://cafm.korea.ac.kr/archibus/safety_edu/selec_my_req_list.jsp")
    for idx in idxs:
        solve_test(driver, idx)
    print("[+] All Solved.")


def get_cert(driver):
    print("[*] Accessing certification issuing page", end='')
    driver.get("http://cafm.korea.ac.kr/archibus/se_cerper1.jsp?sesch_id=12&seem_id=91100")
    driver.execute_script("poppop('win', 'se_certificate.jsp?sesch_id=12&seem_id=91100&emper=', 200, 200, 950, 950, 0, 0, 0, 'yes', 'yes')")
    driver.switch_to.window(driver.window_handles[-1])
    print("Done.")
