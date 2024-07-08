# -*- coding: utf-8 -*-
# @Time: 2024/7/6 11:17
# @Auth: Zhou Yanhui

import re


# Pattern.search(string[,pos[,endpos]])
# string: 要匹配的字符串
# pos: 匹配的起始位置, 默认为0
# endpos: 匹配的结束位置, 默认为字符串长度
# 扫描整个字符串, 寻找第一个成功的匹配, 返回Match类的实例对象; 如果没有匹配, 则返回None
# p = re.compile('og')
# m = p.search('dog')
# print(m)  # <re.Match object; span=(1, 3), match='og'>
#
# print(p.search('dog', 2))  # None
# print(p.search('dog', endpos=2))  # None
# print(p.match('dog', 1))  # <re.Match object; span=(1, 3), match='og'>


# Pattern.match(string[,pos[,endpos]])
# 扫描字符串的起始位置, 必须在起始位置匹配成功, 如果匹配成功, 返回Match类的实例对象, 否则返回None
# p = re.compile(r'og')
# print(p.match('dog'))  # None
# 可以是切片的字符串开头
# print(p.match('dog', 1))  # <re.Match object; span=(1, 3), match='og'>


# Pattern.fullmatch(string[,pos[,endpos]])
# 匹配字符串, 必须整个字符串匹配成功, 完全一样, 如果匹配成功, 返回Match类的实例对象, 否则返回None
# p = re.compile('o[gh]')
#
# print(p.fullmatch('ogh'))  # None
# print(p.fullmatch('og'))  # <re.Match object; span=(0, 2), match='og'>
# print(p.fullmatch('oh'))  # <re.Match object; span=(0, 2), match='oh'>
# print(p.fullmatch('dog'))  # None
# print(p.fullmatch('dog', 1))  # <re.Match object; span=(1, 3), match='og'>


# Pattern.findall(string[,pos[,endpos]])
# 对字符串从左往右扫描, 照的所有不重复匹配, 以列表的形式返回; 如果没有找到匹配, 则返回空列表
# p = re.compile(r'\d')
# print(p.findall('Ten years ago, Three dogs.'))  # []
# print(p.findall('10 years ago, 3 dogs.'))  # ['1', '0', '3']

# p = re.compile(r'.+')
# print(p.findall('abc'))  # ['abc']

# p = re.compile(r'.*')
# print(p.findall('abc'))  # ['abc', '']


# Pattern.finditer(string[,pos[,endpos]])
# 和findall类似, 不同在于finditer以迭代器形式返回,保存的是Match类的实例对象
# p = re.compile(r'\d')
# print(p.finditer('10 years age, 3 dogs.'))  # <callable_iterator object at 0x10ed31fc0>
# for i in p.finditer('10 years age, 3 dogs.'):
#     print(i)


# 特殊字符
# .  匹配除了换行符以为的任意一个字符, 在re.DOTALL(re.S)模式下, 它将匹配包括换行符的任意一个字符
# p = re.compile(r'.')
# print(p.match('abc'))  # <re.Match object; span=(0, 1), match='a'>
# print(p.match('9bc'))  # <re.Match object; span=(0, 1), match='9'>
# print(p.match('@bc'))  # <re.Match object; span=(0, 1), match='@'>
# print(p.match('.bc'))  # <re.Match object; span=(0, 1), match='.'>
# print(p.match('\tbc'))  # <re.Match object; span=(0, 1), match='\t'>
# print(p.match('\nbc'))  # None
# print(p.search('abc'))  # <re.Match object; span=(0, 1), match='a'>


# ^  匹配字符串的开头, re.MULTILINE(re.M)模式下, 还会继续匹配换行后的开头
# p = re.compile(r'^ab')
# print(p.findall('abcd\nabfg'))  # ['ab']
#
# p = re.compile(r'^ab', re.MULTILINE)
# print(p.findall('abcd\nabfg'))  # ['ab', 'ab']


# $  匹配字符串的末尾 或者 匹配换行符之前的字符(换行符必须在字符串的末尾)
# re.MULTILINE(re.M)模式下, 还会匹配换行符之前的字符(换行符可以不在字符串末尾)
# p = re.compile(r'cd$')
# print(p.findall('abcd\n'))  # ['cd']
#
# p = re.compile(r'cd$', re.M)
# print(p.findall('abcd\nefcd'))  # ['cd', 'cd']

