class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=[10,20,30,40]
head=node(arr[0])
current=head
for i in range(1,len(arr)):
    current.next=node(arr[i])
    current=current.next
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next