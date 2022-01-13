## APP 说明
 
> 目前仅支持，`阿里云漏洞预警查询` 一种方式

## 动作列表

### 漏洞列表

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **range_time**  | number | `否` | 查询与当前时间差值范围内的漏洞，单位：秒，默认相差：3600秒 |

**返回值：**
```
# 数据
{"status": 0, "result": {"count": len(vulns), "data": vulns}}
```

```
# 正常
{'errcode': 0, 'errmsg': 'ok'}
```