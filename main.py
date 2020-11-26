import smtplib
from time import sleep
from selenium import webdriver
import random
import datetime
url = 'https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp2%2Fsys%2FlwReportEpidemicSeu%2Findex.do%3Ft_s%3D1600433934587%26amp_sec_version_%3D1%26gid_%3DR0U5aEFFci9aTzYxMkpXQWZHQUNHL0hFcU9YUStWVmlQekhqNkEyNHUzdHZyRThCNFMvU2pVbWw0U1VKNVlaa1F5QkpGQkJuYkt6OEg2UE0rZzZTclE9PQ%26EMAP_LANG%3Dzh%26THEME%3Dindigo%23%2FdailyReport'

def sendEmail(content):
    # smtplib 用于邮件的发信动作
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header
    # 用于构建邮件头

    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '1162008006@qq.com'
    password = 'mqxqeoxafvqwfhdi'

    # 收信方邮箱
    to_addr = 'linjie980421@163.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(content, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('python test')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
#sendEmail("111")

#return random temperature [36.3~36.8]
def randTemper():
    return 36.0 + random.randint(3,8) * 0.1

#simulate the mouse
def simulate(user_name, password):
    driver = webdriver.Chrome('./chromedriver.exe')
    #enter the url
    driver.get(url)
    sleep(1)
    #find the username aera
    driver.find_elements_by_xpath("//input[@name='username' and @id='username']")[0].send_keys(user_name)
    sleep(1)
    #find the password aera
    driver.find_elements_by_xpath("//input[@id='password']")[0].send_keys(password)
    sleep(1)
    #find the submit button
    button = driver.find_element_by_xpath("//button")
    button.click()
    sleep(2)
    #following next page
    #find the add button
    driver.find_elements_by_xpath("//div[@data-action='add']")[0].click()
    #load the page 2s;
    sleep(2)

    #input the temper
    temper = str(randTemper())
    driver.find_elements_by_xpath("//input[@data-caption='当天晨检体温']")[0].send_keys(temper)
    sleep(1)
    #submit
    button = driver.find_element_by_xpath("//div[@id='save']")
    button.click()

    #sure it
    button = driver.find_element_by_xpath("// div[@class ='bh-dialog-btnContainerBox']/a[1]")
    button.click()
    #save png
    pic_name = user_name + "_" + str(datetime.date.today())
    driver.save_screenshot(pic_name+".png")
	#sendEmail("111")
	# sometimes get the input aera
	#driver.find_element_by_id('username').send_keys(user_name)
	#driver.find_element_by_id('password').send_keys(password)

if __name__ == '__main__':
    user_name = '220205053'
    password = 'AaLinjieer34..'
    simulate(user_name, password)