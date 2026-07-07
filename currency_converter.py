print("1.USD to INR")
print("2.EUR to INR")
print("3.JPY to INR")
print("4.GBP to INR")

choice=input("Enter your choice:")
if choice=='1':
    inr=float(input("Enter usd:"))
    print("USD:",inr*86)
elif choice=='2':
    inr=float(input("Enter eur:"))
    print("EUR: ",inr*101)
elif choice=='3':
    inr=float(input("Enter jpy:"))
    print("JPY:",inr*0.60)
elif choice=='4':
    inr=float(input("Enter gbp:"))
    print("GBP",inr*117)
else:
    print("Invalid choice")
