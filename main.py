#!/bin/env python2
'''
git clone https://github.com/seanharr11/etlalchemy

mysql damago@10.9.2.20:3306
passwort: damago

mssql sa@10.9.2.20:1433
passwort: thu4At7ale7iah5A1
'''

from etlalchemy import ETLAlchemySource, ETLAlchemyTarget
import etlalchemy


hostname = "10.9.2.20"
db_name = "Blumenversand_Test"

source = ETLAlchemySource("mssql+pyodbc://sa:thu4At7ale7iah5A1@"+hostname)
target = ETLAlchemyTarget("mysql://damago:damago@"+hostname+"/db_name", drop_database=True)
target.addSource(source)
target.migrate()
