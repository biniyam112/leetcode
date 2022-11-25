class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int i = 0;
        for(int j = 0;j < nums.length; j++){
            if(nums[j] != nums[i]){
                if(j-1+1 > nums.length/2){
                    return nums[i];
                }
                i = j;
            }
        }
        return nums[i];
    }
}