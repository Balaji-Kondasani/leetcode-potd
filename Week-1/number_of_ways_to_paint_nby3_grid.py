class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial state for n=1
        # aba: count of rows with pattern ABA (2 colors)
        # abc: count of rows with pattern ABC (3 colors)
        aba, abc = 6, 6
        
        for _ in range(n - 1):
            # Calculate next counts based on transitions
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            
            # Update states
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD