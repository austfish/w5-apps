## APP 说明

> 目前仅支持，`查询漏洞` 和 `统计漏洞状态` 两种方式

- 洞察官方文档：https://cesrc-creditease.github.io/doc/

## 动作列表

### 漏洞列表

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **api**  | text | `是` | 洞察2服务api接口地址 |
| **token**  | text | `是` | 洞察2 token|
| **search**  | text | `否` | 查询语句 |
| **vul_status**  | text | `否` | 漏洞状态：40/确认|

**返回值：**

```
# 正常
{'errcode': 0, 'errmsg': 'ok'}
```
