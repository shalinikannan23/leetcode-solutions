// Last updated: 9/16/2025, 2:18:11 PM
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int pos = 0, neg = 1;
        int[] result = new int[n];

        for (int num : nums) {
            if (num > 0) {
                result[pos] = num;
                pos += 2;
            } else {
                result[neg] = num;
                neg += 2;
            }
        }
        return result;
    }
}
