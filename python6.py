# 1. Exception handling
# 2. Try: the code which we think might get error we will write in try block
# 3. except:
# 4. else:
# 5. finally:


# try:
#     print(a)
# except NameError:  # using attribute NameError is used for a specific type of error 
#     print("a is not defined") 
# except:
#     print("not defined")


# try:
#     a=x/y
# except ZeroDivisionError:
#     print("denominator cannot be zero")
# except:
#     print("something is wrong")
# finally:
#     print("No one can stop me")



# try:
#     f = open("koc31.txt","w")
#     try:
#         f.write("hello class")
#     except:
#         ("Error during writing")
#     finally:
#         f.close()
# except:
#     print("Error in the opening file")


# try:
#     print("hello class")
# except:
#     print("Error")
# else:
#     print("working")



f1 = open("logo.png","rb")
f2 = open("abc.png","wb")
for x in f1:
    f2.write(x)



















