#!/usr/bin/python3
import requests
import os
import time
from _datetime import datetime
import errno
import re
from zipfile import ZipFile
import argparse
import sys
import platform


# Function for fetching firebase endpoints
def getDb( dir_name ):
 dirct = dir_name
 # print("\n entered directory:", dirct)
 files_found = []

 for (dir, sub_dirs, files) in os.walk(dirct):
  for finame in files:
   files_found.append(os.path.abspath(os.path.join(dir, finame)))
 # print("full:",files_found)
 fin_arr = []
 for ex_file in files_found:
  with open(ex_file, "rb") as file_read:
   content = str(file_read.read())
   pattern = '[-a-zA-Z0-9_]+\.firebaseio.com'
   dbnames = re.findall(pattern, content)
   fin_arr.extend(dbnames)
 # print("\n Firebase Db found:", fin_arr)

 if len(fin_arr)==0:
  exit("\n \t \033[37;1m Firebase DB Name Not Found,Exit!\033[0m ")

 for fbase in fin_arr:
  isVulnfb(fbase)

# Check the given firebase db is misconfigure or not
def isVulnfb(fbdb_name):
 today = datetime.now()
 global read_en
 global write_en
 prj_name_str = fbdb_name.split('.', 1)
 prj_name=prj_name_str[0]
 read_en=0
 write_en=0

 new_endp = "https://" + str(fbdb_name)+"/.json/?shallow=true&format=exports"
 res_endp = "https://" + str(fbdb_name)
 test_endpoint = "https://" + str(fbdb_name) + "/test.json"
 try:
# check for read Access
   read_req = requests.get(new_endp)
   if read_req.status_code == 404 or read_req.status_code == 403 :
    exit("\n \t  Status > Firebase Db %s not found! exit.\n" % prj_name)
   elif read_req.status_code == 401:
    print("\n \t \033[37m Firebase DB > \033[36;1m %s\033[0m is Exist. \n" % prj_name)
    print("\n \t \033[37m Security Rule(\033[34;1m.read\033[0m) > Found \033[1;37;42m Secure Read Access!\033[0m \n")
   else:
    read_en=1
    print("\n \t \033[37m Firebase DB > \033[36;1m %s\033[0m is Exist. \n" % prj_name)
    print("\n \t \033[37m Security Rule(\033[34;1m.read\033[0m) > Found \033[1;37;41m Insecure Read Access, Data Exposed!\033[0m \n")
    print(" \t \033[37m Data retrieving\033[0m(\033[34;1m%s\033[0m) > \n" % prj_name)
    data_json = read_req.text
    print("\t ---------------------------------------------------------------------------------------------------- \n")
    print("\t  Root node found: \n")
    print("\t ",read_req.text, "\n")
    print("\t ----------------------------------------------------------------------------------------------------")
    print("\n \t \033[37m Data Retrieval(\033[34;1m%s\033[0m) > \033[0m\033[31;1m[*] Done \033[0m \n" % prj_name)


# check for write Access
   write_req = requests.put(test_endpoint, json={"fireprint_test": "Done"})
   if write_req.status_code == 401:
    print("\n \t \033[37m Appending Test Node (\033[34;1m /test.json\033[0m) > \033[0;37m Failed!\033[0m \n")
    print("\n \t \033[37m Security Rule(\033[34;1m.write\033[0m) > Found \033[1;37;42m Secure Write Access!\033[0m \n")
   else:
    write_en=1
    print("\n \t \033[37m Appending Test Node (\033[34;1m /test.json\033[0m) > \033[0;37m Successfull!\033[0m \n")
    # Delete created endpoint
    requests.delete(test_endpoint)
    print("\n \t \033[37m Cleaning Test Node (\033[34;1m%s\033[0m) > \033[0;37m Successfull!\033[0m \n" % prj_name)
    print("\n \t \033[37m Security Rule(\033[34;1m.write\033[0m) > Found \033[1;37;41m Insecure Write Access!\033[0m \n")
   if write_en == 1 or read_en == 1:
     print("\n \t \033[37m Security Status(\033[34;1m%s\033[0m) > \033[1;37;41m Firebase Db is Vulnerable! \033[0m\n" % prj_name)
   else:
     print("\n \t \033[37m Security Status(\033[34;1m%s\033[0m) > \033[1;37;42m Firebase Db is Secure! \033[0m \n" % prj_name)

