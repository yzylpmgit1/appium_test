#coding=utf-8

import logging
from Conf.conf import cfg
import os
clock_in_path = r'D:\Program Files (x86)\Jenkins\workspace\clock in'
clock_out_path = r'D:\Program Files (x86)\Jenkins\workspace\clock out'
log_path = os.path.dirname(__file__)

class HandleLog(object):

    @staticmethod
    def create_logger():
        #创建日志的收集器、设置日志等级
        mylog = logging.getLogger(cfg.get("log","name"))
        mylog.setLevel(cfg.get("log","level"))

        #创建输出到控制台的日志等级
        sh = logging.StreamHandler()
        sh.setLevel(cfg.get("log","sh_level"))
        mylog.addHandler(sh)

        #创建输出到文件的日志等级
        fh = logging.FileHandler(os.path.join(log_path,"log.txt"),encoding='utf-8')
        fh.setLevel(cfg.get("log","fh_level"))
        mylog.addHandler(fh)

        fh1 = logging.FileHandler(os.path.join(clock_in_path, "log.log"), encoding='utf-8')
        fh1.setLevel(cfg.get("log", "fh_level"))
        mylog.addHandler(fh1)

        fh2 = logging.FileHandler(os.path.join(clock_out_path, "log.log"), encoding='utf-8')
        fh2.setLevel(cfg.get("log", "fh_level"))
        mylog.addHandler(fh2)


        #定义输出日志的格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)
        fh1.setFormatter(fm)
        fh2.setFormatter(fm)
        return mylog

log = HandleLog().create_logger()












