class ATM(object):
    def __init__(self,totalCash,cashWithdrawl,balanceEnquiry,cashDrawn):
        self.totalCash=totalCash
        self.cashWithdrawl=cashWithdrawl
        self.balanceEnquiry=balanceEnquiry
        self.cashdrawn=cashDrawn
    def printATMDetails(self):
        print("Total amount in the ATM is ",self.totalCash)
        print("Total cash withdrawl is ",self.cashWithdrawl)
        print("Total balance in the ATM is ",self.balanceEnquiry)
        print("Total cash placed is ",self.cashdrawn)
a1=ATM("$100","$50","$50","$20")
a2=ATM("$1000","$200","$800","$500")
a3=ATM("$5000","$2500","$2500","$2500")
print("\nDetails Of ATM1:")
a1.printATMDetails()

print("\nDetails Of ATM2:")
a2.printATMDetails()

print("\nDetails Of ATM3:")
a3.printATMDetails()