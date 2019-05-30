import re
#match function
pattern = re.compile('ell')
print(pattern.match('hello world'))
print(pattern.match('hello world', 1))

#result = print(pattern.match('hello world', 1))
#print("Result: ", result)


#search function
print(pattern.search('hello world'))
print(pattern.search('hello world', 1))
print(pattern.search('hello world', 2))


#advanced expressions
string1 = "Hello World is awesome"
result = re.search(r'(.*) world (.*?) .*', string1, re.M|re.I)   #M for multiline, I for case-insensitive
if (result):
    print("Found", result.group())
    print("Found", result.group(1))
    print("Found", result.group(2))
else:
    print("No Result")


#search and replace
string2 = "Search and Destroy - 843574o7etruhergierw7843t078wergui"

result = re.sub(r'\D', "", string2)   #remove all digits
print(result)



