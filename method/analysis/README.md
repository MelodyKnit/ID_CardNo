## 通过信息分析号码的方法集成
<p>以下使用的号码为伪号码，切勿用于其他使用</p>

### get_uid15And18

该方法负责分析传入号码是否满足长度为15或者18<br>
如果满足则返回18和15长度是身份的两个参数，不满足返回None<br>
该方法会调用get_18IdNum和get_15IdNum<br>
例如:

```python
id_number = '110101192011076171'
id18, id15 = get_uid15And18(id_number)
print(id18) # 110101192011076171
print(id15) # 110101201107617
```

### get_time

该方法获取出生时间<br>
以列表(数组)的形式返回<br>
例如:

```python
id_number = '110101192011076171'
"""[年, 月, 日]"""
for i, t in zip(get_time(id_number), ['年', '月', '日']):
    print(i, t)
# 1920 年
# 11 月
# 07 日
```

### get_area

该方法获取所在城市地区<br>
以列表(数组)的形式返回<br>
该方法会调用readAreaData方法来获取数据但不会频繁获取，只会程序启动时调用一次<br>
例如:

```python
id_number = '110101192011076171'
''.join(get_area(id_number)) # 北京北京东城区
```

### get_18IdNum

该方法传入15长度的号码会转为18长度<br>
以字符串形式返回<br>
该方法会调用code方法来获取第18位校验码<br>
例如:

```python
id_number = '110101201107617'
get_18IdNum(id_number) # 110101192011076171
```

### get_15IdNum

该方法传入18长度的号码会转为15长度<br>
以字符串形式返回<br>
例如:

```python
id_number = '110101192011076171'
get_15IdNum(id_number) # 110101201107617
```

### get_gender

该方法传入号码会提取对应位置来验证性别<br>
返回bool值<br>
男 == False 女 == True <br>

```python
id_number = '110101192011076171'
get_gender(id_number) # False
```
