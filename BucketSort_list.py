"""
Bucket sort using array of buckets, and each bucket holding a linkedlist

"""
class Sorting:
    def bucket_sort(self, nums):
        buckets = [None for x in range(10)]
        
        # Insert items into appropriate buckets
        for value in nums:
            newNode = Node(value)
            index = int(value * len(buckets))

            if buckets[index] is None:
                buckets[index] = newNode
            else:
                current = buckets[index]
                if current is not None:
                    while current.next is not None:
                        current = current.next
                    current.next = newNode
        result = []
        for bucket in buckets:
            if bucket is not None:
                result.append(self.insertion_sort_linkedlist(bucket))
        return result

    def insertion_sort_linkedlist(self, head):
        if head is None:
            return None

        current = head
        tail = None
        while current is not None and tail != head:
            next = current
            while next.next != tail:
                if next.val <= next.next.val:
                    next.val, next.next.val = next.next.val, next.val
                next = next.next
            tail = next
            current = head
        
        while head.next is not None:
            head = head.next

        return head

class Node:
    __slots__ = 'val', 'next', 'prev'

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    def __repr__(self):
        return "[" + str(self.val) + "]"
    
if __name__ == "__main__":
    app = Sorting()
    sorted = app.bucket_sort([0.4, 0.8, 0.2, 0.6, 0.1, 0.5])
    print(sorted)
