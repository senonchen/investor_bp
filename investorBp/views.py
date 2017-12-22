#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import xlrd
from investorBp.models import investor

def createInvestor(request):
    data = xlrd.open_workbook('test.xls') # 打开xls文件
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    print nrows
    # import pdb; pdb.set_trace()
    for item in range(1,nrows):
        realname = table.row_values(item)[2]
        email = table.row_values(item)[3]
        telephone = table.row_values(item)[4]
        weixin = table.row_values(item)[5]
        create_time = table.row_values(item)[6]
        update_time = table.row_values(item)[7]
        last_login  = table.row_values(item)[8]
        company = table.row_values(item)[9]
        position  = table.row_values(item)[10]
        industry  = table.row_values(item)[11]
        investAmount  = table.row_values(item)[12]
        fields = table.row_values(item)[13]
        stages = table.row_values(item)[14]
        roles = table.row_values(item)[15]
        investor.objects.create(realname=realname,email=email,telephone=telephone,weixin=weixin,company=company,position=position,industry=industry,investAmount=investAmount,fields=fields,stages=stages,roles=roles).save()
        
    return HttpResponse('%s | %s | %s | %s | %s'%(realname,email,telephone,stages,roles)) 

def deleteInvestor(request):
    investor.objects.all().delete()
    return HttpResponse("delete done")