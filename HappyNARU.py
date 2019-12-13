from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    driver.switch_to.window(driver.window_handles[1])

    # Select Identification
    driver.find_element_by_xpath("//input[@value='선택']").click();

    # Finally enter education page
    sleep(LATENCY)
    driver.get("http://cafm.korea.ac.kr/archibus/safety_edu/selec_req_list.jsp")
    print("Done.")




def enrolling(driver, idx):
    '''
    [Requirement]
    driver should be in education page!
    '''
    print(f"[+] Enrolling class #{idx}... ", end='')
    driver.execute_script(f"se_event('{idx}')")
    sleep(LATENCY)
    driver.switch_to.alert.accept()
    print("Done.")

def auto_enroll(driver, idxs):
    print(f"[*] Automatically enrolling class #{idxs}...", end='')
    for idx in idxs:
        enrolling(driver, idx)
    print("Done.")

