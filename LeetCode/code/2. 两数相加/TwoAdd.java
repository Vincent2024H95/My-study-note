package TwoAdd;

import java.util.InputMismatchException;
import java.util.Scanner;

//import java.lang.classfile.components.ClassPrinter.ListNode;
class Solution {
    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { 
            this.val = val; 
        }
        ListNode(int val, ListNode next) { 
            this.val = val; this.next = next; 
        }
    }
    public ListNode TwoAdd(ListNode l1, ListNode l2) {
        ListNode head = null, tail = null;
        int carry = 0;
        while(l1!= null || l2!= null){
            int n1 = l1!= null? l1.val : 0;
            int n2 = l2!= null? l2.val : 0;
            int sum = n1 + n2 + carry;
            if(head == null){
                head = tail = new ListNode(sum % 10);
            }else{
                tail.next = new ListNode(sum % 10);
                tail = tail.next;
            }
            carry = sum / 10;// 添加这行代码来更新进位值
            if(l1!= null){
                l1 = l1.next;
            }
            if(l2!= null){
                l2 = l2.next;
            }
            if(carry > 0){
                tail.next = new ListNode(carry);
            }
        }
       return head;
    }

    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        Solution solution=new Solution();

        // 输入链表1
        System.out.println("请输入链表1的元素（以空格分隔）：");
        ListNode l1 = createList(scanner);

        // 输入链表2
        System.out.println("请输入链表2的元素（以空格分隔）：");
        ListNode l2 = createList(scanner);

        //输出
        ListNode result=solution.TwoAdd(l1,l2);
        printList(result);

        scanner.close();
    }

    //根据用户输入的数组创建链表
    private static ListNode createList(Scanner scanner) {
        ListNode head=null;
        ListNode tail=null;
        int retrycount=0;
        while(true){
        try{
            String input=scanner.nextLine();
            String[] values=input.split(" ");

            for(String value:values){
                int digit=Integer.parseInt(value);
                ListNode newNode=new ListNode(digit);

                if(head==null){
                    head=tail=newNode;
                }else{
                    tail.next=newNode;
                    tail=newNode;
                }
            }
            break;
        }
        catch(InputMismatchException | NullPointerException e){
            retrycount++;
            if(retrycount>=3){
                System.out.println("输入格式错误");
                System.exit(1);
            }
            System.out.println("输入格式错误");
            return createList(scanner);
        }
    }
    return head;
}

    private static void printList(ListNode node){
        while(node!=null){
            System.out.print(node.val);
            if(node.next!=null){
                System.out.print("->");
            }
            node=node.next;
        }
        System.out.println();
    }
}