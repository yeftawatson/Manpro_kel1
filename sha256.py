# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib

# initializing string
str = "I won a lottery."
str2 = "i won a lottery."
str3 = "i  won a lottery."

str = str.lower()
str2 = str2.lower()
str3 = str3.lower()

str = str.replace(" ","")
str2 = str2.replace(" ","")
str3 = str3.replace(" ","")
# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())
result2 = hashlib.sha256(str2.encode())
result3 = hashlib.sha256(str3.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())

if(result.hexdigest() == result2.hexdigest()):
    print("res1 == res2")

print ("\r")

#BANDINGKAN SAMA HASH GENERATOR DI LINK: https://emn178.github.io/online-tools/sha256.html

# initializing string
# str = "GeeksforGeeks"

# # encoding GeeksforGeeks using encode()
# # then sending to SHA384()
# result = hashlib.sha384(str.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA384 is : ")
# print(result.hexdigest())

# print ("\r")

# # initializing string
# str = "GeeksforGeeks"

# # encoding GeeksforGeeks using encode()
# # then sending to SHA224()
# result = hashlib.sha224(str.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA224 is : ")
# print(result.hexdigest())

# print ("\r")

# # initializing string
# str = "GeeksforGeeks"

# # encoding GeeksforGeeks using encode()
# # then sending to SHA512()
# result = hashlib.sha512(str.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA512 is : ")
# print(result.hexdigest())

# print ("\r")

# # initializing string
# str = "GeeksforGeeks"

# # encoding GeeksforGeeks using encode()
# # then sending to SHA1()
# result = hashlib.sha1(str.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA1 is : ")
# print(result.hexdigest())
