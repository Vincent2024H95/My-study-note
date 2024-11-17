#include<iostream>
#include<vector>
using namespace std;
//Definition for singly-linked list.
/*
@brief 两数相加
@para l1,l2 两个链表
@return 相加后的链表
*/
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head=nullptr,*tail=nullptr;
        // 初始化结果链表的头节点和尾节点
        int carry=0;
        // 初始化进位值
        while(l1||l2){// 当 l1 或 l2 不为空时，执行循环
            int n1=l1?l1->val:0;
            int n2=l2?l2->val:0;
            int sum=n1+n2+carry;
            // 如果结果链表为空，则创建新节点作为头节点和尾节点
            if(!head){
                head=tail=new ListNode(sum%10);
            }else{
                //不为空，在尾节点后添加新节点
                tail->next=new ListNode(sum%10);
                tail=tail->next;
            }
            carry=sum/10;// 计算进位值
            if(l1){
                l1=l1->next;// 移动 l1 指针
            }
            if(l2){
                l2=l2->next;// 移动 l2 指针
            }
        }
        // 如果进位值大于 0，则在尾节点后添加新节点
        if(carry>0){
            tail->next=new ListNode(carry);
        }
        return head;// 返回结果链表的头节点
    }
};

//用于构建链表的函数，根据用户输入的数字位数和各个数位的值来构建链表
ListNode* createList(){
    int n;//要输入链表的位数
    cout<<"请输入要输入链表的位数：\n";
    cin>>n;

    ListNode* head=nullptr;//初始化链表的头节点为空
    ListNode* tail=nullptr;//初始化链表的尾节点为空

    for(int i=0;i<n;i++){
        int digit;
        cout<<"请输入第"<<i+1<<"位数的值：";
        cin>>digit;
        ListNode* newNode=new ListNode(digit);//创建新节点，节点值为digit

        if(!head){
            head=tail=newNode;//如果链表为空，将新节点赋值给头节点和尾节点
        }else{
            tail->next=newNode;//如果链表不为空，将新节点添加到尾节点的后面
            tail=newNode;//更新尾节点为新节点
        }
    }
    return head;//返回链表的头节点
}

int main(){
    cout<<"请输入第一个链表："<<endl;
    ListNode* l1=createList();//调用createList函数创建第一个链表

    cout<<"请输入第二个链表:"<<endl;
    ListNode* l2=createList();//调用createList函数创建第二个链表

    Solution solution;
    ListNode* result=solution.addTwoNumbers(l1,l2);//调用addTwoNumbers函数计算两个链表的和

    cout<<"结果链表为：\n"<<endl;
    while(result){
        cout<<result->val<<"";
        if(result->next){
            cout<<",";
        }
        result=result->next;
    }
    cout<<endl;
    return 0;
}