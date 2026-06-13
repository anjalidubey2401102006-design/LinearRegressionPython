class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
current=head
current.next=node(20)
current=current.next
current.next=node(30)
current=current.next
current.next=node(40)
current=current.next
current.next=node(50)
current=current.next
k=60
temp=head
while temp :
    if temp.data==k:
        print("element found")
        break
    temp=temp.next
else:
    print("element not found")