class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
for i in range(1,51):
    if i>1:
        is_prime=True
        for divisor in range(2,i):
            if i%divisor==0:
                is_prime=False
                break
        if is_prime:
            new_node=node(i)
        if head is None:
            head=new_node
            tail=new_node
        else:
             tail.next=new_node
             tail=new_node
count=0
temp=head
while temp and count<15:
    print(temp.data,end="->")
    temp=temp.next
    count+=1
print("None")