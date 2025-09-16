// Last updated: 9/16/2025, 2:17:05 PM
class Solution {
    public int maximumCount(int[] nums) {
        int negCount = 0, posCount = 0;
        
        for (int num : nums) {
            if (num < 0) negCount++;
            else if (num > 0) posCount++;
        }
        
        return Math.max(negCount, posCount);
    }
}
