class Solution {
    public int lengthOfLongestSubstring(String s) {
        String st = "";
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int p = st.indexOf(ch);

            if (p != -1) {
                st = st.substring(p + 1);
            }

            st += ch;

            if (st.length() > max) {
                max = st.length();
            }
        }

        return max;
    }
}