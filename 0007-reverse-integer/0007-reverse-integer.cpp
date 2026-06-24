class Solution {
public:
    int reverse(int n) {
        long long rev = 0;
        
        while (n != 0) {
            int digit = n % 10;   
            n = n / 10;             
            rev = rev * 10 + digit; 
        }
        
        if (rev > INT_MAX || rev < INT_MIN){
            return 0; //out of range
        }
        
        return (int)rev;
    }

};