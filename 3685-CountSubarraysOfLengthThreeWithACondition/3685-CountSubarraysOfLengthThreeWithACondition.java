// Last updated: 9/16/2025, 2:16:12 PM
class Solution {
    public int countSubarrays(int[] arr) {
        int sum = 0, c = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            sum = arr[i] + arr[i+2];
            if ((sum*2) == arr[i+1]) {
                c++;
            }
        }
        return c;
    }
}
