class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=[10,20,30,40]
n1=Node(arr[0])
n2=Node(arr[1])
n3=Node(arr[2])
n4=Node(arr[3])
#linking the nodes
n1.next=n2
n2.next=n3
n3.next=n4
temp=n1
while temp:
    print([temp.data],end="->")
    temp=temp.next
print("None")