name=input("enter your name")
gender=input("enter your gender male or female")
age=int(input("enter your age "))
purchase=0
product=input("enter product name")

product_gram=float(input("enter product gram"))
current_product_price=5752
total_rate=product_gram*current_product_price

print("total rate is ",total_rate) 
purchase_amt=int(input("enter perchase amt")) 

if age>65 and gender=="male":
    
    if purchase>200000:
        discount=20
        print("you get 20 per discount")    
        print()
    elif purchase>300000:
        discount=30
        print("you get 30 per discount")
        print()
    else :
        discount=35
        print("you get 35 per discount")
        print()
if age<65 and gender=="male":
    
    if purchase>200000:
        discount=10
        print("you get 10 per discount")
        print()    
    elif purchase>300000:
        discount=20
        print("you get 20 per discount")
        print()
    else :
        discount=25
        print("you get 25 per discount")
        print()        
if age>65 and gender=="female":
    
    if purchase>200000:
        discount=25
        print("you get 25 per discount")
        print()    
    elif purchase>300000:
        discount=35
        print("you get 35 per discount")
        print()
    else :
        discount=40
        print("you get 40 per discount")
        print()
if age<65 and gender=="female":
    
    if purchase>200000:
        discount=15
        print("you get 15 per discount")
        print()    
    elif purchase>300000:
        discount=25
        print("you get 25 per discount")
        print()
    else :
        discount=30
        print("you get 30 per discount")
        print()        
        print()
  
m_charge=0
m_charge=product_gram*845

print("m_charge is",m_charge)


total_amount=0
total_amount=total_rate+m_charge
print("total amount is ",total_amount)

discount=0
discount=int(input("enter a discount"))
discount=(total_amount*discount)/100
print("discount is ",discount)


total_net_amount=0
total_net_amount=total_amount-discount
print("total net amount is ",total_net_amount)





               
        
        
            
    
    
        
        
    
    
    
