from heaps import MaxHeap

class Debt:
    def __init__(self, borrower, lender, amt) -> None:
        self.borrower=borrower
        self.lender=lender
        self.amt=amt

    def __str__(self) -> None:
        return f'{self.borrower} owes {self.lender} Rs.{self.amt}'
    
# class Pay:
#     def __init__(self, borrower, lender, amt) -> None:
#         self.borrower=borrower
#         self.lender=lender
#         self.amt=amt

#     def __str__(self) -> None:
#         return f'{self.borrower} pays {self.lender} Rs.{self.amt}'

class Ledger:
    def __init__(self) -> None:
        self.people=set()
        self.ledger=[]

    def __getitem__(self, idx) -> Debt:
        return self.ledger[idx]
    
    def __len__(self) -> int:
        return len(self.ledger)
    
    def get_people(self) -> int:
        return len(self.people)
    
    def __str__(self) -> None:
        return f"The Ledger currently handles {len(self.people)}\'s debts."

    def addDebt(self, borrower, lender, amt) -> None:
        debt=Debt(borrower, lender, amt)
        # print(debt)
        self.people.add(borrower)
        self.people.add(lender)

        self.ledger.append(debt)

    def printLedger(self):
        for i in self.ledger:
            print(i)

    def solve(self):
        # print('Finding the Minimum Cashflows!')
        sol=self._solve()
        return sol
        # for i in sol:
            # print(i)

    def _solve(self):
        val={}
        for n in self.people:
            val[n]=0

        for debt in self.ledger:
            val[debt.borrower]-=debt.amt
            val[debt.lender]+=debt.amt

        pos_heap=MaxHeap(self.get_people())
        neg_heap=MaxHeap(self.get_people())

        for name, amt in val.items():
            if amt>0:
                pos_heap.insert([name, amt])
            else:
                neg_heap.insert([name, -amt])
                val[name]*=-1


        newEdges=[]
        while not pos_heap.empty() and not neg_heap.empty():
            
            mx=pos_heap.extractMax()
            mn=neg_heap.extractMax()
            # print(mx, mn)

            amt=min(mx[1], mn[1])
            to=mx[0]
            from_=mn[0]

            newEdges.append(Debt(from_, to, abs(amt)))
            val[to]-=amt
            val[from_]-=amt

            if mx[1]>mn[1]:
                pos_heap.insert([to, val[to]])
            elif mx[1]<mn[1]:
                neg_heap.insert([from_, val[from_]])

        return newEdges


# l=Ledger()
# l.addDebt('Yash', 'Riddhi', 10)
# l.addDebt('Riddhi', 'Anisha', 5)
# l.addDebt('Pranya', 'Riddhi', 8)
# l.addDebt('Yash', 'Anisha', 5)
# l.addDebt('Yash', 'Riddhi', 10)

# l.solve()