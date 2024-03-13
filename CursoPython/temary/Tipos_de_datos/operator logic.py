#and both options they be correct for what return true

option1 = True & True
option2 = True & False
option3 = (2 == 2) and (2 == 2) #return true
option4 = (3 > 4) and (2 > 4) #return folse

#or if one of the options is true return true because only is necesary that be one true, 
option5 = True or False or False 
option6 = False or False or False or False 
option7 = (5 == 5) or (4 < 3) or (5 < 3) #return true
option8 = (2 == 5) or (4 < 3) or (5 < 3) or (8 == 9) #return folse


#not invert de return, for example yes the option9 he was coming bact true, now return folse (invert of the result)
option9 = not "hola" == "hola"


print(option9)


