class Solution {
    public boolean checkDivisibility(int n) {
        int s=0,p=1,a,m=n;
        while (n>0){
            a=n%10;
            s=s+a;
            p=p*a;
            n=n/10;
        }
        if(m%(s+p)==0)
            return true;
        else
            return false;
    }
}