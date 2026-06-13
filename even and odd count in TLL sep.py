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
current.next=node(7)
current=current.next
even_count=0
odd_count=0
temp=head
while temp is not None:
    if temp.data%2==0:
        even_count+=1
    else:
        odd_count+=1
    temp=temp.next
print("even numbers:",even_count)
print("odd numbers:",odd_count)