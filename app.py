#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2022/06/10 16:54:48
@Author  :   Yu qianguo 
@Version :   1.0
@Contact :   yuqianguo@gmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import asyncio,os,json,time
import logging;logging.basicConfig(level=logging.INFO)
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Hello,world!</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()