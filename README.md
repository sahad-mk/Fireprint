<p align="center"> <img src="https://github.com/sahad-mk/Fireprint/blob/master/screenshots/fireprint_banner.png" height="50%" width="75%"></p>
<p align="center"><b><i> Fireprint - Firebase Scanner For Android/iOS Application </i> </b> </p>

## Fireprint
[![Build Status](https://api.travis-ci.org/sqlmapproject/sqlmap.svg?branch=master)](https://travis-ci.org/sqlmapproject/sqlmap)
 [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) 
 [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) 

 [![PyPI version](https://badge.fury.io/py/sqlmap.svg)](https://badge.fury.io/py/sqlmap) [![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/sqlmapproject/sqlmap.svg?colorB=ff69b4)](https://github.com/sqlmapproject/sqlmap/issues?q=is%3Aissue+is%3Aclosed) [![Twitter](https://img.shields.io/badge/twitter-@sqlmap-blue.svg)](https://twitter.com/sqlmap)

[![Fireprint](https://img.shields.io/badge/version-1.0-success)] [![Python](https://img.shields.io/badge/Python-3.x.x-important)]

## Introduction
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
 
             
  <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_android.png >
  

 ➋ Scanning iOS(.ipa) apps 
 
           
   <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_iOS.png >
   

 ➌ Scanning firebase db name
 
            
  <img src=https://github.com/sahad-mk/Fireprint/blob/master/screenshots/scan_dbname.png >

