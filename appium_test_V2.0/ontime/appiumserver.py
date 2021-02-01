#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import socket
import threading
from Conf.conf import cfg
from appium import webdriver
from app_logs.clock_log import log
from time import sleep
#命令行启动appium-server的进程，是一个多线程的封装
class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self) #继承父类的init
        self.cmd = cmd

    def run(self):    #重构run方法
        os.chdir(r'E:\appium_old_version\Appium')
        os.system(self.cmd)

#检查端口号是否被占用
def checkport(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
        print('%s is used' % port)
        return True
    except WindowsError:
        log.error('端口{}未被占用，可以使用！'.format(port))
        return False

#停止appium-server进程
def stop_appium():
    try:
        if os.system("taskkill /f /im node.exe"):
            log.info("关闭appium服务成功！")

    except Exception as e:
        log.error("关闭appium服务失败,失败原因是:{}".format(e))

#实例启动
class AppiumServer(object):
    def __init__(self, host=cfg.get('HOST-IP','host'), port=int(cfg.get('HOST-IP','port'))):
        self.host = host
        self.port = port
        self.cmdpath = cfg.get('HOST-IP','cmd')

    def start_appium(self):
        while 1:
            if checkport(self.host, self.port):
                self.port = self.port + 1
            else:
                break
        bp = self.port + 1
        cmd = (r'node.exe "%s" -a %s -p %s -bp %s --session-override'
               %(self.cmdpath,self.host, self.port, bp))
        try:
            t1 = RunServer(cmd)
            t1.start()      #进程的启动方式
            log.info("appium启动成功，接下来开始连接手机啦！")
        except Exception as e:
            log.error("appium启动失败！失败原因是:{}".format(e))

    def getport(self):
        return self.port

    def gethost(self):
        return self.host

#连接真机/模拟器
class Android:
    def __init__(self):
        # uninstall('io.appium.settings')
        try:
            desired_caps = dict(cfg.items('android-ZTE'))  #获取desired_caps的键值对
            url = ('http://%s:%s/wd/hub' % (cfg.get('HOST-IP','host'), cfg.get('HOST-IP','port')))
            self.driver = webdriver.Remote(url, desired_caps)
        except Exception as e:
            log.error("手机连接失败，失败的原因是{}".format(e))
        else:
            log.info("手机app连接成功，接下来开始操作界面ing")

    #设置元素定位方法 例如：xpath
    def clickbutton(self, locateway, path):
        if locateway == 'xpath':
            self.driver.find_element_by_xpath(path).click()
        elif locateway == 'name':
            self.driver.find_element_by_name(path).click()

    #坐标定位元素
    def tap(self, locationx, locationy):
        self.driver.tap([(locationx, locationy)], 10)

    #判断界面是否存在元素
    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def downswipe(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe((width / 2), ((height * 3) / 4), (width / 2), ((height * 2) / 5))
        sleep(5)

if __name__ == '__main__':
    a = AppiumServer()
    a.start_appium()
    # b = Android()
