import java.util.ArrayList;
import java.util.List;

class Solution {
    public void dfs(int index,int[] nums){
        Solution solution = new Solution();
        if (nums[index] != -1){
            int val = nums[index]-1;
            nums[index] = -1;
            solution.dfs(val,nums);
        }
    }
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int i = 0;i < nums.length;i++){
            if(nums[i] != -1){
                dfs(nums[i]-1,nums);
            }
        }
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for (int i = 0;i < nums.length;i++){
            if(nums[i] != -1){
                ans.add(i+1);
            }
        }
        return ans;
    }
}