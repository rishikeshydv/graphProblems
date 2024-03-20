''' 
"Currency Arbitrage" - Given exchange rates between different currencies, 
implement a function to determine if there's an arbitrage opportunity. Return true if there's a way to 
execute trades resulting in a profit, otherwise return false.

Example: 
    USD  NPR  IND
[USD  1   133  89]
[NPR 0.2   1   0.8 ]
[IND 0.4   1.6  1]
    

currencyExchanges = [["USD",1,133,89],["NPR",0.2,1,0.8],["IND",0.4,1.6,1]]
'''
from typing import List
class Solution:
    def __init__(self,currencyExchanges:List[str]):
        self.edgeTo={i[0]:[] for i in currencyExchanges}
        self.arbitrage = ""
        self.currencyExchanges=currencyExchanges
        self.currencyOrder = ["USD","NPR","IND"]
        for i,exchanges in enumerate(self.currencyExchanges):
            for j,element in enumerate(exchanges):
                if element == "1":
                    continue
                if self.currencyOrder[j-1] == exchanges[0]:
                    continue
                self.edgeTo[exchanges[0]].append(["NPR",element])
    def currencyArbitrage(self):
        return self.edgeTo
            
sol = Solution([["USD",'1','133','89'],["NPR",'0.2','1','0.8'],["IND",'0.4','1.6','1']])
print(sol.currencyArbitrage())


    