# Creating Output directory
   output_dir = "result"
   try:
    os.mkdir(output_dir)
    print("\n \t \033[37m Output Directory >\033[0m \033[36;1m%s\033[0m  created! \n" % output_dir)
   except OSError as error_no:
    if errno.EEXIST:
     print("\n \t \033[37m Output Directory > \033[0m\033[36;1m%s\033[0m already exist! \n" % output_dir)

# saving result into html & txt file
   result = prj_name

   with open('./result/'+result+'.txt','w') as txt:
     txt.writelines('\n'+__headertxt__+'\n')
     txt.writelines('\n   \t \t                  Fireprint Scan Report \n')
     txt.writelines('\n   \t \t--------------------------------------------------------------------------- \n')
     txt.writelines('\n \t \t Firebase Project name : ' + prj_name + '\n')
     txt.writelines('\n \t \t Firebase db endpoint  : '+res_endp+'\n')

     if write_en == 1 and read_en == 1:
      txt.writelines('\n \t \t Read Access           : Insecure Read Access, Data Exposed! \n')
      txt.writelines('\n \t \t Write Access          : Insecure Write Access! \n')
      txt.writelines('\n \t \t Status                : Firebase Db is Vulnerable! \n')
     elif read_en==1:
       txt.writelines('\n \t \t Read Access : Insecure Read Access, Data Exposed! ')
       txt.writelines('\n \t \t Write Access :Secure ')
       txt.writelines('\n \t \t Nodes found           : '+data_json+'\n')
       txt.writelines('\n \t \t Status                : Firebase Db is Vulnerable! \n')
     elif write_en==1:
       txt.writelines('\n \t \t Read Access           : Secure \n')
       txt.writelines('\n \t \t Write Access          : Insecure Write Access! \n')
       txt.writelines('\n \t \t Status                : Firebase Db is Vulnerable! \n')
     else:
      txt.writelines('\n \t \t Read Access :  Secure ')
      txt.writelines('\n \t \t Write Access : Secure ')
      txt.writelines('\n \t \t Status                : Firebase DB is Secure! \n')
     txt.writelines('\n \t \t Scanning completed on : '+str(today.strftime("%Y-%m-%d %H:%M")))

   with open('./result/'+result+'.html','w') as ht:
       ht.writelines('<body style="background-color:lavender;">')
       ht.writelines('<h1 style="font-family:verdana;text-align:center;color:Teal">'+'<u>FirePrint Scan Report</u>'+'</h1>')
       ht.writelines('<div style="color:Red;font-family:courier;font-size:150%"><pre style="align:center"><b>'+__headertxt__+'</b></pre></div>')
       ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Firebase Project name : <b> '+prj_name+'</b></p>')
       ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%"> Firebase db endpoint : <b>'+res_endp+'</b></p>')

       if write_en == 1 and read_en == 1:
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Read Access  : <b> ' + 'Insecure, Data Exposed!' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Nodes found  : <b>' + data_json + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Write Access : <b> ' + 'Insecure Write Access!' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Status       : <b>Firebase Db is Vulnerable!</b> </p>')
       elif read_en == 1:
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Read Access  : <b> ' + 'Insecure, Data Exposed!' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Nodes found  : <b>'+data_json+'</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Write Access : <b> ' + 'Secure' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Status       : <b>Firebase Db is Vulnerable!</b> </p>')
       elif write_en == 1:
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Read Access  : <b> ' + 'Secure' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Write Access : <b> ' + 'Insecure Write Access!' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Status       : <b>Firebase Db is Vulnerable!</b> </p>')
       else:
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Read Access  : <b> ' + 'Secure' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Write Access : <b> ' + 'Secure' + '</b></p>')
        ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Status       : <b>Firebase DB is Secure!</b> </p>')
       ht.writelines('<p style="text-align:center">Scanning completed on: '+str(today.strftime("%Y-%m-%d %H:%M"))+'</p>')
       ht.writelines('<br>')
       ht.writelines('<p style="text-align:center"><b>©FirePrint 2020 - 2021</b></p> </body>')
       print("\n \t \033[37m Output Files(\033[36;1m/%s\033[0m) >\033[0m\033[36;1m %s.html  %s.txt \033[0mare Generated! \n" % (output_dir,result,result))


