class Solution(object):
    def lastRemaining(self, n):
        if( n == 1 ):
            return 1;
        left = 2 ;
        right = n-(n%2);

        pos = 1;
        skip = 2;
        while( left < right ):
            if( pos == 1 ):
                if( ( (right-left)/skip )%2 == 0):
                    left += skip;
                right -= skip ;
                pos = 0;
            else:
                if( ( (right-left)/skip )%2 == 0):
                    right  -= skip;
                left += skip;
                pos = 1;
            skip *= 2;
        return right ;