<p align="center"> <img src="https://github.com/sahad-mk/Fireprint/blob/master/screenshots/fireprint_banner.png" height="50%" width="75%"></p>
<p align="center"><b><i> Fireprint - Firebase Scanner For Android/iOS Application </i> </b> </p>

## Fireprint v1.0

![Fireprint](https://img.shields.io/badge/version-1.0-success)   ![python](https://img.shields.io/badge/Python-v3.x.x-important)   ![Tested](https://img.shields.io/badge/Tested%20On-Ubuntu%2018.04-green)  ![Support](https://img.shields.io/badge/Supported%20Files-Android%20apk%20/%20iOS%20ipa-blueviolet) [![Linkedin](https://img.shields.io/badge/Linkedin-/Sahadmk-blue)](https://www.linkedin.com/in/sahadmk)

Fireprint is a python based tool for finding misconfigured Firebase databases used in Android or iOS applications. Just drag and drop your apk/ipa files to this script and find if there is any misconfigured Firebase database is exist.

## Prerequisites
          1. pip3 install json2html
          
          2. apktool.jar (/tools directory)
          
          3. grep and awk
           
           
## Installation
          • clone the fireprint repo,   git clone https://github.com/sahad-mk/Fireprint
          
          • Give executable permission, chmod +x fireprint.py 
          
  
## Usage
          ➢ python3 fireprint.py -a|-i|-p <filename/firebase db name> [-o filename]
          
          ➢ python3 fireprint.py -h for help
 
   Examples:
                                                                                                                                             
          • python3 fireprint.py -a test.apk 
              
          • python3 fireprint.py -i tets.ipa or
                                                         
          • python3 fireprint.py -p tets_db 
                                                         
             if '-o' option is not specified by the user, Default file name will be as of the input file.
  
## Screenshots

 ➊ Scanning Android(.apk) apps
 
             
  <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_apk >
  

 ➋ Scanning iOS(.ipa) apps 
 
           
   <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_ipa >
   

 ➌ Scanning firebase db name
 
            
  <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_dbname.png >

