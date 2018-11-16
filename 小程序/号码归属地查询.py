from phone import Phone

import time,re


class SelectNumberHome(object):
    def get_user_input(self):
        while True:
            phoneNum = input("请输入要查询的号码:")
            result = re.match(r"1[3456789]\d{9}$", phoneNum)
            if result:
                print("输入号码有效")
                print("正在为您查询号码归属地...请稍后")
                time.sleep(2)
                return phoneNum
                break
            else:
                print("输入号码无效,请重新输入")
                time.sleep(1)

    def get_number_addr(self,phoneNum):
        info = Phone().find(phoneNum)
        try:
            phone = info['phone']
            province = info['province']
            city = info['city']
            zip_code = info['zip_code']
            area_code = info['area_code']
            phone_type = info['phone_type']
        except:
            print("Sorry,号码<%s>归属地信息系统暂时无法查询..." % phoneNum)
            print("请登录http://www.ip138.com/sj/ 进行查询")
        else:
            print("手机号码:%s\n运营商:%s\n归属地:%s,%s\n邮编:%s\n区号:%s" % (phone, phone_type, province, city, zip_code, area_code))


class SelectNumbersHome(object):

    def decide_numbers(self):
        while True:
            number1 = input("请输入第一个号码:")
            result1 = re.match(r"1[3456789]\d{9}$", number1)
            if result1:
                print("输入号码有效")
                break
            else:
                print("输入号码无效,请重新输入")
                time.sleep(1)
        while True:
            number2 = input("请输入第二个号码:")
            result2 = re.match(r"1[3456789]\d{9}$", number2)
            if result2:
                print("输入号码有效")
                break
            else:
                print("输入号码无效,请重新输入")
                time.sleep(1)
        while True:
            number3 = input("请输入第三个号码:")
            result3 = re.match(r"1[3456789]\d{9}$", number3)
            if result3:
                print("输入号码有效")
                print("正在为您查询号码归属地...请稍后")
                time.sleep(2)
                return number1,number2,number3
                break
            else:
                print("输入号码无效,请重新输入")
                time.sleep(1)

    def get_numbers_addr(self,number1,number2,number3):
        info1 = Phone().find(number1)
        info2 = Phone().find(number2)
        info3 = Phone().find(number3)
        try:
            phone1 = info1['phone']
            province1 = info1['province']
            city1 = info1['city']
            zip_code1 = info1['zip_code']
            area_code1 = info1['area_code']
            phone_type1 = info1['phone_type']
        except:
            print("Sorry,号码<%s>归属地信息系统暂时无法查询..." % number1)
            print("请登录http://www.ip138.com/sj/ 进行查询")
        else:
            print("手机号码:%s\n运营商:%s\n归属地:%s,%s\n邮编:%s\n区号:%s" % (phone1, phone_type1, province1, city1, zip_code1, area_code1))
            print("*"*20)
            time.sleep(1)
        try:
            phone2 = info2['phone']
            province2 = info2['province']
            city2 = info2['city']
            zip_code2 = info2['zip_code']
            area_code2 = info2['area_code']
            phone_type2 = info2['phone_type']
        except:
            print("Sorry,号码<%s>归属地信息系统暂时无法查询..." % number2)
            print("请登录http://www.ip138.com/sj/ 进行查询")
        else:
            time.sleep(1)
            print("手机号码:%s\n运营商:%s\n归属地:%s,%s\n邮编:%s\n区号:%s" % (phone2, phone_type2, province2, city2, zip_code2, area_code2))
            print("*" * 20)

        try:
            phone3 = info3['phone']
            province3 = info3['province']
            city3 = info3['city']
            zip_code3 = info3['zip_code']
            area_code3 = info3['area_code']
            phone_type3 = info3['phone_type']
        except:
            print("Sorry,号码<%s>归属地信息系统暂时无法查询..." % number3)
            print("请登录http://www.ip138.com/sj/ 进行查询")
        else:
            print("手机号码:%s\n运营商:%s\n归属地:%s,%s\n邮编:%s\n区号:%s" % (phone3, phone_type3, province3, city3, zip_code3, area_code3))
            time.sleep(1)

def print_menu():
    print("****号码归属地查询****")
    print("---------V1.0--------")
    print("----1.查询单个号码----")
    print("----2.查询多个号码----")
    print("----3.退出程序----")


def main():
    print_menu()
    select_number = SelectNumberHome()
    select_numbers = SelectNumbersHome()
    while True:
        num = int(input("请输入操作序号:"))
        if num == 1:
            phoneNum = select_number.get_user_input()
            select_number.get_number_addr(phoneNum)
        elif num == 2:
            number1,number2,number3 = select_numbers.decide_numbers()
            select_numbers.get_numbers_addr(number1,number2,number3)
        elif num == 3:
            print("正在退出程序...请稍后")
            time.sleep(2)
            break
        else:
            print("输入无效，请重新输入")
            time.sleep(1)


if __name__ == "__main__":
    main()