#exception handling
 except requests.exceptions.HTTPError as errh:
   print("An Http Error occurred:",errh.response)
 except requests.exceptions.ConnectionError as errc:
   print("An connection Error occurred:", str(errc))
 except requests.exceptions.Timeout as errt:
   print("An timeout error occurred:", errt)
 except requests.exceptions.RequestException as err:
   print("An request Error occurred:", err)
 


#passing ipa file and find firebase project name
def deipa(infile):
 dir = "decomp"
 try:
  os.mkdir(dir)
  print("\n \t \033[37m Directory for extraction >\033[0m \033[36;1m'%s'\033[0m created now.\n" % dir)
 except OSError as error_no:
    if errno.EEXIST:
     print("\n \t \033[37m Directory for extraction > \033[0m \033[36;1m'%s'\033[0m already exist \n" % dir)
 print("\t \033[31;1m --------------------------------- Scanning For Misconfigured Firebase ----------------------------------\033[0m \n")
 infile1 = infile
 file_org = infile1.replace("'", "")

 path_file = os.path.split(file_org)
 fle_name, file_ext = os.path.splitext(file_org)
 file_name = path_file[1]

 # print("file extension is:",file_ext)
 if file_ext == '.ipa':
  print('\t \033[37m Processing ipa >\033[0m \033[35;1m%s \033[0m \n' % file_name)
 else:
  print('\t \033[37;1m Error: Please choose only ipa file! \033[0m \n')
  exit()

#checking whether the file is exist or not
 try:
  file_read = open(file_org,"r")
 except FileNotFoundError:
  print("\t \033[37;1m The chosen file is not found, Exit! \033[0m \n")
  sys.exit()

#EXtracting ipa file
 with ZipFile(infile1,'r') as ipa:
  ipa.extractall('./decomp/'+file_name)
  print("\n \t \033[37m IPA Extraction > \033[0m\033[31;1m[*] Done \033[0m \n")
  dir_name = "./decomp/" + file_name
  getDb(dir_name)

#passing apk file and find firebase project name
def decapk(apk_file):
 dir = "decomp"
 try:
  os.mkdir(dir)
  print("\n \t \033[37m Directory for extraction >\033[0m \033[36;1m'%s'\033[0m is created now.\n" % dir)
 except OSError as error_no:
  if errno.EEXIST:
   print("\n \t \033[37m Directory for extraction > \033[0m \033[36;1m'%s'\033[0m already exists \n" % dir)
 print("\t \033[31;1m --------------------------------- Scanning For Misconfigured Firebase ----------------------------------\033[0m \n")

 apk_file1 = apk_file                #input("input apk filename: )
 file_org = apk_file1.replace("'","")
 path_file = os.path.split(file_org)
 fle_name,file_ext = os.path.splitext(file_org)
 file_name = path_file[1]

#checking apk extension
 if file_ext == '.apk':
   print ('\t \033[37m Processing apk >\033[0m \033[35;1m%s \033[0m \n' % file_name)
 else:
  print('\t \033[37;1m Error:Please choose only apk file! \033[0m \n')
  exit()