# 会找到两个(空的)匹配:一个在换行符之前,一个在字符串的末尾
# p = re.compile(r'$')
# print(p.findall('abcd\n'))  # ['', '']


# *  对它前面的正则表达式匹配0到任意次重复, 尽量多的匹配(贪婪)
# p = re.compile(r'ab*')
# print(p.search('a'))  # <re.Match object; span=(0, 1), match='a'>
# print(p.search('ab'))  # <re.Match object; span=(0, 2), match='ab'>
# print(p.search('abb'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 4), match='abbb'>


# +  对它前面的正则表达式匹配1到任意次重复, 尽量多的匹配(贪婪)
# p = re.compile(r'ab+')
# print(p.search('a'))  # None
# print(p.search('ab'))  # <re.Match object; span=(0, 2), match='ab'>
# print(p.search('abb'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 4), match='abbb'>


# ?  对它前面的正则表达式匹配0到1次, 尽量多的匹配(贪婪)
# p = re.compile(r'ab?')
# print(p.search('a'))  # <re.Match object; span=(0, 1), match='a'>
# print(p.search('ab'))  # <re.Match object; span=(0, 2), match='ab'>
# print(p.search('abb'))  # <re.Match object; span=(0, 2), match='ab'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 2), match='ab'>


# *? +? ??  * + ? 都是贪婪的, 它们对字符串进行尽可能多的匹配, 有时候并不需要这种行为, 可以在之后添加?,
# 就可以以非贪婪的方式进行匹配, 则尽可能少的字符将会被匹配
# p = re.compile(r'<.*>')
# print(p.search('<a> b <c>'))  # <re.Match object; span=(0, 9), match='<a> b <c>'>
#
# p = re.compile(r'<.*?>')
# print(p.search('<a> b <c>'))  # <re.Match object; span=(0, 3), match='<a>'>
#
# p = re.compile(r'ab+?')
# print(p.search('abbbc'))  # <re.Match object; span=(0, 2), match='ab'>
#
# p = re.compile(r'ab??')
# print(p.search('abc'))  # <re.Match object; span=(0, 1), match='a'>


# {m}  对其之前的正则表达式指定匹配m个重复
# p = re.compile(r'ab{2}')
# print(p.search('abc'))  # None
# print(p.search('abbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 3), match='abb'>


# {m,n}  对其之前的正则表达式进行m到n次匹配, 在m和n之间取尽量多(贪婪方式), 忽略m则下限为0, 忽略n则上限默认为无限次(逗号不能省略)
# p = re.compile(r'ab{2,4}')
# print(p.search('abc'))  # None
# print(p.search('abbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 4), match='abbb'>
# print(p.search('abbbbc'))  # <re.Match object; span=(0, 5), match='abbbb'>
# print(p.search('abbbbbc'))  # <re.Match object; span=(0, 5), match='abbbb'>


# {m,n}?  上面{m,n}的非贪婪模式
# p = re.compile(r'ab{2,4}?')
# print(p.search('abc'))  # None
# print(p.search('abbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbbbc'))  # <re.Match object; span=(0, 3), match='abb'>

# p = re.compile(r'ab{,4}?')
# print(p.search('ac'))  # <re.Match object; span=(0, 1), match='a'>
# print(p.search('abc'))  # <re.Match object; span=(0, 1), match='a'>

# p = re.compile(r'ab{2,}?')
# print(p.search('abbbbc'))  # <re.Match object; span=(0, 3), match='abb'>
# print(p.search('abbbbbc'))  # <re.Match object; span=(0, 3), match='abb'>


# |  任意个正则表达式可以用|连接, 比如A|B表示匹配正则表达式A或B, 一旦有一个先匹配成功, 另外的就不会再进行匹配, |绝不贪婪,和[amk]功能相同
# p = re.compile(r'd|e|b')
# print(p.search('abc'))  # <re.Match object; span=(1, 2), match='b'>
# print(p.search('aebcd'))  # <re.Match object; span=(1, 2), match='e'>


# \  转义特殊字符(元字符)
# 只匹配*号
# p = re.compile(r'\*')
# print(p.findall('*'))  # ['*']

# 只匹配+号
# p = re.compile(r'\+')
# print(p.findall('+'))  # ['+']

# 只匹配?号
# p = re.compile(r'\?')
# print(p.findall('?'))  # ['?']


