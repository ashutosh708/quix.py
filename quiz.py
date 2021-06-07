print("Welcome to quiz")
print("")
score=0
Q1="""1. what is the sum of 13 and 34
a.54
b.47
c.74
d.67"""




Q2="""1. what is the sum of 2 and 4

a.5
b.4
c.7
d.6
"""


Q3="""1. what is the product of 2 and 4

a.52
b.4
c.8
d.16
"""


questions={Q1:"b",Q2:"d",Q3:"c"}
name=input("enter your name")
print("welcome",name,"to our quiz")
score=0
for item in questions:
    print(item)#() small bracket is used to enter the key (e.g. Q1)
   
    ans=input("Enter the correct option:(a/b/c/d)")
    if ans==questions[item]:#[] big bracket is used to enter the value(e.g. "b")
        print("correct answer")
        score=score+1
        print("your current score=",score )
    else:
        print("wrong answer")
        print("Your current answer=",score)

print("your final answer=",score)


