print("Roman numeral to Integer Calculator.")
#Defining a function to convert roman numerals into integers.
def romanToInt(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} #All possible Values
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
      return num
while True:
      x = input("Enter an number in Roman Numeral(in capital letters): ")
      print("Value in integer is=",romanToInt(x))
      
#Asking user whether he wants another calculation.
      choice = input("Do you want next calculation?(YES/NO)")

      if choice == "YES":
            continue
      else:
            print("Thank you!")
            break