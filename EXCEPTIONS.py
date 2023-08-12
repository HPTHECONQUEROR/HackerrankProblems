try:
   i=int(input('age= '))
   print(1/i)

except ValueError:
    print("PRINT CLEAR VALUE")
except ZeroDivisionError:
    print("dont enter zero")


'''THIS IN TRY EXCEPT METHOD IT IS USED FOR NOT RETURNING ANY ERROR MESSAGE 
AND ONLY RETURNING OUR GIVEN STATEMENT'''