# \A 匹配字符串的开头, 类似于^, 区别在于:re.MULTILINE模式下, \A不识别换行
# p = re.compile(r'^ab')
# print(p.findall('abcd\nabfg'))  # ['ab']
#
# p = re.compile(r'^ab', flags=re.MULTILINE)
# print(p.findall('abcd\nabfg'))  # ['ab', 'ab']
#
# p = re.compile(r'\Aab')
# print(p.findall('abcd\nabfg'))  # ['ab']
#
# p = re.compile(r'\Aab', flags=re.MULTILINE)
# print(p.findall('abcd\nabfg'))  # ['ab']


# \b  匹配空字符串, 但只在单词开始或结尾的位置, 即匹配一个单词边界
# p = re.compile(r'er\b')
# print(p.search('never'))  # <re.Match object; span=(3, 5), match='er'>
# print(p.search('verb'))  # None

# p = re.compile(r'\ba\b')
# print(p.search('I have a dog'))  # <re.Match object; span=(7, 8), match='a'>
#
# p = re.compile(r'\b ')  # 空格也在单词的边界
# print(p.search('I have a dog'))  # <re.Match object; span=(1, 2), match=' '>


# \B  匹配空字符串, 但不能在单词开始或结尾的位置, 即匹配非单词边界
# p = re.compile(r'er\B')
# print(p.search('never'))  # None
# print(p.search('verb'))  # <re.Match object; span=(1, 3), match='er'>
#
# p = re.compile(r'\Ba\B')
# print(p.search('I have a dog'))  # <re.Match object; span=(3, 4), match='a'>


# \d  匹配任何一个十进制数字, 等价于 [0-9]
# p = re.compile(r'\d')
# print(p.search('a1234b'))  # <re.Match object; span=(1, 2), match='1'>
#
# p = re.compile(r'\d+')
# print(p.search('a1234b'))  # <re.Match object; span=(1, 5), match='1234'>


# \D  匹配任何一个非数字字符, 等价于 [^0-9]
# p = re.compile(r'\D')
# print(p.search('ab1234c'))  # <re.Match object; span=(0, 1), match='a'>
#
# p = re.compile(r'\D+')
# print(p.search('ab1234c'))  # <re.Match object; span=(0, 2), match='ab'>


# \s  匹配任何一个空白字符
# p = re.compile(r'a\sb')
# print(p.search('abd a bc'))  # <re.Match object; span=(4, 7), match='a b'>


# \S  匹配任何一个非空白字符
# p = re.compile(r'a\Sb')
# print(p.search('adb a bc'))  # <re.Match object; span=(0, 3), match='adb'>


# \w 匹配一个字母或一个数字, 或一个下划线, 等价于 [a-zA-Z0-9_]
# p = re.compile(r'a\wb')
# print(p.findall('adba9ba_ba b'))  # ['adb', 'a9b', 'a_b']


# \W  匹配一个非字母数字下划线, 等价于 [^a-zA-Z0-9_]
# p = re.compile(r'a\Wb')
# print(p.findall('adba9ba_ba b'))  # ['a b']


# \Z  只匹配字符串的末尾, 且MULTILINE模式下, \Z不识别换行
# p = re.compile(r'cd\Z')
# print(p.findall('abcd'))  # ['cd']

# 结尾是 '\n', 不是 'cd'
# print(p.findall('abcd\n'))  # []

# MULTILINE模式下, \Z不识别换行
# p2 = re.compile(r'cd\Z', flags=re.MULTILINE)
# print(p2.findall('abcd\nef'))  # []

# 只会找到一个(空的)匹配
# p = re.compile(r'\Z')
# print(p.findall('abcd\n'))  # ['']


# \n \t \\ \' \"  绝大部分Python的标准转义字符也被正则表达式分析器支持
# p = re.compile(r'\n')
# print(p.findall('\n'))  # ['\n']
#
# p = re.compile(r'\t')
# print(p.findall('\t'))  # ['\t']
#
# p = re.compile(r'\\')
# print(p.findall('\\'))  # ['\\']
#
# p = re.compile(r'\'')
# print(p.findall("'"))  # ["'"]
#
# p = re.compile(r'\"')
# print(p.findall('"'))  # ['"']


# []  用于表示一个字符集, 字符集可以单独列出, 比如[amk]匹配'a', 'm', 或者'k'
# p = re.compile(r'[amk]')
# print(p.findall('I have a monkey'))  # ['a', 'a', 'm', 'k']

# 可以表示字符范围, 通过用 - 将两个字符连起来
# p = re.compile(r'[a-y]')
# print(p.findall('ahzyqAHZYQ'))  # ['a', 'h', 'y', 'q']

