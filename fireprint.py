#!/usr/bin/python3
import urllib.request
import urllib.error
import subprocess
import os
import time
from _datetime import datetime
import errno
import re
from zipfile import ZipFile
import argparse
import json
import sys





# Check the given firebase db is misconfigure or not
def isVulnfb(fbdb_name):
 today = datetime.now()
 global result
 new_endp = "https://" + str(fbdb_name) +".firebaseio.com" + "/.json/?shallow=true&format=exports"
 res_endp = "https://" + str(fbdb_name) +".firebaseio.com"
 #print("\n Scanning for--->", new_endp)
 try:

  f = urllib.request.urlopen(new_endp)

  print("\n \t \033[37m Firebase Status >\033[0m Firebase Db \033[31m %s\033[0m \033[0;37;41mfound and vulnerable!\033[0m \n" %fbdb_name)
  print(" \t \033[37m Data retrieving\033[0m(\033[34;1m%s\033[0m) > \n" %fbdb_name )
  data_ex = f.read()
  data_fin = str(data_ex.decode('utf-8').rstrip())
  data_print = json.loads(data_fin)
  data_json=json.dumps(data_print,indent=5)
  print(" ---------------------------------------------------------------------------------------------------- \n")
  print("Root node found: \n")
  print(data_json, "\n")
  print(" ----------------------------------------------------------------------------------------------------")
  print("\n \t \033[37m Data Retrieval(\033[36;1m%s\033[0m) > \033[0m\033[31;1m[*] Done \033[0m \n" % fbdb_name)
  #Saving result into various file formats
  if result is None:       #check whether the user provide output file name
   result = fbdb_name
#Creating Output directory
  output_dir = "result"
  try:
   os.mkdir(output_dir)
   print("\n \t \033[37m Output Directory >\033[0m \033[36;1m%s\033[0m  created! \n" % output_dir)
  except OSError as error_no:
   if errno.EEXIST:
    print("\n \t \033[37m Output Directory > \033[0m\033[36;1m%s\033[0m already exist! \n" % output_dir)

#saving result into txt file
  with open('./result/'+result+'.txt','w') as txt:
   txt.writelines('\n'+__headertxt__+'\n')
   txt.writelines('\n   \t \t                  Fireprint Scan Report \n')
   txt.writelines('\n   \t \t--------------------------------------------------------------------------- \n')
   txt.writelines('\n \t \t Firebase db endpoint  : '+res_endp+'\n')
   txt.writelines('\n \t \t Firebase Project name : '+fbdb_name+'\n')
   txt.writelines('\n \t \t Nodes found           : '+data_fin+'\n')
   txt.writelines('\n \t \t Status                :  Vulnerable! \n')
   txt.writelines('\n \t \t Scanning completed on : '+str(today.strftime("%Y-%m-%d %H:%M")))


#saving result to html file
  with open('./result/'+result+'.html','w') as ht:
   ht.writelines('<body style="background-color:lavender;">')
   ht.writelines('<h1 style="font-family:verdana;text-align:center;color:Teal">'+'<u>Fireprint Scan Report</u>'+'</h1>')
   ht.writelines('<div style="color:Red;font-family:courier;font-size:150%"><pre style="align:center"><b>'+__headertxt__+'</b></pre></div>')
   ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%"> Firebase db endpoint : <b>'+res_endp+'</b></p>')
   ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Firebase Project name : <b> '+fbdb_name+'</b></p>')
   ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Nodes found  : <b>'+data_json+'</b></p>')
   ht.writelines('<p style="background-color:darkcyan;color:white;font-family:courier;font-size:125%">Status : <b>Vulnerable!</b> </p>')
   ht.writelines('<p style="text-align:center">Scanning completed on: '+str(today.strftime("%Y-%m-%d %H:%M"))+'</p>')
   ht.writelines('<br>')
   ht.writelines('<p style="text-align:center"><b>©FirePrint 2020 - 2021</b></p> </body>')

   print("\n \t \033[37m Output Files(\033[36;1m/%s\033[0m) >\033[0m\033[36;1m %s.html  %s.txt \033[0mare Generated! \n" % (output_dir,result,result))
 except urllib.error.HTTPError as e:           #except urllib.error.HTTPError as e:
     #print(e.code)
     st_code=e.code
     #print(st_code.read())
     if st_code==401:
      print("\n \t \033[37m Firebase Status>\033[0m Firebase Db \033[32m%s\033[0m \033[0;30;42m is exist,but not vulnerable! \033[0m \n" %fbdb_name)
      print("\n \t \033[37m Output Files >\033[0m No data Found,files won't Generate! \n")
     elif st_code==404:
      print("\n \t \033[37m Firebase Status >\033[0m Firebase Db \033[34;1m%s\033[0m \033[33;1mis not exist! \033[0m" %fbdb_name)
      print("\n \t \033[37m Output Files >\033[0m No data Found,files won't Generate! \n")
     else:
      print("\n \t \033[37m Firebase Status>\033[0m FirebaseDb \033[34;1m%s\033[0m \033[33;1m Invalid Firebase name Error! \033[0m" % fbdb_name)
      print("\n \t \033[37m Output Files >\033[0m No data Found,files won't Generate! \n")
 except urllib.error.URLError as u:
  print("\t \033[37;1m Connection Error/bad url Error\033[0m \n")


