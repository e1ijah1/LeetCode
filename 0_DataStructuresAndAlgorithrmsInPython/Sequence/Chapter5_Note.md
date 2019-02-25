# List & Tuple



## 构造新列表:

- `extend` 方法效率高于多次调用 `append`
- 列表生成式或 `[0] * n` 速度快于多次 `append`

# String

- 构造字符串的优化
```python
letters = ''
for c in document:
	if c.isalpha():
	    # 可能重新生成字符串(取决于是否有引用, 无引用时解释器视字符串为一个动态数组)实例并赋值, 时间 O(n^2)
		letters += c
        
# 最优解决方案是使用列表推导式或生成器(避免临时list, 更优雅)
letters = ''.join(c for c in document if c.isalpha())
```