# p = re.compile(r'[0-5][A-Y]')
# print(p.findall('a0hzyq125A6HZYQ'))  # ['5A']

# 特殊字符在字符集中, 失去它的特殊含义
# p = re.compile(r'[.+]')
# print(p.findall('abc'))  # []

# p = re.compile(r'[.+]')
# print(p.findall('a.b+c.d+'))  # ['.', '+', '.', '+']

# 特殊序列, 如 \d \s \w 在集合内可以被接受
# p = re.compile(r'[\d]')
# print(p.search('a1234b'))  # <re.Match object; span=(1, 2), match='1'>

# p = re.compile(r'[\d+]')
# print(p.findall('a1234b+'))  # ['1', '2', '3', '4', '+']

# p = re.compile(r'[a\sb]')
# print(p.findall('adb a bc'))  # ['a', 'b', ' ', 'a', ' ', 'b']

# p = re.compile(r'[\w]')
# print(p.findall('adb_a b!c'))  # ['a', 'd', 'b', '_', 'a', 'b', 'c']

# 不在字符集范围内的字符可以通过取反来进行匹配, 如果字符集首字符是^, 所有不在字符集内的字符将会被匹配, ^如果不在字符集首位, 就没有特殊含义
# p = re.compile(r'[^5]')
# print(p.findall('5a b512!5'))  # ['a', ' ', 'b', '1', '2', '!']

# p =re.compile(r'[^^]')
# print(p.findall('5a^b512!5'))  # ['5', 'a', 'b', '5', '1', '2', '!', '5']

# 如果要匹配 '[' ']', 可以在它之前加上反斜杠
# p = re.compile(r'[\[\]]')
# print(p.findall('[]'))  # ['[', ']']


# ( )  捕获分组, 匹配括号内的任意正则表达式, 并标识出该分组的开始和结尾
# 组从0开始编号, 组0始终存在, 它表示整个正则, Match的对象方法将组0作为默认参数; 子组从左到右编号, 从1向上编号
# 分组匹配的内容可以在之后其他分组用 \number 进行再次引用
# 要匹配字符 ( 或者 ) , 用 \( 或 \) ,或者把它们包含在字符集里: [(] [)]
# p = re.compile(r'b(.+)a(.+)e')
# m = p.match('babacdefg')
# print(m)  # <re.Match object; span=(0, 7), match='babacde'>
# print(m.group(0))  # babacde
# print(m.group(1), m.group(2))  # ab cd
# print(m.groups())  # ('ab', 'cd')
# print(m.span(1), m.span(2))  # (1, 3) (4, 6)
# print(m.start(1), m.end(1))  # 1 3
# print(m.start(2), m.end(2))  # 4 6

# 多个分组, 返回元组列表
# print(p.findall('babacdefg'))  # [('ab', 'cd')]

# 引用第1分组匹配的内容
# p = re.compile(r'b(.+)a(\1)e')
# print(p.findall('babaabefg'))  # [('ab', 'ab')]


# 用来表示一个特殊序列(由 \ 和一个字符组成的特殊序列)
# \ number  匹配数字代表的分组里面的内容(每个括号是一个子组, 子组从1开始编号), 在 [ 和 ] 字符集内, 任何数字转义都被看作是字符
# \1 匹配的内容和第1组一定一样
# p = re.compile(r'(.+) \1')
# print(p.search('ab abc'))  # <re.Match object; span=(0, 5), match='ab ab'>
# print(p.search('5 5'))  # <re.Match object; span=(0, 3), match='5 5'>

# 两个组匹配的内容不一定一样
# p = re.compile(r'(.+) (.+)')
# print(p.search('ab abc'))  # <re.Match object; span=(0, 6), match='ab abc'>
# print(p.search('5 5'))  # <re.Match object; span=(0, 3), match='5 5'>


# (?:)  非捕获分组, 并不创建新的组合, 所匹配的子字符串不能再执行匹配后被获取或是之后在模式中被引用
# string = 'I love apples and oranges.'
# p = re.compile(r'(?:I love )(\w+)')  # 在有捕获分组的情况下不会被捕获
# print(p.findall(string))  # ['apples']
#
# p = re.compile(r'(?:I love )?a')  # 在没有捕获分组的情况下货被捕获(可以当作普通的字符串)
# print(p.findall(string))  # ['I love a', 'a', 'a']


