#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from ontime import  appiumserver
import threading
from app_logs.clock_log import log
from Conf.conf import cfg

class Task(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        appium = appiumserver.AppiumServer()
        appium.start_appium()
        time.sleep(15)
        driver = appiumserver.Android()
        time.sleep(10)
        try:
            driver.clickbutton('xpath', "//android.widget.TextView[@text='工作台']")
            print('-----click the workplace')
            time.sleep(10)
            driver.clickbutton('name','工作台')
            print('-----click the workplace agin')
            time.sleep(10)

            if not driver.is_element_exist('打卡'):
                driver.downswipe()
                print('-----下滑提示')

            driver.clickbutton('xpath',"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.tencent.wework:id/w4']/android.widget.RelativeLayout[5]")
            #driver.clickbutton('xpath', "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.tencent.wework:id/w4']/android.widget.RelativeLayout[11]/android.widget.LinearLayout[1]")
            print('-----click the clock in')
            time.sleep(10)
            driver.tap(266, 693)  # ZTE
            time.sleep(10)
            driver.tap(453, 903)  # ZTE
            print('-----clock in')
            time.sleep(10)
            driver.tap(20,75)
            time.sleep(10)
            driver.tap(132,121)
            print('-----clock back button')
            time.sleep(10)
            if driver.is_element_exist('工作台'):
                log.info("界面断言成功啦！开心~~~")
            else:
                log.error("界面断言失败了！::>_<:: ")

            time.sleep(10)
        except Exception as e:
            log.error("打卡失败，原因是{}".format(e))

        appiumserver.stop_appium()


if __name__ == '__main__':
    task1 = Task()
    # task2 = Task()
    task1.start()
    time.sleep(10)
    # task2.start()
