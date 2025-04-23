class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()  # Sort children's greed factors
        s.sort()  # Sort cookie sizes
        
        count = 0
        i = 0  # Index for children
        j = 0  # Index for cookies
        
        # Try to assign cookies to children
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If current cookie can satisfy current child
                count += 1
                i += 1  # Move to next child
            j += 1  # Always move to next cookie
            
        return count
    
    def findContentChildrenReversed(self, g, s):
        """
        Alternative greedy approach starting with largest greed factor
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        
        # Sort in reverse order (largest to smallest)
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        count = 0
        j = 0  # Index for cookies
        
        # For each child (starting from greediest)
        for i in range(len(g)):
            # If we still have cookies and current cookie can satisfy current child
            if j < len(s) and s[j] >= g[i]:
                count += 1
                j += 1  # Use this cookie and move to next
        
        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases for both approaches
    test_cases = [
        ([1, 2, 3], [1, 1], 1),           # Example 1
        ([1, 2], [1, 2, 3], 2),           # Example 2
        ([1, 2, 3], [], 0),               # Empty cookies
        ([], [1, 2, 3], 0),               # Empty children
        ([10, 20, 30], [1, 2, 3], 0),     # No matches
        ([1, 2, 3], [1, 2, 3], 3),        # Exact matches
        ([1, 2], [1, 2, 3, 4, 5], 2),     # More cookies than children
        ([3, 2, 1], [3, 2, 1], 3)         # Reverse order input
    ]
    
    print("Original Approach (Smallest to Largest):")
    for i, (g, s, expected) in enumerate(test_cases):
        # Create copies to avoid modifying the original arrays
        g_copy = g.copy() if hasattr(g, 'copy') else list(g)
        s_copy = s.copy() if hasattr(s, 'copy') else list(s)
        result = sol.findContentChildren(g_copy, s_copy)
        print(f"Test {i+1}: {result} (Expected: {expected})")
    
    print("\nReversed Approach (Largest to Smallest):")
    for i, (g, s, expected) in enumerate(test_cases):
        # Create copies to avoid modifying the original arrays
        g_copy = g.copy() if hasattr(g, 'copy') else list(g)
        s_copy = s.copy() if hasattr(s, 'copy') else list(s)
        result = sol.findContentChildrenReversed(g_copy, s_copy)
        print(f"Test {i+1}: {result} (Expected: {expected})")

"""
Why this problem can be solved with a greedy approach:

1. Optimal Substructure: The problem exhibits optimal substructure because the
   optimal solution can be constructed from optimal solutions to its subproblems.
   Each decision to assign a cookie to a child is independent of previous assignments.

2. Greedy Choice Property: Making the locally optimal choice at each step leads to
   a globally optimal solution. 

   In the original approach (smallest to largest):
   - We prioritize satisfying children with smaller greed factors first
   - For each child, we use the smallest possible cookie that can satisfy them
   - This ensures we don't "waste" larger cookies on children with small greed factors

   In the reversed approach (largest to smallest):
   - We prioritize satisfying children with larger greed factors first
   - For each child, we use the largest cookie available that can satisfy them
   - This works because if a child with large greed can't be satisfied, we try the
     next child with a smaller greed factor

Both approaches work because the problem has only one constraint: s[j] >= g[i].
There's no benefit to giving a child a cookie larger than needed, nor is there any
benefit to leaving children unsatisfied if we have cookies available. The goal is
simply to maximize the number of content children.
"""

