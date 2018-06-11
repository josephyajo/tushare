import configparser
import os
import sys

projectName = "CJZK.CMS.Data"
thePath = os.getcwd()
thePath = thePath[:thePath.find(projectName)+len(projectName)]
print(thePath)

# def cur_file_dir():
#     path=sys[0]

# print(sys.path[0])
# 
# print(os.getcwd())
# 
# print(os.path.split(os.path.realpath(__file__))[0])

# config = configparser.ConfigParser()
# config.read('config/db.conf')
# str_val = config.get("database","dbhost")
# print(str_val)
