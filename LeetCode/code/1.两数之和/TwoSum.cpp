#include <iostream>
#include <vector>
using namespace std;
class solution{
    public:
    vector<int> twosum(vector<int>& nums,int target){
        int i,j;
        for(int i=0;i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]+nums[j]==target){
                    return vector<int>{i,j};
                }
            }
        }
        return vector<int>();
    };
};
int main(){
    cout<<"请输入数组元素个数：\n";
    int n;
    cin>>n;
    vector<int> arr(n);// 使用vector定义数组，根据输入个数动态分配内存
     cout<<"请输入元素：\n";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int target;
    cout<<"请输入目标值：\n";
    cin>>target;
    solution s;
    vector<int> result=s.twosum(arr,target);

    if(result.size()==2){
        cout<<"结果为：\n";
        cout<<"["<<result[0]<<","<<result[1]<<"]"<<endl;
    }
    else{
        cout<<"没有找到符合条件的结果"<<endl;
    }
}
