# website: https://rohallaheghbali.ir/  |  instagram: eghbaliit  | youtube: rohallaheghbali

# 5 -> 5*4*3*2*1 = 120

user_input = int(input("Enter your Number: "))
fact = 1

print(type(user_input))

if user_input > 1:
    for i in range(1, user_input+1): # 1,2,3,4
        fact *= i # fact = fact * i
    
    print(fact)
else :
    print("user input is not vlaid")