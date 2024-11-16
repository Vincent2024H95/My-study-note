import java.util.ArrayList;
import java.util.Scanner;

public class TwoSum {
    static class solution{
        public int[] twosum(int[] nums,int target){
             int n=nums.length;
                 for(int i=0;i<n;i++){
                     for(int j=i+1;j<n;j++){
                         if(nums[i]+nums[j]==target){
                             return new int[]{i,j};
                         }
                     }
                 }
                return new int[0];
        } 
     }
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arrayList = new ArrayList<>();
        System.out.println("请输入数组元素（以空格分隔，按回车键结束输入）：");
        String input = sc.nextLine();
        String[] elements = input.split(" ");
        int maxInputSize = 10000; // 设定一个最大输入元素个数，可根据实际情况调整
        int count = 0;
        try {
            for (String element : elements) {
                if (count >= maxInputSize) {
                    System.out.println("输入的数组元素个数已达到上限，请重新输入合理数量的元素。");
                    return;
                }
                arrayList.add(Integer.parseInt(element));
                count++;
            }
        } catch (NumberFormatException e) {
            System.out.println("输入的数组元素格式有误，请重新输入整数元素，以空格分隔，按回车键结束输入。");
            sc.nextLine();
            return;
        }
    
        int[] array = new int[arrayList.size()];
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
    
        System.out.println("输入目标值:");
        int target = sc.nextInt();
    
        solution s = new solution();
        int[] result = s.twosum(array, target);
        if (result.length == 2) {
            System.out.println("[" + result[0] + "," + result[1] + "]");
        } else {
            System.out.println("No two sum solution");
        }
    
        sc.close();
    }
    /*public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        //数组不确定大小，动态输入，使用arraylist类
        ArrayList<Integer> arrayList=new ArrayList<>();
        System.out.println("输入数组元素:");
        String input=sc.nextLine();
        String[] elements=input.split(" ");
        try{
            for(String element:elements){
                arrayList.add(Integer.parseInt(element));
            }
        }
        catch(NumberFormatException e)
        {
            System.out.println("error");
            sc.nextLine();
        }
        while(sc.hasNextLine()){
            arrayList.add(sc.nextInt());
        }
        //将arraylist转换为数组
        int[] array = new int[arrayList.size()];
        for(int i=0;i<arrayList.size();i++){
            array[i]=arrayList.get(i);
        }
        System.out.println("输入目标值:");
        int target=sc.nextInt();
        solution s=new solution();
        int[] result=s.twosum(array,target);
        if(result.length==2){
            System.out.println("["+result[0]+","+result[1]+"]");
        }else{
            System.out.println("No two sum solution");
        }
        sc.close();
        System.out.println("test");
    }*/
}
