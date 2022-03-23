class FreqStack:

    def __init__(self):
        self.cnt = {}       # count of each variable
        self.maxCnt = 0
        self.stacks = {}    # hashmap as stack of stacks

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res

        # Time Complexity - O(log n)
        # Space complexity - O(n)