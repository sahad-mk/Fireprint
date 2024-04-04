<p align="center"> <img src="https://github.com/sahad-mk/Fireprint/blob/master/screenshots/banner_2.0.png" height="50%" width="75%"></p>
<p align="center"><b><i> Fireprint - Firebase Scanner For Android/iOS Application </i> </b> </p>

## FirePrint v2.0

![Fireprint](https://img.shields.io/badge/version-2.0-success)   ![python](https://img.shields.io/badge/Python-v3.x.x-important)   ![Tested](https://img.shields.io/badge/Tested%20On-Ubuntu%2018.04%20&%20Windows%2011-green)  ![Support](https://img.shields.io/badge/Supported%20Files-Android%20apk%20/%20iOS%20ipa-blueviolet) [![Linkedin](https://img.shields.io/badge/Linkedin-/Sahadmk-blue)](https://www.linkedin.com/in/sahadmk)

FirePrint is a Python-based tool for identifying misconfigured Firebase databases used in Android or iOS applications. Simply drag and drop your APK/IPA files onto this script to check if any misconfigured Firebase databases exist.

## Prerequisites

          1. apktool.jar (/tools directory)
          
     
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
                                                         
  
## Screenshots

 ➊ Scanning Android(.apk) apps
 
             
   <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/apk1_scan.png>
  

 ➋ Scanning iOS(.ipa) apps 
 
           
   <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/ios_scan.png>
   

 ➌ Scanning firebase db name
 
            
   <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/direct_scan.png>
  
  
 ➍ HTML Report  
  
  
  <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/html_report.png>
  
 
  
 
