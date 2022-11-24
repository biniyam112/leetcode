import java.util.Arrays;

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = 0;
        int runningSum = n*((n+1)/2);
        if(n % 2 == 0){
            runningSum += n/2;
        }
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return runningSum - sum;
    }
}
