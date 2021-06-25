class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def mergeTwoLists(self,l1,l2):   ## 1 -> 2 -> 4
        tmp = dummy = Node(0)        ## 1 -> 3 -> 4
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 :
            tmp.next = l1
        if l2:
            tmp.next = l2
        return dummy.next

    def mergeSort(self,head):
        if self.head is None or self.head.next is None:
            return head
        mid = self.midNode(head)
        newHead = mid.next
        mid.next = None
        l1 = self.mergeSort(head)
        l2 = self.mergeSort(newHead)
        return self.mergeTwoLists(l1,l2)


    def midNode(self,node):
        fast = node
        slow = node
        if node == None or node.next == None:
            return node
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def solve(self, A, B):
        lenL = 0
        head = thead = A

        # Calculate length of linked list
        while head is not None:
            head = head.next
            lenL += 1

        mid = (lenL // 2) + 1

        # Find kth node
        if B < mid:
            j = 0
            while thead is not None:
                if j == mid - B - 1:
                    return thead.val
                thead = thead.next
                j += 1
        else:
            return -1


    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr= itr.next
        return count

    def insertAt(self,index,val):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.insertAtBeginning(val)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(val,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insertAtBeginning(self,val):
        node = Node(val,self.head)
        self.head = node

    def insertAtLast(self,val):
        if self.head is None:
            self.head = Node(val,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val,None)

    def print(self):
        if self.head is None:
            print("Linkedlist is Empty")
            return
        itr = self.head
        while itr:
            if itr.next:
                print(itr.val,"->",end=" ")
            else:
                print(itr.val)
            itr = itr.next

    def addNumbersOfTwoLists(self,A,B):
        carry = 0
        arr = []
        p = A
        q = B
        while p or q:
            if p:
                i = p.val
            else:
                i = 0
            if q:
                j = q.val
            else:
                j = 0
            s = carry + i + j
            if s >= 10:
                carry = 1
                r = s % 10
                arr.append(r)
            else:
                carry = 0
                arr.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        if carry != 0:
            arr.append(carry)
        res = Node(arr[0])
        h1 = res
        for i in range(1,len(arr)):
            res.next = Node(arr[i])
            res = res.next

    def reverseList(self, A):
        head = A
        l = []
        while head:
            g = head.val
            l.append(g)
            head = head.next
        l.reverse()
        print(l)
        res = Node(l[0])
        h1 = res
        for i in range(1, len(l)):
            res.next = Node(l[i])
            res = res.next
        return h1

    def deleteDuplicates(self,A):
        head = A
        l = []
        while head:
            l.append(head.val)
            head = head.next
        q = []
        for i in l:
            if i not in q:
                q.append(i)
            else:
                q.remove(i)

        res = Node(q[0])
        h1 = res
        for i in range(1,len(q)):
            res.next = Node(q[i])
            res = res.next
        return h1


if __name__ == '__main__':
    obj = Linkedlist()
    first = Linkedlist()
    second = Linkedlist()
    first.insertAtLast(1)
    first.insertAtLast(1)
    first.insertAtLast(2)
    first.insertAtLast(3)
    first.insertAtLast(3)
    print(first.deleteDuplicates(first.head))

    first.print()



