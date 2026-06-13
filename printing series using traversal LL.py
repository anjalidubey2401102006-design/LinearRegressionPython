class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next