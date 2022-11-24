import java.util.Arrays;

class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int runningSum = nums.length;
            
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            runningSum += i;
        }
        return runningSum - sum;
    }
}
