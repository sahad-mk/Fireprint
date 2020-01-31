<p align="center"> <img src="https://github.com/sahad-mk/Fireprint/blob/master/screenshots/fireprint_banner.png" height="50%" width="75%"></p>
<p align="center"><b><i> Fireprint - Firebase Scanner For Android/iOS Application </i> </b> </p>

## Introduction
Fireprint is a python based tool for finding misconfigured Firebase databases used in Android or iOS applications. Just drag and drop your apk/ipa files to this script and find if there is any misconfigured Firebase database is exist.

## Prerequisites
           1. pip3 install json2html
           2. apktool.jar (/tools directory)
           3. grep and awk
           4. Java runtime
           
## Installation
    • clone the fireprint repo https://github.com/sahad-mk/Fireprint
    • Make the script has executable permission
    • Just run the script with python3
  
## Usage
 
   Examples:
                                                                                                                                   python3 fireprint.py -a test.apk  
                                                         
              python3 fireprint.py -i tets.ipa or
                                                         
              python3 fireprint.py -p tets_db 
                                                         
              if '-o' option is not specified by the user, Default file name will be as of the input file.

         