#checking whether the file is exist or not
 try:
   file_read = open(file_org, "r")
 except FileNotFoundError:
   print("\t \033[37;1m The chosen file is not found, Exit! \033[0m \n")
   sys.exit()
#checking whether the apktool is exist or not
 if os.path.isfile('./tools/apktool.jar'):
  print()
 else:
  print('\t \033[37;1m apktool not found, Please copy apktool.jar file to the directory /tools  \033[0m \n')
  sys.exit()
#Decompiling apk file and searching for firebase db

 osid = platform.system()
 #print("current os:",osid)
#Windows
 if osid == "Windows":
  dec_cmd = ("java -jar ./tools/apktool.jar  d -f "+file_org + " -o ./decomp/"+file_name + " >nul 2>&1 ")
#Linux
 else:
  dec_cmd = ("java -jar ./tools/apktool.jar  d -f "+file_org + " -o ./decomp/"+file_name + " > /dev/null")
 
 os.system(dec_cmd)
 print("\t \033[37m APK Decompilation > \033[0m\033[31;1m[*] Done \033[0m \n")
 dir_name = "./decomp/"+file_name
 getDb(dir_name)


# Manually provide firebase project name and check whether it's misconfigured or not
def deman(project_name):
 print("\t \033[31;1m --------------------------------- Scanning For Misconfigured Firebase ----------------------------------\033[0m \n")
 fburl=project_name+".firebaseio.com"
 isVulnfb(fburl)


#banner
__headertxt__ = '''
                                  \t \t          ______  _             ______        _         _   
                                  \t \t          |  ___|(_)            | ___ \      (_)       | |  
                                  \t \t          | |_    _  _ __   ___ | |_/ / _ __  _  _ __  | |_ 
                                  \t \t          |  _|  | || '__| / _ \|  __/ | '__|| || '_ \ | __|
                                  \t \t          | |    | || |   |  __/| |    | |   | || | | || |_ 
                                  \t \t          \_|    |_||_|    \___|\_|    |_|   |_||_| |_| \__|
                                                          \t            [Firebase Scanner For Andoid/iOS]

                                       '''


__header__ = '''
\t \t\033[38;5;196m______  _             ______        _         _   \033[0m
\t \t\033[38;5;196m|  ___|(_)            | ___ \      (_)       | |  \033[0m
\t \t\033[38;5;196m| |_    _  _ __   ___ | |_/ / _ __  _  _ __  | |_ \033[0m
\t \t\033[38;5;196m|  _|  | || '__| / _ \|  __/ | '__|| || '_ \ | __|\033[0m
\t \t\033[38;5;196m| |    | || |   |  __/| |    | |   | || | | || |_ \033[0m
\t \t\033[38;5;196m\_|    |_||_|    \___|\_|    |_|   |_||_| |_| \__|\033[0m \033[32;1mv2.0\033[0m
                  \t \033[37;1m [Firebase Scanner For Andoid/iOS]\033[0m
                      
                                       \t\t\t\033[34;1mCoded\033[0m\033[1;37;41m©Sahad.Mk\033[0m
 '''
print(__header__)
time.sleep(1)

#Command line arguments

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='\033[32;1m! Find Misconfigured Firebase Db !\033[0m',
                                 epilog=(''' \n Examples:
                                                         \n python3 fireprint.py -a test.apk  
                                                         \n python3 fireprint.py -i tets.ipa 
                                                         \n python3 fireprint.py -p tets_db 
               
                                                         ''')
                                  )
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-a", help="Choose an apk file \n", type=str,metavar="<apk file>")
group.add_argument("-i", help="Choose an ipa file \n", type=str,metavar="<ipa file>")
group.add_argument("-p", help="Enter a firebase project name ", type=str,metavar="<Firebase dbname>")
args = parser.parse_args()
ipa_file = args.i
apk_file = args.a
fb_project = args.p

if ipa_file is not None:
  deipa(ipa_file)
if apk_file is not None:
  decapk(apk_file)
if fb_project is not None:
  deman(fb_project)


