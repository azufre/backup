import os
import fileinput
from ftplib import FTP

class FtpService:
    
    def __init__(self, ip, user, passwd):

        self.ftp = FTP()
        self.ftp.set_debuglevel(2)
        self.ip = ip

        self.user = user
        self.passwd = passwd

    def __startConnecion__(self):
        self.ftp.connect(self.ip, 21) 
        self.ftp.login(self.user, self.passwd)

    def __closeConnecion__(self):
        self.ftp.quit()

    def sendFile(self, pathName):
        
        self.__startConnecion__()
        self.ftp.storbinary('STOR /files/%s' % os.path.basename(pathName), open(pathName, 'rb'))
        self.__closeConnecion__()




