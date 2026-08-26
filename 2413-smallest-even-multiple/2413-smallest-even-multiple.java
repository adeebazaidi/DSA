class Solution {
    public int smallestEvenMultiple(int n) {
        int k=2;
        while(true){
            if(k%2==0 && k%n==0){
                break;
            }
            k+=2;
        }
        return k;
    }
}