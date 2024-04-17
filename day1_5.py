def subjects():
    sub1= int(input("Enter the marks on math:  "))
    sub2 =int(input("Enter the marks of English "))
    sub3 =int(input("Enter the marks of science "))
    avg=(sub1+sub2+sub3)/3
    print(f"avg={avg}")
    if avg>=90 and avg<=100:
     print("Grade : A")
    elif avg>=80 and avg<=89:
     print(f"Grade : B")
    elif avg>=70 and avg<=79:
     print(f"Grade : C")
    elif avg>=60 and avg<=69:
     print(f"Grade : D")
    else :
     print(f"Grade : F") 

subjects()