# (?=...)  前向肯定界定符, 并不创建新的组合, 且括号里的正则表达式匹配成功时才能继续匹配, 否则整个匹配失败
# 第一步: .+[.] 匹配成功
# 第二步: 前向肯定界定符匹配成功才继续第三步, 否则匹配失败
# 第三步: .+ 接着第一步继续匹配
# 最后结果为第一步和第三步匹配的结果
# p = re.compile(r'.+[.](?=exe$).+')
# m = p.match('ab.exe')  # 文件名必须以exe为后缀
# print(m)  # <re.Match object; span=(0, 6), match='ab.exe'>


# (?!...)  前向否定界定符, 并不创建新的组合, 且括号里的正则表达式匹配失败是才能继续匹配, 否则整个匹配失败
# 第一步: .+[.] 匹配成功
# 第二步: 前向否定界定符匹配失败才进行第三步, 否则匹配失败
# 第三步: .+ 接着第一步继续匹配
# 最后结果为第一步和第三步匹配的结果
# p = re.compile(r'.+[.](?!exe$|txt$).+')
# m = p.match('ab.txt')  # 文件名不能以exe或txt为后缀
# print(m)  # None


# Pattern.splot(string, maxsplit=0)
# string: 要匹配的字符串
# maxsplit: 最大分割次数, 默认为0, 表示不限制次数
# 按照匹配的子串将字符串分割, 以列表形式返回
# 如果有捕获分组, 那么分组了匹配的内容也会包含在结果中
# 如果匹配到字符串的开始, 那么结果将会以一个空字符串开始. 对于结尾也是一样
# p = re.compile(r'\W+')
# print(p.split('Words, Words, Words.'))  # ['Words', 'Words', 'Words', '']
#
# p = re.compile(r'(\W+)')
# print(p.split('Words, Words, Words.'))  # ['Words', ', ', 'Words', ', ', 'Words', '.', '']
#
# print(p.split('...Words, Words, Words.'))  # ['', '...', 'Words', ', ', 'Words', ', ', 'Words', '.', '']


# Patern.sub(repl, string, count=0)
# repl: 替换的字符串或者函数
# string: 要被匹配后替换的字符串
# count: 匹配后替换的最大次数, 默认为0, 表示替换所有的匹配
# p = re.compile(r'blue|white|red')
# 把每一个从左开始非重叠匹配的字符串用其他字符串替换
# print(p.sub('colour', 'blue socks and red shoes'))  # colour socks and colour shoes
# print(p.sub('colour', 'blue socks and red shoes', 1))  # colour socks and red shoes


# def func(matchobj):
#     print(matchobj)
#     if matchobj.group(0) == '-':
#         return ' '
#     else:
#         return '-'


# 把每一个从左开始非重叠匹配的对象作为参数传入函数调用
# 这个函数只能有一个匹配对象参数, 并返回一个替换字符串
# p = re.compile(r'-{1,2}')
# print(p.sub(func, 'pro----gram-files'))  # pro--gram files


# Pattern.subn(repl, string, count=0)
# 行为与 sub() 相同, 但是返回一个元组(字符串, 替换次数)
# p = re.compile(r'blue|white|red')
# print(p.subn('colour', 'blue socks and red shoes'))  # ('colour socks and colour shoes', 2)
# print(p.subn('colour', 'blue socks and red shoes', 1))  # ('colour socks and red shoes', 1)
#
#
# def func(matchobj):
#     print(matchobj)
#     if matchobj.group(0) == '-':
#         return ' '
#     else:
#         return '-'
#
#
# p = re.compile(r'-{1,2}')
# print(p.subn(func, 'pro----gram-files'))  # ('pro--gram files', 3)


# re.I / re.IGNORECASE  匹配时忽略大小写
# print(re.match(r'[a-z]+', 'aAbBcC', re.I))  # <re.Match object; span=(0, 6), match='aAbBcC'>


# re.X / re.VERBOSE  允许你编写更具可读性的正则表达式, 主要体现在分段、 添加注释、 空白符号
# p = re.compile(r'\d+\.\d*')
# p = re.compile(r"""
#                 \d +  # 匹配整数部分, re.X 使得该空格不影响
#                 \.    # 匹配小数点, re.X 使得可以分段写
#                 \d *  # 匹配小数部分, re.X 使得该空格不影响
#                 """, re.X)
# print(p.findall('1.2345.78'))  # ['1.2345']
