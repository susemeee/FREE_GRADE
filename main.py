#Where all the magics happen
import HappyNARU

#test
id = input("ID : ")
pw = input("PW : ")

things_to_take = [1, 3, 13]

driver = HappyNARU.init_driver()

HappyNARU.enter_education(driver, id, pw)
HappyNARU.auto_enroll(driver, things_to_take)
HappyNARU.auto_solve_test(driver, things_to_take)
HappyNARU.get_cert(driver)
