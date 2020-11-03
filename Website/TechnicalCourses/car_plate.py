# -*- coding: utf-8 -*-

import os
from aip import AipOcr

import json
 
"""get img"""
def get_file_content(filePath):
  with open(filePath,'rb') as fp:


    return fp.read()

 
""" get licsense plate """
def get_license_plate(filePath):
  """ APPID AK SK """
  APP_ID = '22912038'
  API_KEY = 'coAcbQDminM5Gr9fN5XtljPf'
  SECRET_KEY = 'T0zqfGFeIskxPycmY1tR3G7A03Kg4A8C'
 
  """ create client """
  client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
  image = get_file_content(filePath)
 
  """ 调用车牌识别 """
  res = client.licensePlate(image)
  return res
 
 
""" call example """

def find_files(filename, search_path):
  result = []

  # Wlaking top-down from the root
  for root, dir, files in os.walk(search_path):
    if filename in files:
      result.append(os.path.join(root, filename))
      file = result[0]
      res = get_license_plate(file)
      print('车牌号码：' + res['words_result']['number'])
      print('车牌颜色：' + res['words_result']['color'])







