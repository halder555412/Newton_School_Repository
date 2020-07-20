#You are given an array A of size N, and you are also given a sum. 
#You need to find if two numbers in A exists such that their sum is equal to the given sum. 
#If yes, print 1, else print 0.

import java.util.Scanner;
import java.util.Map.Entry;
class Main
{
    public static void main(String ars[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum=sc.nextInt();
        int arr[]=new int[n];
        boolean found=false;
        Set<Integer>set=new HashSet<>();
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
            if(set.contains(arr[i]))
            {
                found=true;
                sc.nextLine();
                System.out.println(1);
                break;
            }
            else
            {
                set.add(sum-arr[i]);
            }

        }
        if(!found){
            System.out.println(0);
        }
    }
}
    
'''
Sample Input
10 14
1 2 3 4 5 6 7 8 9 10

Sample Output
1

Explanation 
10 + 4 = 14,  so pair exists

Sample Input
5 9
1 2 3 4 5 

Sample Output 
1
'''
