// Last updated: 9/16/2025, 2:17:25 PM
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long c=0;
        int start=-1,mini=-1,maxi=-1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<minK || nums[i]>maxK) start=i;
            if(nums[i]==minK) mini=i;
            if(nums[i]==maxK) maxi=i;
            int valid=Math.max(0,Math.min(mini,maxi)-start);
            c+=valid;

        }
        return c;
    }
}