from configparser import ConfigParser
import os
a = os.path.join(os.path.dirname(__file__),'config.ini')
class Handle(ConfigParser):
    def __init__(self,filename):
        ConfigParser.__init__(self, defaults=None)   #重写optionxform的方法，让option输出区分大小写
        super().__init__()
        self.filename = filename
        self.read(filename)

    def optionxform(self, optionstr):
        return optionstr


cfg = Handle(a)





