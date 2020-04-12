#class to implement queue
class Queue:
    def __init__(self,size):
        self.queue=[None] *size
        self.front=-1
        self.rear=-1
        self.size=size
    #function to check empty stack
    def isEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False
    #function to check full stack
    def isFull(self):
        #if next of rare is front then stack is full
        if ((self.rear+1)%(self.size))==self.front:
            print("queue is full")
            return True
        else:
            return False
    #function to insert element into queue in rear side   
    def Enqueue(self,data):
        if self.isFull():
            return
        elif (self.isEmpty()):
            self.front=0
            self.rear=0
            self.queue[0]=data
        else:
            #increment rear
            #use of array in circular fashion to effeciently use space in array
            self.rear=(self.rear+1)%(self.size)
            self.queue[self.rear]=data

    #function to remove element from front
    def Dequeue(self):
        if (self.isEmpty()):
            print("queue is empty")
            return
        #if queue contains single element after removing make queue empty
        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            #update front of queue
            self.front=(self.front+1)%(self.size)
            return temp
    #function to return front element of queue        
    def Front(self):
        if self.isEmpty(): 
            print("Queue is empty") 
        else:
            print("Front item is", self.queue[self.front]) 
    #function to return last element of queue
    def Rear(self):
        if self.isEmpty():
            return
        else:
            print("rear item is",self.queue[self.rear])
    #function to print elements of queue in inserted order
    def print_queue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        if self.front==0 and self.rear==0:
            print(self.queue[0])
            return
        current=self.front
        print("front element is"+str(self.queue[current]))
        while(True):
            print(self.queue[current])
            current=(current+1)%(self.size)
            if(current==self.rear):
                print(self.queue[current])
                break

if __name__=="__main__":
    que=Queue(10)
    que.Enqueue(1)
    que.Enqueue(2)
    que.Enqueue(3)
    que.Enqueue(4)
    que.Enqueue(5)
    que.print_queue()
    print("dequed element is"+str(que.Dequeue()))
    print("dequed element is"+str(que.Dequeue()))
    que.print_queue()
    que.Front()
    que.Rear()
    
    





