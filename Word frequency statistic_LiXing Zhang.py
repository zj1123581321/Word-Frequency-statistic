#coding=utf-8
'''
statistic words frequency of an essay written in English, and then output in order from large to small
'''

import re
#Regular expression operations
import collections
'''
Import the file and statistic words
'''
def count_word(path):
    result={}
    with open(path) as file_process:
        texts = file_process.read()
        # Capital to lowercase
        texts = texts.lower()
        # Using the regular expression to substitute special characters
        # Substitute " , . ! ?
        texts = re.sub("\"|,|\.|!|\?"," ",texts)

        for word in texts.split():
            if word not in result:
                result[word]=0
            result[word] +=1
        return result


'''
Sort by the word frequency 
'''
def sort_by_count(d):
    # OrderDict
    # need to learn more
    d = collections.OrderedDict(sorted(d.items(), key=lambda t: -t[1]))
    return d


file_name = "D:\My Nutshell\Python\Word frequency statistic_LiXing Zhang\Test.txt"

dword = count_word(file_name)
dword = sort_by_count(dword)

# Output top five words
# while 循环怎么设置条件遍历字典减少循环次数？
x=1
for key, value in dword.items():
    if x <= 5:
        print(key, value, sep=":")
        x += 1








