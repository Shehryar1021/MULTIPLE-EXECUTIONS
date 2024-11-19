
try :
 num1 = int(input("ENTER A NUMBER : "))
 num2 = int(input("ENTER A NUMBER : "))
 result=num1/num2
 print("RESULT IS : ",result)
except ZeroDivisionError:
 print("DIVISION BY ZERO IS NOT ALLOWED")
except ValueError:
 print("PLEASE ENTER NUMERICAL VALUE")
except NameError as ex:
 print("THE EXCEPTION IS : ",ex)

except:
 print("SOME ERROR OCCURED")
finally:
 print("I WILL EXECUTE NO MATTER WHAT HAPPENS")