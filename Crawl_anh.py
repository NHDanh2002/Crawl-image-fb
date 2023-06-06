from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import urllib.request
import os

output_dir = 'temp'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def LuuAnh(img_url):
    img_save_path = output_dir + '/' + str(id) + '.jpg'
    urllib.request.urlretrieve(img_url, img_save_path)

taikhoan = input("Nhập tài khoản facebook của bạn vào đây:")
matkhau = input("Nhập mật khẩu facebook của bạn vào đây:")

browser = webdriver.Chrome(executable_path = "chromedriver.exe")
browser.get("https://www.facebook.com/Onmyojigame/photos/?ref=page_internal")
#browser.get("https://www.facebook.com")

sleep(3)

TenDN = browser.find_element_by_name("email")
TenDN.send_keys(taikhoan)
MatKhau = browser.find_element_by_name("pass")
MatKhau.send_keys(matkhau)

MatKhau.send_keys(Keys.ENTER)

sleep(10) 

imgs_list = browser.find_elements_by_xpath("//div[@class='x1n2onr6']")
#print(imgs_list)
#sleep(5)

id = 0
for img in imgs_list:
    a = img.find_element_by_class_name("xzg4506")
    b = a.get_attribute("src")
    LuuAnh(b)
    print(b)
    id+=1

sleep(5)
browser.close()