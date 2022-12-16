class MyQueue:
    def newstackB(self):
        if self.B == []:               
            while self.A:
                self.B.append(self.A.pop(-1))      
    def __init__(self):
        self.A, self.B = [], [] 
    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        self.newstackB()
        return self.B.pop(-1)  
    def peek(self) -> int:
        self.newstackB()
        return self.B[-1]        

    def empty(self) -> bool:
        return len(self.A) + len(self.B) == 0
