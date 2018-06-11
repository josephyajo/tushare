import configparser,os

projectName = "Sheep.Tushare"
thePath = os.getcwd()
print(thePath)
thePath = thePath[:thePath.find(projectName)+len(projectName)]
 
cf = configparser.ConfigParser() 
print(thePath+"/system.conf")
# cf.read(thePath+"system.conf")
# s = cf.sections()
# print ('section:', s) 

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
