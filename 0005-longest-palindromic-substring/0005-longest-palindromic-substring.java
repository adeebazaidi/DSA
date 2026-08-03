class Solution {

    public String longestPalindrome(String s) {

        String st = "";

        for (int i = 0; i < s.length(); i++) {

            String ch = expand(s, i, i);
            if (ch.length() > st.length()) {
                st = ch;
            }

            ch = expand(s, i, i + 1);
            if (ch.length() > st.length()) {
                st = ch;
            }
        }

        return st;
    }

    public String expand(String s, int left, int right) {

        while (left >= 0 && right < s.length()
                && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }
}