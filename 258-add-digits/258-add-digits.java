class Solution {
    public int addDigits(int num) {
        while(num > 9){
            int val = 0;
            while(num!=0){
                val += num%10;
                num /= 10;
            }
            num = val;
        }
        return num;
    }
}