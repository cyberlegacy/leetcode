class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Solves the Candy Distribution problem using the Two-Pass Greedy Approach.
        
        Algorithm Choice: Two-Pass Greedy Approach
        
        Step-by-Step Logic:
        1. Initialize an array 'candies' where each child starts with 1 candy (satisfying the minimum requirement).
        
        2. First Pass (Left to Right):
           - For each child from index 1 to n-1:
           - If the current child has a higher rating than their left neighbor,
             give them one more candy than their left neighbor.
           - This ensures the "higher rating than left neighbor" constraint is satisfied.
        
        3. Second Pass (Right to Left):
           - For each child from index n-2 down to 0:
           - If the current child has a higher rating than their right neighbor,
             they need at least one more candy than their right neighbor.
           - Take the maximum of their current candies and (right neighbor's candies + 1).
           - This ensures the "higher rating than right neighbor" constraint is satisfied
             while preserving the left constraint from the first pass.
        
        4. Return the sum of all candies.
        
        Correctness:
        - The first pass ensures that any child with a higher rating than their left neighbor
          gets more candies than that neighbor.
        - The second pass ensures that any child with a higher rating than their right neighbor
          gets more candies than that neighbor.
        - By taking the maximum in the second pass, we preserve both constraints.
        - Each child starts with at least 1 candy, satisfying the minimum requirement.
        - The greedy approach of giving just one more candy than the neighbor (when needed)
          ensures we use the minimum number of candies.
        
        Complexity Analysis:
        - Time Complexity: O(n) where n is the number of children.
          We make exactly two passes through the array, each taking O(n) time.
        - Space Complexity: O(n) for the candies array that stores the candy count for each child.
        
        Args:
            ratings: List of integers representing each child's rating
            
        Returns:
            int: The minimum number of candies needed
        """
        if not ratings:
            return 0
        
        n = len(ratings)
        if n == 1:
            return 1
        
        # Initialize each child with 1 candy
        candies = [1] * n
        
        # First pass: left to right
        # Ensure children with higher ratings than left neighbor get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Second pass: right to left
        # Ensure children with higher ratings than right neighbor get more candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)


if __name__ == "__main__":
    print("Testing the Candy Distribution Solution")
    print("=" * 50)
    
    # Create an instance of Solution
    solution = Solution()
    
    # Define test cases
    test_cases = [
        # LeetCode examples
        {
            "input": [1, 0, 2],
            "expected": 5,
            "description": "Basic example from LeetCode"
        },
        {
            "input": [1, 2, 2],
            "expected": 4,
            "description": "Example with equal ratings"
        },
        # Edge cases
        {
            "input": [],
            "expected": 0,
            "description": "Empty list"
        },
        {
            "input": [1],
            "expected": 1,
            "description": "Single child"
        },
        # Simple progressions
        {
            "input": [1, 2, 3, 4, 5],
            "expected": 15,
            "description": "Strictly increasing"
        },
        {
            "input": [5, 4, 3, 2, 1],
            "expected": 15,
            "description": "Strictly decreasing"
        },
        # Valley then peak
        {
            "input": [1, 3, 4, 5, 2],
            "expected": 11,
            "description": "Valley then peak pattern"
        },
        # Complex sequence with plateaus and valleys
        {
            "input": [1, 3, 2, 2, 1],
            "expected": 7,
            "description": "Complex with plateaus and valleys"
        },
        # Additional test cases for thoroughness
        {
            "input": [2, 1],
            "expected": 3,
            "description": "Two children, decreasing"
        },
        {
            "input": [1, 2],
            "expected": 3,
            "description": "Two children, increasing"
        },
        {
            "input": [1, 1, 1],
            "expected": 3,
            "description": "All equal ratings"
        },
        {
            "input": [1, 2, 87, 87, 87, 2, 1],
            "expected": 13,
            "description": "Peak with plateau"
        },
        {
            "input": [1, 2, 3, 1, 0],
            "expected": 9,
            "description": "Mountain shape"
        }
    ]
    
    # Run tests
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        ratings = test["input"]
        expected = test["expected"]
        description = test["description"]
        
        actual = solution.candy(ratings)
        passed = actual == expected
        status = "✅ Pass" if passed else "❌ Fail"
        
        if not passed:
            all_passed = False
        
        print(f"\nTest {i}: {description}")
        print(f"Input: {ratings}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print(f"Status: {status}")
        
        # For failed tests, show candy distribution for debugging
        if not passed and ratings:
            n = len(ratings)
            candies = [1] * n
            # First pass
            for j in range(1, n):
                if ratings[j] > ratings[j - 1]:
                    candies[j] = candies[j - 1] + 1
            # Second pass
            for j in range(n - 2, -1, -1):
                if ratings[j] > ratings[j + 1]:
                    candies[j] = max(candies[j], candies[j + 1] + 1)
            print(f"Candy distribution: {candies}")
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed. Please review the implementation.") 