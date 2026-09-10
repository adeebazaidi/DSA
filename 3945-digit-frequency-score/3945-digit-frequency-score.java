class Solution {
    public int digitFrequencyScore(int n) {
        int a[]=new int[10];
        int m =n;
        while(m!=0){
            int d=m%10;
            a[d]++;
            m=m/10;
        }
        int ans = 0;

        for (int i = 0; i < 10; i++) {
            if (a[i] > 0) {
                ans += i * a[i];
            }
        }
        return ans;
    }
}