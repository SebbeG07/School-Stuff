Yes=int (input ("Hur många poäng fick du: "))
A=45
B=40
C=35
D=30
E=25
if Yes<E:
    print ("Du fick F i betyg")
elif Yes>=25 and Yes<30:
    print ("Du fick E i betyg")
elif Yes>=30 and Yes<35:
    print ("Du fick D i betyg")
elif Yes>=35 and Yes<40:
    print ("Du fick C i betyg")
elif Yes>=40 and Yes<45:
    print ("Du fick B i betyg")
elif Yes>=45 and Yes<50:
    print ("Du fick A i betyg")
else:
    print ("Fuskare! Shame!")