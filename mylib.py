def input_int(msg):
    while(True):
        try:
            v=int(input("enter any value:"))
            return(v)
        except ValueError as e:
            print("please enter integer only...")
# for raising error for strings 
def input_str(msg):
 while(True):
  try:
   v=input(msg)
   if(not v.isalpha()):
    raise(Exception("please input alphabets only"))
   return(v)
  except Exception as e:
   print(e)