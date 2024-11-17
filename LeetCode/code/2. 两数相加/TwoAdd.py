# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    #l1和l2是两个链表,carray是进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:
            # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s=carry+l1.val+(l2.val if l2 else 0)
            # 节点值和进位加在一起
        carry=s//10
        l1.val=s%10 
        l1.next=self.addTwoNumbers(l1.next,l2.next if l2 else None,carry)
        return l1
    def input_linked_list(self,max_retry=3):
                """
                用于获取用户输入构建链表的方法，添加了输入错误次数限制以及数字范围验证
                """
                retry_count = 0
                while True:
                     input_str=input("请输入数字序列，以空格分隔：")
                     if not input_str.strip():
                        return None
                     values=input_str.split()
                     head=None
                     tail=None
                     for value in values:
                        try:
                            val=int(value)
                            if not (0<=val<=9):
                                print("输入错误，请输入整数，范围在0-9之间。")
                                continue
                            new_node=ListNode(val)
                            if head is None:
                                head=new_node
                                tail=new_node
                            else:
                                tail.next=new_node
                                tail=new_node
                        except ValueError:
                            print("输入错误，请输入整数，范围在-100到100之间。")
                            retry_count+=1
                            if retry_count>=max_retry:
                                print("输入错误次数过多，程序退出。")
                                raise SystemExit(1)
                     return head
if __name__=="__main__":
     solution=Solution()
     print("请输入第一个链表：")
     l1=solution.input_linked_list()

     print("请输入第二个链表：")
     l2=solution.input_linked_list()

     result=solution.addTwoNumbers(l1,l2,0)

     print("结果：")
     while result:
        print(result.val,end="->")
        result=result.next
     print("None")