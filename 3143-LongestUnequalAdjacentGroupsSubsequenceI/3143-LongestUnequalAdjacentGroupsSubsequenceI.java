// Last updated: 9/16/2025, 2:16:27 PM
class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> result = new ArrayList<>();
        int last = -1;
        for (int i = 0; i < words.length; i++) {
            if (groups[i] != last) {
                result.add(words[i]);
                last = groups[i];
            }
        }
        return result;
    }
}