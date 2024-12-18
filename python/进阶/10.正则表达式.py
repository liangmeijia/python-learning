import re
'''
正则表达式
概念：字符串处理工具
使用:需要导入re模块;使用re.match(pattern,string)方法 来匹配字符串string是否以pattern【开头】，是就返回一个Match对象，不是就返回None；使用Match对象的group方法获取获取匹配到的字符串
特点:语法比较复杂，可读性较差通用性很强，适用于多种编程语言
'''

# res = re.match(pattern='哈哈',string='哈哈是我的口头禅')
# print(res.group())


# 1、正则表达式的规则（匹配单个）：
# . 匹配任何一个字符，除了换行符\n
# [] 匹配[]中列举的单个字符
# \s 匹配空白或tab键
# \S 匹配非空白的任意一个
# \d 匹配0到9之间的任意一个数字
# \D 匹配非数字的任意一个
# \w 匹配单词字符，即a-z A-Z 0-9 _ 汉字
# \W 匹配非单个单词字符




#res = re.match('[0123456789]','9243')
# 匹配0-9第二种写法
# res = re.match( '[0-9]','3787')
#匹配0到4 7到9
# res = re.match( '[0-47-9]','5787')
# res = re.match( '[a-zA-Z]','adh787') #匹配52个大小写英文字母中的任意一个
# res = re.match(r'\d','3322') #在字符串前面加上r，这样Python解释器就不会尝试解析字符串中的转义序列了
# res = re.match(r'\s.',' 3322')
# print(res.group())


# 2、正则表达式的规则（匹配多个）：
# * 匹配前一个字符出现0次或者无限次，即可有可无
# + 匹配前一个字符出现1次或者无限次，即至少一次---常用
# ? 匹配前一个字符出现1次或者0次
# {m} 匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现从m次到n次,m必须小于n


#res = re.match(r'\d*','f23vfvga哈哈哈')
#res = re.match(r'\d+','23vfvga哈哈哈')
#res = re.match(r'\d?','563gf23vfvga哈哈哈')
# res = re.match(r'\w{3}','虾2s14d5f23vfvga哈哈哈')
# res = re.match(r'\w{1,4}','2f a2434knds')
# print(res)
# print(res.group())

#3、匹配开头和结尾
# ^ 匹配以某个字符开头，或取反
# $ 匹配以某个字符结尾
# res = re.match(r'^py','python') #代表以字符串py开头
# res = re.match(r'[^py]','thon') # ^放在中括号里面 代表匹配p,y以外的字符
#res = re.match(r'^jav\w$','java')
# print(res.group())

'''
4、匹配分组
| 匹配左右任意一个表达式
(ab) 将括号中字符作为一个分组
'''
# res = re.match(r'\w|\s',' er23g')
res = re.match(r'\w*@(163|qq|yeah).com','yyer23g@yeah.com')
print(res.group())