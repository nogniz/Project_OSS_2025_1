import datetime
from expense import Expense # Expense 클래스가 expense.py 파일에 있다고 가정합니다.

class Budget:
    def __init__(self):
        self.expenses = []

    
    def add_expense(self, date_str, category, description, amount):
        
        expense = Expense(date_str, category, description, amount) 
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
       
        try: 
            sorted_expenses = sorted(self.expenses, key=lambda x: x.date)
        except Exception:
            sorted_expenses = self.expenses

        for idx, e in enumerate(sorted_expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")