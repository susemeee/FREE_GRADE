#Where all the magics happen
import HappyNARU

#test
id = input("ID : ")
pw = input("PW : ")

things_to_take = [1, 3, 13]

mode = input("OS?\n1 : Linux\n2 : Windows\n3 : MacOS\n> ")

mode = ["linux", "windows", "mac"][int(mode) - 1]

driver = HappyNARU.init_driver(mode)

HappyNARU.enter_education(driver, id, pw)
HappyNARU.auto_enroll(driver, things_to_take)
HappyNARU.auto_solve_test(driver, things_to_take)
HappyNARU.get_cert(driver)
