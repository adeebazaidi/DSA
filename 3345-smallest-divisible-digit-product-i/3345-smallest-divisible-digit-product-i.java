class Solution {
    public int smallestNumber(int n, int t) {
        int x=0,k;
        for(int i=n;i<=100;i++){
            k=i;
            int p=1;
            while(k!=0){
                int a=k%10;
                p=p*a;
                k/=10;
            }
            if(p%t==0){
                x=i;
                break;
            }
        }
        return x;
    }
}