class node:
    def __init__(self,data):
        self.data=data
        self.next=None
num=int(input("enter the number of nodes:"))
head=None
current=None
for i in range(num):
    number=int(input("enter the node:"))
    new_node=node(number)
    if head is None:
        head=new_node
        current=new_node
    else:
        current.next=new_node
        current=new_node
    min_num=head.data
    temp=head
    while temp:
        if temp.data<min_num:
            min_num=temp.data
        temp=temp.next
print("minimum number:",min_num)