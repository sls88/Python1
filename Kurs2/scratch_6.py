def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0
a = [i for i in range(31)] # [0, 1, 2, ... , 30]

class multifilter:
    def judge_half(pos, neg):
        pos=pos
        neg=neg
        if pos>=neg:
            return True
    def judge_any(pos, neg):
        pos=pos
        neg=neg
        if pos>=1:
            return True
    def judge_all(pos, neg):
        pos=pos
        neg=neg
        if neg==0:
            return True
    def __init__(self, a, *funcs, judge=judge_any):
        self.a=a
        self.funcs=funcs
        self.judge=judge
    def __iter__(self):
        self.pos = 0
        self.neg = 0
        for x in self.a:
            self.s = [f(x) for f in self.funcs]
            for i in self.s:
                if i==True:
                    self.pos+=1
                else:
                    self.neg+=1
            if self.judge(self.pos, self.neg)!=True:
                self.pos = 0
                self.neg = 0
                continue
            else:
                self.pos = 0
                self.neg = 0
                yield x

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_any)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
