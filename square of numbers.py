class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n1=None
for num in range(1,11):
    square= num**2
    if head is None:
            head=node(square)
            n1=head
    else:
            n1.next=node(square)
            n1=n1.next
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("None")
