from os import system
from email_config import send_email



s=system("python DT_Test_Case.py")
assert  s==0, send_email() 
 

if s==True:
	send_email()
	
	
	

else:
	print("Test Case Run Successfully")


  
  

 


 
  