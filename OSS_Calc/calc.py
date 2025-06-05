import tkinter as tk
# import math # 이전 기능에서 사용되었으나 현재 코드에는 필요 없어 주석 처리

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x450") # 버튼 추가 공간 확보

        self.expression = ""
        self.last_result = "" # 이전 결과를 저장할 변수 추가

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성 (이전 결과 불러오기 버튼 추가)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Prev', '='] # 'Prev' 버튼 (이전 결과 불러오기) 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            # self.last_result = "" # 이 줄을 주석 처리하거나 삭제합니다.
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.last_result = result
                self.expression = result
            except Exception:
                self.expression = "에러"
                self.last_result = "" # 에러 시에는 결과가 없으므로 초기화 유지
        elif char == 'Prev':
            if self.last_result:
                 self.expression += self.last_result
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

