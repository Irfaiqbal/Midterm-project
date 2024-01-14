print('''
1. add
2. subtract
3. multiply
4. divide
''')

num1=int(input("enter your number value num1"))
num2=int(input("enter your number value num2"))
print("""Select the option 1. add
2. subtract
3. multiply
4. divide
""")
opr=input("enter your opr...")
if opr == "1":
    print(num1+num2)
elif opr =="2":
    print(num1-num2)
elif opr == "3":
    print (num1*num2)
elif opr =="4":
    print(num1/num2)
else:
    print("invalid opr..")
