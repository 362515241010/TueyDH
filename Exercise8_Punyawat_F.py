#!/usr/bin/env python
# coding: utf-8

# In[9]:


#นาย ปุณยวัจน์ เฟื่องฟุ้ง 362515241010 EE36241N
u=input("Username :")
p=input("Password :")
if u=="wasd" and p=="1111":
    print("Welcome to Icecream Shop.")
    print("-------------------Menu-------------------")
    print("Welcome to Icecream Shop")
    print("1. Strawberry 80 THB")
    print("2. Vanila 50 THB")
    print("3. Chocolate 40 THB")
    print("4. Lemon 90 THB")
    print("5. Milk 10 THB")
    s=80
    v=50
    c=40
    l=90
    m=10
    ice=int(input("What do you want?(1-5) : "))
    num=int(input("How many do you want? : "))
    if ice==1:
        print("You order ",num," of Strawberry ",s*num, " THB")
    elif ice==2:
        print("You order ",num," of Vanila ",v*num, " THB")
    elif ice==3:
        print("You order ",num," of Chocolate ",c*num, " THB")
    elif ice==4:
        print("You order ",num," of Lemon ",l*num, " THB")
    elif ice==5:
        print("You order ",num," of Milk ",m*num, " THB")
    
else :
    print("Error ,please try again.")


# In[ ]:




