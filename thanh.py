class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, left, right):
        # Find minimum on interval [left, right)
        left += self.n
        right += self.n
        min_val = float('inf')
        while left < right:
            if left % 2:
                min_val = min(min_val, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                min_val = min(min_val, self.tree[right])
            left //= 2
            right //= 2
        return min_val

def find_SX(A):
    N = len(A)
    seg_tree = SegmentTree(A)
    result = []

    for X in range(1, N + 1):
        max_min = float('-inf')
        for i in range(N - X + 1):
            min_val = seg_tree.query(i, i + X)
            max_min = max(max_min, min_val)
        result.append(max_min)

    return result

n = int(input())
A = list(map(int, input().split()))
# Example usage:
# A = [1, 2, 3, 4, 5, 4, 6, 2, 1, 2]
print(*find_SX(A))  # Output should match the example output in the problem statement

# 10
# 1 2 3 4 5 4 6 2 1 2
# 5
# 1 2 3 4 5