from selenium import webdriver
import datetime
import time
'''
option = webdriver.ChromeOptions()

option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=option)
'''


def buy(buy_time,mall):
    if mall=='1':
        #"结算"的css_selector
        btn_buy='#J_Go > span'
        #"立即下单"的css_selector
        btn_order='#submitOrderPC_1 > div.wrapper > a.go-btn'
    else:
        btn_buy='#J_Go > span'
        btn_order='#submitOrderPC_1 > div > a.go-btn'
    while datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')<'2019-12-12 03:02:00':
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
            try:
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    print("生成订单")
                    break
                time.sleep(0.01)
                #等待时间缩短至10ms，下同
            except:
                time.sleep(0.01)
        #print ('还在试，别催了')

    while datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')<'2019-12-12 03:02:00':
        try:
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                print("Sucess!")
                break
        except:
            time.sleep(0.01)
if __name__=='__main__':
    url='https://world.taobao.com/cart/cart.htm'
    mall='2' # 1-taobao 2-tmall
    bt='2019-12-12 03:00:00' # on sale time
    bt_dt=datetime.datetime.strptime(bt, '%Y-%m-%d %H:%M:%S')
    now_dt=datetime.datetime.now()
    print(f'{(bt_dt-now_dt).seconds:.1f} seconds remained, initialize or not？')
    input() # start
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    buy(bt,mall)
