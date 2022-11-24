import java.util.ArrayList;

class Solution {
    public int[] countBits(int n) {
        ArrayList<Integer> ones = new ArrayList<Integer>();
        ones.add(0);
        int next_power = 1;
        for(int i = 1;i<= n;i++){
            if(i == next_power){
                ones.add(1);
                next_power *= 2;
            }
            else{
                int cur_power = next_power/2;
                ones.add(ones.get(cur_power) + ones.get(i - cur_power));
            }
        }
        int[] arr = ones.stream().mapToInt(i -> i).toArray();
        return arr;
    }
}