'''
Created on Mar 22, 2018

@author: jack
'''
from sys import argv
import ConfigParser
import urllib
import subprocess
# import requests

scriptName, scriptConfigurationFileName = argv
print "The script is called:", scriptName
print "Your script comfiguration file name:", scriptConfigurationFileName

Config = ConfigParser.ConfigParser()
# print Config.sections()
Config.read(scriptConfigurationFileName)

wheretodownload = Config.get('DownloadFrom', 'URL')
saveto = Config.get('SaveTo', 'FileNameAmdLocation')

urllib.urlretrieve(wheretodownload, saveto)

subprocess.call([saveto, "/S", "/D=C:\\winpython27"])
print '*'*10
