I=int(input("Enter Num1:"))
J=int(input("Enter Num2:"))
print("1.Sum")
print("2.Sub")
print("3.Mul")
print("4.Div")
L=int(input("Enter any Option:"))
if L==1:
    def sum():
        K=I+J
        print(K)
    sum()
elif L==2:
    def Sub():
        K=I-J
        print(K)
    Sub()
elif L==3:
    def Mul():
        K=I*J
        print(K)
    Mul()
elif L==4:
    def Div():
        K=I/J
        print(K)
    Div()
else:
    print("Select a valid option")