#passing ipa file and find firebase project name
def deipa(infile):
 dir = "decomp"
 try:
  os.mkdir(dir)
  print("\n \t \033[37m Directory for extraction >\033[0m \033[36;1m'%s'\033[0m created now.\n" % dir)
 except OSError as error_no:
    if errno.EEXIST:
     print("\n \t \033[37m Directory for extraction > \033[0m \033[36;1m'%s'\033[0m already exist \n" % dir)
 print("\t \033[31;1m --------------------------------- Scan Misconfigured Firebase For iOS ----------------------------------\033[0m \n")
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
  grep_ipa = ("grep -aiR  'firebaseio.com' ./decomp/" + file_name + "/ |awk -F:// '{print $2}' | awk -F. '{print $1}'")
  #print("entered command:" + grep_ipa)
  print("\n \t \033[37m IPA Extraction > \033[0m\033[31;1m[*] Done \033[0m \n")
  process = subprocess.Popen(grep_ipa, stdout=subprocess.PIPE, shell=True)
  (ifireb_db, err) = process.communicate()
  ifireb_dbname = str(ifireb_db.decode('utf-8').replace('\n', '').rstrip())
  if ifireb_dbname == '':
   print("\t \033[37;1m No Firebase Database Name Found, Exit! \033[0m \n")
   sys.exit()
  isVulnfb(ifireb_dbname)

#passing apk file and find firebase project name
def decapk(apk_file):
 dir = "decomp"
 try:
  os.mkdir(dir)
  print("\n \t \033[37m Directory for extraction >\033[0m \033[36;1m'%s'\033[0m is created now.\n" % dir)
 except OSError as error_no:
  if errno.EEXIST:
   print("\n \t \033[37m Directory for extraction > \033[0m \033[36;1m'%s'\033[0m already exists \n" % dir)
 print("\t \033[31;1m --------------------------------- Scan Misconfigured Firebase For Android ----------------------------------\033[0m \n")

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
 dec_cmd = ("java -jar ./tools/apktool.jar  d -f "+file_org + " -o ./decomp/"+file_name + " > /dev/null")
# print("entered command:"+dec_cmd)
 os.system(dec_cmd)
 print("\n \t \033[37m APK Decompilation > \033[0m\033[31;1m[*] Done \033[0m \n")
 grep_cmd = ("grep -iR  'firebaseio.com' ./decomp/"+file_name+"/ |awk -F:// '{print $2}' | awk -F. '{print $1}'")
 #print("entered command:" + grep_cmd)
 process= subprocess.Popen(grep_cmd, stdout=subprocess.PIPE, shell=True)
 (fireb_db, err) = process.communicate()
 fireb_dbname = str(fireb_db.decode('utf-8').replace('\n','').rstrip())
 if fireb_dbname == '':
  print("\t \033[37;1m No Firebase Database Name Found, Exit! \033[0m \n")
  sys.exit()
 isVulnfb(fireb_dbname)

# Manually provide firebase project name and check whether it's misconfigured or not
def deman(project_name):
 dir = "decomp"
 try:
  os.mkdir(dir)
  print("\n \t \033[37m Directory for extraction >\033[0m \033[36;1m'%s'\033[0m  created now.\n" % dir)
 except OSError as error_no:
  if errno.EEXIST:
   print("\n \t \033[37m Directory for extraction > \033[0m \033[36;1m'%s'\033[0m already exists \n" % dir)
 print("\t \033[31;1m --------------------------------- Scan Misconfigured Firebase  ----------------------------------\033[0m \n")
 fburl=project_name
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
\t \t\033[38;5;196m\_|    |_||_|    \___|\_|    |_|   |_||_| |_| \__|\033[0m \033[32;1mv1.1\033[0m
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
                                                         \n if '-o' option is not specified by the user, Default file name will be as of the input file.
                                                         ''')
                                  )
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-a", help="Choose an apk file \n", type=str,metavar="<apk file>")
group.add_argument("-i", help="Choose an ipa file \n", type=str,metavar="<ipa file>")
group.add_argument("-p", help="Enter a firebase project name ", type=str,metavar="<Firebase dbname>")
parser.add_argument("-o", help="Output file name", type=str,metavar="<file_name>")
args = parser.parse_args()
ipa_file = args.i
apk_file = args.a
fb_project = args.p
result = args.o
pattern="^[a-zA-Z0-9_]*$"
if result is not None:
 if not re.match(pattern,result):
   print('\t \033[37;1m Error: invalid file name %s, please choose a valid file name\033[0m \n' % result)
   sys.exit()
if ipa_file is not None:
  deipa(ipa_file)
if apk_file is not None:
  decapk(apk_file)
if fb_project is not None:
  deman(fb_project)


