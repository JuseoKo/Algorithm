"""
이진트리
전위 순회 : 루트 -> 왼쪽 -> (위에서 아래)오른쪽
중위 순회 : 왼쪽-> 루트 -> 오른쪽
후위 순회 : 왼쪽 -> 오른쪽 -> 루트

A B C
B D .
C E F
E . .
F . G
D . .
G . .
                A
            B         C
         D         E      F
                             G

"""
import sys

n = int(sys.stdin.readline())
# 0 = 부모 노드 , 1 = 왼쪽 자식 노드, 2 = 오른쪽 자식 노드
tree = {}
for i in range(n):
    root, left, right = sys.stdin.readline().rstrip().split(" ")
    tree[root] = [left, right]
# print(tree)


def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
