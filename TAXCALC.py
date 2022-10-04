# BASIC TAX Calculator
# Slab: OLD Regime
# Author: Vijay Reddy

T_Inc=int(input("Enter Total Income before TDS:"))
B_TDS=int(T_Inc/12)
#print(T_Inc)
T_Ded=int(input("Enter Total deduction:"))
Tax_Inc=T_Inc-T_Ded
print("Total Taxable income:",Tax_Inc)
print("Total earning before TDS:",B_TDS)
if Tax_Inc>250000:
    if Tax_Inc>500000:
        if Tax_Inc>1000000:
            brac1=(Tax_Inc-1000000)*0.3
            print("Total Tax to pay:",int(brac1+112500))
            print("Estimated Inhand Salary:",int((T_Inc-brac1)/12))
        else:
            brac2=(Tax_Inc-500000)*0.2
            print("Total Tax to pay:",int(brac2+12500))
            print("Estimated Inhand Salary:",int((T_Inc-brac2)/12))
    else:
        brac3=(Tax_Inc-250000)*0.05
        print("Total Tax to pay:",int(brac3))
        print("Estimated Inhand Salary:",int((T_Inc-brac3)/12))
else:
    print("Not applicable for tax deduction !!")
