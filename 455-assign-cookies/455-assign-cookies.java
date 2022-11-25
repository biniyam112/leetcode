import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int ans = 0;
        int j = 0;
        for (int i = 0; i < g.length; i++) {
            if (j == s.length) {
                return ans;
                }
            if (g[i] <= s[j]) {
                ans += 1;
                j += 1;
            }
            else {
                while(j < s.length && s[j] < g[i]){
                    j += 1;
                }
             if (j == s.length) {
                return ans;
                }   
                j += 1;
                ans += 1;
            }
        }
        return ans;
    }
}
