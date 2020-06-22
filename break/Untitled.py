#!/usr/bin/env python
# coding: utf-8

# In[8]:


# !bin/usr/env python3
# coding=utf-8
import requests
import json
import threading
 
def call_post(n):
    #http://localhost:8888/login?next=%2F
    #url = 'http:///login?next=%2Ftree%3F'
    url = 'http://localhost:8888/login?next=%2Ftree'
    body = {"_xsrf":"2|c29aad5a|cf64ccdce97f7bee4fd582d0cffc2f42|1590735819", "password": "123"}
    #body = {"akid":"623563258065190912", "appKey":"b01ace7af697413b9e06b15f6ceb44cb "}
    headers = {'content-type': "application/json"}
    
    r = requests.post(url,data=json.dumps(body),headers=headers)
    print('线程'+ str(n) + ':' + str(r.status_code) ) # n为并发数
    print (r.text)
def thread(n):
    threads = []
    for i in range(0,n):   # n 为并发数
        t = threading.Thread(target=call_post,args=(i,))
    # 针对函数创建线程，target为调用的并发函数，args为调用函数的参数，该参数必须为数组，所以这里加了逗号，如果不加就不是数组，运行会报错
        threads.append(t)# 添加线程到线程组
    print(threads)
    for t in threads:
        t.start()# 开启线程
    for t in threads:
        t.join()# 等待所有线程终止
for i in range(1):
    thread(1)


# In[ ]:




