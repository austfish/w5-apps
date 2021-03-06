## APP 说明

> Redis 操作客户端

### 通用参数

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **host**  | text | `是` | Redis 主机 |
| **port**  | number | `是` | 端口 |
| **db**  | number | `是` | Redis DB |
| **password**  | text | `否` | Redis 密码 |


## 动作列表

### GET

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 获取某个KEY的数据 |

**返回值：**

```
有数据直接返回数据，没有返回 None
```

### SET

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 写入某个 KEY |
| **value**  | text | `是` | 写入这个 KEY 的内容 |

**返回值：**

```
成功返回 True，失败 False
```

### DEL

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 删除这个 KEY |

**返回值：**

```
有数据返回条数，没有返回 0
```

### 清空数据-单个DB

> **危险动作，请谨慎操作**

**返回值：**

```
成功返回 True，失败 False
```

### 清空数据-全部DB

> **危险动作，请谨慎操作**

**返回值：**

```
成功返回 True，失败 False
```

### LPUSH-左插

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 写入某个 KEY 队列 |
| **value**  | text | `是` | 左边插入这个 KEY 的内容 |

**返回值：**

```
成功返回 True，失败 False
```

### RPOP-右取

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 获取某个KEY的队列右边的值 |

**返回值：**

```
有数据直接返回数据，没有返回 None
```

### LRANGE-左范围取

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 读某个 KEY 队列 |
| **index1**  | text | `是` | 从左数位置1 |
| **index2**  | text | `是` | 从左数位置2 |

**返回值：**

```
成功返回 位置1到位置2的数据列表，失败 False
```

### LLEN

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **key**  | text | `是` | 获取某个KEY 列表的长度 |

**返回值：**

```
用于返回列表的长度。 如果列表 key 不存在，则 key 被解释为一个空列表，返回 0 。 如果 key 不是列表类型，返回一个错误。
```