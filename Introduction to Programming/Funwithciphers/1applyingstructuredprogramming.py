'''
Created on 24 jan. 2017

@author: tos340
'''
lst = [
"1101000",
"1100101",
"1101100",
"1101100",
"1101111"
]
#By using your function to decimal you can now decode the message.
msg = ""
for b in lst:
decimal_value = to_decimal(b)
msg += chr(decimal_value)
print(msg)
