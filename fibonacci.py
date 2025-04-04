class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("ERROR: Input must be an integer.")
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration

        if self.n < 0:
            raise StopIteration

        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
