my_name = 'Andres'
my_age= 33
my_height=68    #inches
my_weight= 250 #pounds
my_eyes= 'brown'

printf{f"My name is.. {my_name}."}
printf{f"I'm {my_height} inches tall."}
print{"Which is actually not very tall."}
printf{f"I also have {my_eyes}  eyes!"}
printf{f"Printf is neat! I can even do arithmetic..like  1+1={1+1}"}
print{"Print is very powerful as well!"}

q = 1001
p = 0.111
print(q,p,p*q)
# Output - 1001 .111 1001.111

print(q,p,p*q, sep=",")
# Output - 1001,.111,1001.111

print(str(q) + " " + str(p) + " " + str(p * q))
# Output - 1001 .111 1001.111
