class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# creating nodes 
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
#linking the nodes
n1.next=n2
n2.next=n3
n3.next=n4
#print the linked list
temp=n1
while temp:
    print(temp.data,end=" ->") 
    temp=temp.next
print("None")