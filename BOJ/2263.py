import sys
sys.setrecursionlimit(10 ** 6)


def func(in_l, in_r, po_l, po_r):
    if in_l > in_r or po_l > po_r:
        return
    root = postorder[po_r]
    print(root, end=' ')
    tmp = idx[root]
    left = tmp - in_l
    func(in_l, tmp - 1, po_l, (po_l + left) - 1)
    func(tmp + 1, in_r, po_l + left, po_r - 1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
idx = [0] * (N + 1)
for i in range(N):
    idx[inorder[i]] = i
func(0, N - 1, 0, N - 1)
