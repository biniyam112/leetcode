class Solution {
    int getOrder(char c) {
        int order = c;
        if ((97 <= order && order <= 122) || (48 <= order && order <= 57)) {
            return order;
        }
        
        else if (65 <= order && order <= 90) {
            return order + 32;
        }
        else {
            return -1;
        }
    }

    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length()-1;
        while (j > i) {
            int start = getOrder(s.charAt(i));
            int end = getOrder(s.charAt(j));
            if (start == -1) {
                i += 1;
            }
            if (end == -1) {
                j -= 1;
            }
            else if (start != -1 && end != -1) {
                if (start != end) {
                    return false;
                }
                i += 1;
                j -= 1;
            }

        }
        return true;
    }
}