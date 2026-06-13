class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(2)
current=head
current.next=node(4)
current=current.next
current.next=node(6)
current=current.next
current.next=node(8)
current=current.next
current.next=node(10)
current=current.next
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next