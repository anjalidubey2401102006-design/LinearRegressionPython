class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n1=None
for num in range(1,21):
    if num !=10:
     new_node=node(num)
    if head is None:
       head=node(num)
       n1=head
    else:
       n1.next=new_node
       n1=n1.next
temp=head
while temp:
   print(temp.data,end="->")
   temp=temp.next
print("None")