class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(1)
current=head
current.next=node(2)
current=current.next
current.next=node(3)
current=current.next
current.next=node(4)
current=current.next
current.next=node(5)
current=current.next
current.next=node(6)
current=current.next
temp=head
while temp is not None:
    if temp.data % 2 == 0:
        print(temp.data)
    temp=temp.next