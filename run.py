import datetime
from lib.ZipDataService import ZipData
from lib.DBService import DB
from lib.FtpService import FtpService

if __name__ == "__main__":

    db = DB()
    path = 'C:/'
    name_zip = f'backup{ datetime.datetime.now().strftime("%d%m%Y") }.zip'

    zip = ZipData(path, db)
    zip.run()

    resultExistZip = db.checkExistNameZip(name_zip)
    
    if(resultExistZip):
        ftp = FtpService('localhost', 'UserTest', 'PasswordTest')
        ftp.sendFile(path + name_zip)
        db.setAsSentBackup(name_zip)
        print("Envio realizado.")


