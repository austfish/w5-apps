## APP 说明
- 文本发送
- 企业微信机器人官方文档：https://work.weixin.qq.com/api/doc/90000/90136/91770

## 动作列表

### 企微文本通知

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **webhook_key**  | text | `是` | 企业微信机器人 webhook_key，Webhook 地址可以看到 |
| **msg**  | text | `是` | 通知内容 (自定义关键字方式，需有关键字方可生效)|
| **mentioned_list**  | textarea | `否` | userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list|
| **mentioned_mobile_list**  | textarea | `否` | 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人|

**返回值：**

```
# 正常
{'errcode': 0, 'errmsg': 'ok'}
```

更多看：https://work.weixin.qq.com/api/doc/90000/90136/91770