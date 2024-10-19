import random
passlen = int(input("enter the length of password : "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-?><:"
p =  "".join(random.sample(s,passlen ))
print("Your random security password is: "p)
