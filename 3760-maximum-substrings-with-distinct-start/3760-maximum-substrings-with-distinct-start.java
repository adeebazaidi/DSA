class Solution {
    public int maxDistinct(String s) {
        String a = "";

        for (int i = 0; i < s.length(); i++) {
            if (a.indexOf(s.charAt(i)) == -1) {
                a += s.charAt(i);
            }
        }

        return a.length();
    }
}