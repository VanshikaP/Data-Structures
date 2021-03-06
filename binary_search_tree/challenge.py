"""
Print out each element of the following array on a separate line:
```
["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
```
You may use whatever programming language you'd like. 
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

# Understanding
# 1. Input - array - ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
# 2. Output - 
# "Joe
# 2
# Ted
# 4.98
# 14
# ...
# 5006"

# Plan and Execute

def printList(items):
    # iterate over the list
    for item in items:
        # print each item
        print(item)

sampleInput = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

printList(sampleInput)
