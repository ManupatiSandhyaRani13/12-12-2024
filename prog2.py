sal=int(input('Enter basic salary:'))
if sal < 10000:
    hra=(67*sal)/100
    da=(73*sal)/100
# elif sal >10000 and sal < 20000: can also wrirtten as---
elif sal <20000:
    hra=(69*sal)/100
    da=(76*sal)/100
else:
    hra=(73*sal)/100
    da=(89*sal)/100
gs=hra+da+sal
print('The Gross Salary is :',gs)
