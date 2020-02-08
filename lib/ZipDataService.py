import os
import zlib
import glob
import shutil
import zipfile
import datetime
from lib.DBService import DB

class ZipData():

    def __init__(self, dir_to_zip, db, ext = '*.bak'):
        self.dir_to_zip = dir_to_zip
        self.ext = ext
        self.db = db

    def __get_list__(self):

        os.chdir(self.dir_to_zip)
        curr_date = datetime.datetime.now().date()
        curr_list = []    

        for f in glob.glob(self.ext):
            created_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)

            if created_date.date() == curr_date:
                curr_list.append(f)

        return curr_list

    def __zip_list__(self):
        
        list_to_zip = self.__get_list__()
        print(list_to_zip)
        if list_to_zip:

            name_zip = f'backup{ datetime.datetime.now().strftime("%d%m%Y") }.zip'

            zf = zipfile.ZipFile(name_zip, mode='w')
            
            try:
                for f in list_to_zip:
                    zf.write(f, compress_type= zipfile.ZIP_DEFLATED)
                    print(f'ziped {f}')

                self.db.registerBackup(name_zip)

            finally:
                zf.close()

    def run(self):

        print('ejecutando script de respaldo.')
        self.__zip_list__()
        print('proceso finalizado.')
