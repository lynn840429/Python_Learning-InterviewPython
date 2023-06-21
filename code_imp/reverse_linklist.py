class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

print("root: ")
root = link
while root:
    print(root.data)
    root = root.next

print("rev root: ")
root = rev(link)
while root:
    print(root.data)
    root = root.next

######################################
class ListNode:
	def __init__(self,x=None, next=None):
		self.val = x
		self.next = next
	
def recurse(head, newhead):    #递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        pass
    if head.next is None:
        newhead = head
    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None
        head.next = ListNode(None, None)
    return newhead
	

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
newhead = ListNode(None, None)

p = recurse(head, newhead);           #输出链表4->3->2->1->None
print("\nver 2:")
while p:
	print(p.val)
	p = p.next
