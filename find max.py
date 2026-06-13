class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(15)
head.next=node(50)
head.next.next=node(15)
head.next.next.next=node(10)
max_n=head.data
temp=head
while temp :
    if temp.data>max_n:
        max_n=temp.data
    temp=temp.next
print("Maximum number:",max_n)