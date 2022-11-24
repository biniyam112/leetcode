class Solution {
    public int arrangeCoins(int n) {
        int counter = 0;
        int cur = 1;
        while(n > 0){
            n -= cur;
            cur += 1;
            counter += 1;
        }
        if(n < 0){
            counter -= 1;
        }
        return counter;
    }
}