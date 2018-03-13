#coding:utf-8
'''
title:mock server   初始化
author:Robert
date:20180123
email:luoshuibo@vcredut.com
content:
other:
'''


import sys,os
print("dirpath",os.getcwd())
curDir = os.getcwd()
sys.path.append(curDir)


from mockserver.templates import serverinfo, mock_body,showlog
from flask import Flask, jsonify, g, request
import requests
import random
import time
from datetime import datetime


app = Flask(__name__)




@app.before_request
def set_up_data():
    pass
    # g.in_body = mock_body.req_input_applycheck   ##导入参数

@app.route('/')
def Hello():
    return  "This is a Mock Server!!!  author:Robert"

@app.route('/mock/kbs/fund/PreCheck',methods=['POST'])
def mock_PreCheck():
    '''
    mock 资方平台fundsource 函数名称:PreCheck
    :return:
    '''
    g.in_body = mock_body.req_input_applycheck      ##导入返回参数
    req =request.json
    reqpath = request.full_path
    print("☆request☆☆☆☆☆☆",req,reqpath)
    print("☆response☆☆☆☆☆☆", g.in_body)
    return jsonify(g.in_body)

@app.route('/mock/kbs/fund/createApply',methods=['POST'])
def mock_createApply():
    '''
    mock 资方平台fundsource 函数名称:createApply
    :return:
    '''
    g.in_body = mock_body.req_input_createApply     ##导入返回参数
    req =request.json
    reqpath =request.full_path
    print("☆request☆☆☆☆☆☆",req,reqpath)
    print("☆response☆☆☆☆☆☆", g.in_body)
    return jsonify(g.in_body)

def mock_request():
    '''

    :return:
    '''
    # http://10.139.60.61:8089/OrderApplyLendingService/OrderLendingStatusResult

    url = mock_body.kbsmsa+mock_body.OrderLendingStatusResult
    inputbody =mock_body.input_body
    tempp =requests.post(url,json=inputbody)


@app.route('/mock/kbs/fund/createApplyold',methods=['POST'])
def mock_createApplyold():

    g.createorder = {
        "Kids": 'error',
        "OperaterId": "1",
        "Operater":"admin"

    }

    g.getorderstatus = {
        "ApplyCode": 'error',
        "LendingStatus": 56,
        "LendingTime":datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'),
        "LoanNo":int(time.mktime(time.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S"))),
        "ThirdSerialNo":random.randint(11000000,19999999)
    }

    req = request.json
    print('req_Kids_json',req)

    try:
        if req['Kids'] ==None or req['Operater'] == None or req['OperaterId'] == None :
            app.logger.error('参数不合法')
        elif len(req['Kids']) >= 1:
            g.createorder['Kids'] =req['Kids']

        else:
            g.createorder['Kids'] = '系统错误 '
    except Exception as execp :
        print(app.logger.error('参数不合法'))
        print('Exception ' ,execp)

    return jsonify(g.createorder)






if __name__ == '__main__':
    command_kill = "ps -ef | grep java | grep '${TOMCAT_DIR}/bin' | awk '{print $2}' | sed -n '$p'| xargs kill -9"
    # ps -ef | grep java | grep '${TOMCAT_DIR}/bin' | awk '{print $2}' | sed -n '$p'| xargs kill -9
    cs = serverinfo.serverinfo()         ##实例化
    ip = cs.get_serverip_local()                    ##获取本地ip
    showlog.showlog()
    app.run(host=ip , port=5000 ,debug=True )



