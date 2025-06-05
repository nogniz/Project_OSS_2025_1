class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date # 날짜를 받아서 저장
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"