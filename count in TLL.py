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
count=0
temp=head
while temp is not None:
    print(temp.data)
    count+=1
    temp=temp.next
print("Total Node=",count)