class node:
    def __init__(self,data):
        self.data=data
        self.next=None
num=int(input("enter the number of nodes:"))
head=None
current=None
for i in range(num):
    value=int(input("enter the node:"))
    new_node=node(value)
    if head is None:
        head=new_node
        current=new_node
    else:
        current.next=new_node
        current=new_node
    max_num=head.data
    temp=head
    while temp:
        if temp.data>max_num:
            max_num=temp.data
        temp=temp.next
print("maximum number",max_num)