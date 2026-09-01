import java.util.*;
class Solution {
    public int mirrorDistance(int n) {
        int a,abs,m=n,rev=0;
        while(m!=0){
            a=m%10;
            rev=rev*10+a;
            m=m/10;
        }
        return abs= Math.abs(n-rev);
    }
}