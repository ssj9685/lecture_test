import os

arr=[]
for i in range(0,5):
    os.system('cls')
    num=int(input("번호 "))
    kor=int(input("국어 점수 : "))
    eng=int(input("영어 점수 : "))
    math=int(input("수학 점수 : "))
    phy=int(input("물리 점수 : "))
    sum=kor+eng+math+phy
    avg=sum/4
    grade=""
    if avg>90:
        grade="A"
    elif avg>80:
        grade="B"
    elif avg>70:
        grade="C"
    elif avg>60:
        grade="D"
    else:
        grade="F"
    arr.append("{}    {}    {}    {}    {}    {}    {:.2f}    {}\n".format(num,kor,eng,math,phy,sum,avg,grade))
print("===============================================\n")
print("번호  국어  영어  수학  물리  총점  평균  학점\n")
print("===============================================\n")
for i in range(0,5):
    print(arr[i])