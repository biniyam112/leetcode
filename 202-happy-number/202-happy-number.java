class Solution {
    public boolean isHappy(int n) {
        Set<Integer> visited = new HashSet<Integer>();
        while(true){
            Integer squared = 0;
            while(n!=0){
                int s = n%10;
                squared += s*s;
                n /= 10;
            }
            if (visited.contains(squared)){
                return false;
            }
            if(squared == 1){
                return true;
            }
            n = squared;
            visited.add(squared);
        }
        
    }
}