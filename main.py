#Where all the magics happen
import HappyNARU

#test
id = input("ID : ")
pw = input("PW : ")

driver = HappyNARU.init_driver()

HappyNARU.enter_education(driver, id, pw)
HappyNARU.auto_enroll(driver, [1, 3, 13])

