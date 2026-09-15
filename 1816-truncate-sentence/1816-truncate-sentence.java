class Solution {
    public String truncateSentence(String s, int k) {
        int i, c = 0;

        for (i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                c++;

                if (c == k) {
                    break;
                }
            }
        }

        return s.substring(0, i);
    }
}