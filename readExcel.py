#!/usr/bin/env python
#coding:utf-8
import xlrd


from investorBp.models import investor

data = xlrd.open_workbook('test.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
print nrows
import pdb; pdb.set_trace()
for item in range(1,nrows+1):
    realname = table.row_values(item)[1]
    email = table.row_values(item)[2]
    telephone = table.row_values(item)[3]
    weixin = table.row_values(item)[4]
    create_time = table.row_values(item)[5]
    update_time = table.row_values(item)[6]
    last_login  = table.row_values(item)[7]
    company = table.row_values(item)[8]
    position  = table.row_values(item)[9]
    industry  = table.row_values(item)[10]
    investAmount  = table.row_values(item)[11]
    fields = table.row_values(item)[12]
    stages = table.row_values(item)[13]
    roles = table.row_values(item)[14]
   




