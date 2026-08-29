import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        
        if (digits.length() == 0) {
            return result;
        }

        String[] map = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        solve(digits, 0, "", map, result);

        return result;
    }

    public void solve(String digits, int index, String current,
                      String[] map, List<String> result) {

        if (index == digits.length()) {
            result.add(current);
            return;
        }

        String letters = map[digits.charAt(index) - '0'];

        for (char ch : letters.toCharArray()) {
            solve(digits, index + 1, current + ch, map, result);
        }
    }
}