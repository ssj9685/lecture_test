a=input("첫 번째 정수: ")
b=input("두 번째 정수: ")
op=input("연산자: ")
if op is "+":
    print("{} + {} = {}".format(a,b,int(a)+int(b)))
elif op is "-":
    print("{} - {} = {}".format(a,b,int(a)-int(b)))
elif op is "*":
    print("{} * {} = {}".format(a,b,int(a)*int(b)))
elif op is "/":
    print("{} / {} = {}".format(a,b,int(a)/int(b)))
elif op is "%":
    print("{} % {} = {}".format(a,b,int(a)%int(b)))
else:
    print("error wrong operator")