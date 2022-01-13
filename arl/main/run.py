#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def get_asset_scope(api, token, search=''):
    logger.info(f"[灯塔助手通知] APP执行参数为: {api} {token} {search}")

    headers = {'accept': 'application/json','Token': token}
    try:
        r = requests.get(
            url=f"https://{api}/api/asset_scope/?{search}",
            headers=headers, 
            verify=False)
    except Exception as e:
        logger.error("[灯塔助手通知] 请求灯塔 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求灯塔资产组 API 失败"}

    return {"status": 0, "result": r.json()}

async def get_asset_scope_site(api, token, scope_id='', site='', search=''):
    logger.info(f"[灯塔助手通知] APP执行参数为: {api} {token}")

    headers = {'accept': 'application/json','Token': token}
    try:
        r = requests.get(
            url=f"https://{api}/api/asset_site/?site={site}&scope_id={scope_id}&{search}",
            headers=headers, 
            verify=False)
    except Exception as e:
        logger.error("[灯塔助手通知] 请求灯塔 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求灯塔资产组站点 API 失败"}

    return {"status": 0, "result": r.json()}

async def add_site_tag(api, token, _id='', tag=''):
    logger.info(f"[灯塔助手通知] APP执行参数为: {api} {token}")

    headers = {'accept': 'application/json','Token': token,'Content-Type':'application/json'}
    try:
        r = requests.post(
            url=f"https://{api}/api/asset_site/add_tag/",
            headers=headers,
            data=json.dumps({"tag": tag,"_id": _id}),
            verify=False)
    except Exception as e:
        logger.error("[灯塔助手通知] 请求灯塔 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求灯塔资产组站点 API 失败"}

    return {"status": 0, "result": r.json()}
