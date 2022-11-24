class Solution {
    public List<String> summaryRanges(int[] nums) {
        ArrayList<String> ans = new ArrayList<String>();
        ArrayList<Integer> stack = new ArrayList<Integer>();
        for(int i=0;i < nums.length;i++){
            if(stack.size() == 0 || stack.get(stack.size()-1)+1 == nums[i]){
                stack.add(nums[i]);
            }
            else{
                if(stack.size() > 1){
                    ans.add(Integer.toString(stack.get(0))+"->"+Integer.toString(stack.get(stack.size()-1)));
                }
                else{
                    ans.add(Integer.toString(stack.get(0)));
                }
                stack = new ArrayList();
                stack.add(nums[i]);
            }
        }
        if(stack.size() > 1){
                ans.add(Integer.toString(stack.get(0))+"->"+Integer.toString(stack.get(stack.size()-1)));
        }
        else if(stack.size() == 1){
                ans.add(Integer.toString(stack.get(0)));
        }
        return ans;
    }
}