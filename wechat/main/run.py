#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def send_text(webhook_key, content, mentioned_list=None, mentioned_mobile_list=None):
    logger.info("[企微机器人通知] APP执行参数为: {webhook_key} {text}", webhook_key=webhook_key, text=content)

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    try:
        r = requests.post(
            url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={webhook_key}".format(webhook_key=webhook_key),
            data=json.dumps({
                "msgtype": "text",
                "text": {
                    "content": content,
                    "mentioned_list": [x.strip() for x in mentioned_list.splitlines(keepends=True)]  if mentioned_list else None,
                    "mentioned_mobile_list": [x.strip() for x in mentioned_mobile_list.splitlines(keepends=True)]  if mentioned_mobile_list else None
                }
            }),
            headers=headers
        )
    except Exception as e:
        logger.error("[企微机器人通知] 请求企微机器人 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求企微机器人 API 失败"}

    return {"status": 0, "result": r.json()}

