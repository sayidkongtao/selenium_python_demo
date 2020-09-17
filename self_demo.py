from utils.utils import Utils
from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\PycharmProjects\selenium_python_demo\chrome_driver\chromedriver.exe")

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 启动

# server = Server(r'C:\Users\Administrator\Documents\WeChat Files\kttaoo\FileStorage\File\2020-08\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')

# server.start()
# proxy = server.create_proxy()

# 设置driver options
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server={0}'.format(proxy.proxy))
# options.add_argument('--ignore-certificate-errors')
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\PycharmProjects\selenium_python_demo\chrome_driver\chromedriver.exe",
                          options=options)

#url = 'https://www.dbs.com.sg/index/default.page'
#proxy.new_har('zhiye', options={'captureHeaders': True, 'captureContent': True})
url = 'https://www.dbs.com.cn/personal-sc/default.page'
driver.get(url)
time.sleep(10)
#res = proxy.har

#proxy.new_har('zhiye2', options={'captureHeaders': True, 'captureContent': True})
driver.get(url)
time.sleep(10)
# res1 = proxy.har

for entry in res['log']['entries']:
    res_url = entry['request']['url']
    if "/ApiUser/login?useraccount" in res_url:
        res_response = entry['response']
        print(res_response)
# server.stop()
# 59400121
# 966966
