class Solution {
    public int counter(int n){
        int counter = 0;
        while(n>0){
            if(n%2 == 1){
                n -= 1;
                counter += 1;
            }
            else {
                n /= 2;
            }
        }
        return counter;
    }
    public int[] countBits(int n) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        Solution solution = new Solution();
        for(int i=0;i <= n;i++){
            ans.add(solution.counter(i));
        }
        int[] arr = ans.stream().mapToInt(i -> i).toArray();
        return arr;
    }
}