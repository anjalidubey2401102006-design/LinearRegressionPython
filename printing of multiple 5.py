class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(5)
n1=head
for num in range(10,55,5):
    n1.next=Node(num)
    n1=n1.next
temp=head 
while temp is not None:
    print(temp.data,end="->")
    temp=temp.next
print("None")