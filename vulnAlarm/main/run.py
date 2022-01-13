#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json

async def get_vuln_aliyun(range_time=3600):
    try:
        from datetime import datetime
    except:
        logger.info("[漏洞告警通知] 导入 datetime 模块失败, 请输入命令 pip install datetime")
        return {"status":2,"result":"导入 datetime 失败"}

    try:
        from lxml import etree
    except:
        logger.info("[漏洞告警通知] 导入 lxml 模块失败, 请输入命令 pip install lxml")
        return {"status":2,"result":"导入 lxml 失败"}

    logger.info(f"[漏洞告警通知] APP执行参数为: {range_time}")
    headers = {'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3)AppleWebKit / 535.20(KHTML, like Gecko) Chrome / 19.0.1036.7Safari / 535.20'}
    vulns = []
    try:
        r = requests.get(
            url="https://help.aliyun.com/noticelist/9213612.html",
            headers=headers)
        if r.status_code != 200:
            return {"status": 2, "result": f"请求阿里云 API 失败 ：{r.status_code}"}
        content = etree.HTML(r.text)
        vuln_list = content.xpath('//li[@class="y-clear"]')
        for vuln in vuln_list:
            title = vuln.xpath("./a/text()")[0]
            url = 'https://help.aliyun.com%s'%vuln.xpath("./a/@href")[0]
            vuln_create_time = vuln.xpath("./span/text()")[0] + ' ' +vuln.xpath("./span/span/text()")[0]
            now = datetime.now()
            vuln_time = datetime.strptime(str(vuln_create_time),"%Y-%m-%d %H:%M:%S")
            durn = (now-vuln_time).total_seconds()
            if durn<=int(range_time):
                vulns.append(f"{title} {url} {vuln_create_time}")
    except Exception as e:
        logger.error("[漏洞告警通知] 请求阿里云 API 失败:{e}", e=e)
        return {"status": 2, "result": f"请求阿里云 API 失败:{e}"}
    return {"status": 0, "result": {"count": len(vulns), "data": '\n'.join(vulns)}}

async def get_vuln_tencent(range_time=3600):
    try:
        from datetime import datetime
    except:
        logger.info("[漏洞告警通知] 导入 datetime 模块失败, 请输入命令 pip install datetime")
        return {"status":2,"result":"导入 datetime 失败"}
    logger.info(f"[漏洞告警通知] APP执行参数为: {range_time}")
    headers = {'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3)AppleWebKit / 535.20(KHTML, like Gecko) Chrome / 19.0.1036.7Safari / 535.20'}
    vulns = []
    data = {
            "action": "getAnnounceList",
            "data": {
             "rp": 10,
            "page": "1",
            "categorys": [
             "21"
            ],
             "labs": [],
             "keyword": ""
            }
        }
    try:
        r = requests.post(
            url="https://cloud.tencent.com/announce/ajax",
            headers=headers,data=json.dumps(data))
        if r.status_code != 200:
            return {"status": 2, "result": f"请求腾讯云 API 失败 ：{r.status_code}"}
        vuln_data=r.json()
        vuln_lists=vuln_data['data']['rows']
        for vuln in vuln_lists:
            title = vuln['title']
            url = 'https://cloud.tencent.com/announce/detail/%s'%vuln['announceId']
            vuln_create_time = vuln['beginTime']
            now = datetime.now()
            vuln_time = datetime.strptime(str(vuln_create_time),"%Y-%m-%d %H:%M:%S")
            durn = (now-vuln_time).total_seconds()
            if durn<=int(range_time):
                vulns.append(f"{title} {url} {vuln_create_time}")
    except Exception as e:
        logger.error("[漏洞告警通知] 请求腾讯云 API 失败:{e}", e=e)
        return {"status": 2, "result": f"请求腾讯云 API 失败:{e}"}
    return {"status": 0, "result": {"count": len(vulns), "data": '\n'.join(vulns)}}


# if __name__ == '__main__':
#     # 导入异步库
#     import asyncio


#     # 测试函数
#     async def test():
#         result = await get_vuln_aliyun(range_time='6700000')
#         print(result)


#     # 加入异步队列
#     async def main(): await asyncio.gather(test())


#     # 启动执行
#     asyncio.run(main())