from collections import UserDict, UserList
from distutils.log import error
from http.client import OK
from webbrowser import get

from flask import *
import keyword
from multiprocessing import Value
import re
from telnetlib import AUTHENTICATION, STATUS
from urllib.request import urlopen
from flask import Flask, abort, jsonify, request
from flask_login import LoginManager
from flask_restful import Resource, Api
from mysqlx import Auth
from psutil import users

import requests



app = Flask(__name__)



@app.route('/employee', methods=['GET'])
def home():
    url=('https://globaleur63w.dayforcehcm.com/api/MediaKind/V1/Employees/')
    r = requests.get(url,auth=('SAPIntegWEBSVCS','Zombiet99')) 
    # res=r.json() 
    # return r
    # print(res) 
    final_result=[]  
    # json_result=[]
    for val in r.json()['Data']:
        val['XRefCode']
        # if [['Location']['LegalEntity']['Country']['Name']]=='India':
        #     final_result.append(val)
        #     print(final_result)
        url=(f'https://globaleur63w.dayforcehcm.com/api/MediaKind/V1/Employees/{val["XRefCode"]}?expand=EmployeeManagers,EmployeeProperties,Addresses,Contacts,EmploymentStatuses,OrgUnitInfos,WorkAssignments,Locations,EmploymentTypes,WorkContracts')
        r = requests.get(url,auth=('SAPIntegWEBSVCS','Zombiet99'))  
        res=r.json() 
        
        for i in res['Data']['Contacts']['Items']:
            print(i.get("Country",None))
            if i.get("Country") and i.get("Country").get("Name") == "India":
                print(i.get("Country"))
                # final_result.append(res['Data']['DisplayName'])
                final_result.append(res['Data']['DisplayName'])
                break
                   #print("value not found")
              
    print(final_result)
    return jsonify(final_result)

if __name__ == '__main__':
   app.run(debug = True) 