#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def get_vuln(api, token, search=None, vul_status=None):
    logger.info(f"[洞察助手通知] APP执行参数为: {api} {token} {search} {vul_status}")

    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    try:
        r = requests.get(
            url=f"http://{api}/api/vul/list?token={token}&vul_status={vul_status}&search={search}",
            headers=headers)
    except Exception as e:
        logger.error("[洞察助手通知] 请求洞察 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求洞察漏洞列表 API 失败"}

    return {"status": 0, "result": r.json()}

async def get_vuln_status_group(api, token):
    logger.info(f"[洞察助手通知] APP执行参数为: {api} {token}")

    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    try:
        r = requests.get(
            url=f"http://{api}/api/vul/my/status/group?token={token}",
            headers=headers)
    except Exception as e:
        logger.error("[洞察助手通知] 请求洞察 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求洞察漏洞状态统计 API 失败"}

    return {"status": 0, "result": r.json()}