'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.'''

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Calculate the longer repeating character
        string when replacing with one letter
        Args:
            s (str): String to evaluate
            k (int): Number of characters to replace
        Returns:
            int: Length of longest repeating sequence
        """
        behind, ahead = 0, 0
        char_count = defaultdict(int)
        char_count[s[ahead]] += 1
        max_length = 0

        while ahead < len(s):
            length = ahead - behind + 1
            max_freq = max(char_count.values())
            if length - max_freq <= k:
                max_length = max(length, max_length)
                ahead += 1
                if ahead == len(s):
                    break
                char_count[s[ahead]] += 1
            else:
                char_count[s[behind]] -= 1
                behind += 1

        return max_length
      
      
      
      
      
      
      
      
      
      
      
#       DESCRPTION
'''One of my first thoughts on this is to create a hashmap of each character to the positions it occupies. Then somehow analyze the list of positions to find the
ones that have the minimum distance. Perhaps subtracting the character indexes could reveal which characters are the closest together.
Step 1
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Calculate the longer repeating character
        string when replacing with one letter
        Args:
            s (str): String to evaluate
            k (int): Number of characters to replace
        Returns:
            int: Length of longest repeating sequence
        """
        positions = defaultdict(list)
        max_length = 0

        for index, char in enumerate(s):
            positions[char].append(index)

        for indexes in positions.values():
            index_length = len(indexes)
            diffs = [
                indexes[j] - indexes[i] - 1
                for i, j in zip(range(index_length - 1), range(1, index_length))
            ]
            diffs.insert(0, indexes[0])
            diffs.append(len(s) - 1 - indexes[-1])

        return 0
        
        
        This function constructs the spacing between characters in a string. For example, if s="aabbcba" then the spacing for “a” is [0,0,4,0]. It includes the beginning and end of the string. This sets us to to determine which character can create the longest repeating sequence through substitution.

The next step is to create a function that will take these “diff” arrays and calculate the longest possible repeating substring from them.

Step 2?

 def calculate_length(self, diffs: List[int], k: int) -> int:
        """Calculate maximum sequence length based
        on the differences between character positions
        Args:
            diffs (List[int]): List of position differences
            k (int): Number of characters to replace
        Returns:
            int: Maximum length of replacement
        """
        behind, ahead = 0, 0
        current_k = diffs[0]
        max_length = 0

        while ahead < len(diffs):
            if current_k <= k:
                ahead += 1
                if ahead == len(diffs):
                    break
                current_k += diffs[ahead]
            else:
                behind += 1
                current_k -= diffs[behind]
            length = ahead - behind + current_k
            if length > max_length and current_k <= k:
                max_length = length

        return max_length
        
     This is meant to be the function that calculates the maximum length substring for a “diff” array described above. It essentially looks at the array and tries to find the longest subarray where the sum is <= k. It uses the two pointer method to make the ahead pointer move ahead if the sum current_k <= k and the behind pointer move head if current_k > k. This is meant to keep the current sum hovering around k.

The problem with this approach is that mixing the diff values with characters makes the substring length hard to calculate. For example, for the string “babbab” the diff array for “a” is [1,2,1]. For k=2 it is clear that the maximum substring length for “a” is 4. This is created by replacing the two “b”s in the middle. However, coming up with that sum based on the ahead and behind pointer both pointing at 2 is challenging.

A simpler representation for the arrays is to just have 0sand 1s represent whether the character is present. So for the string “babbab” the array for “a” would look like [0,1,0,0,1,0]. 
The per-character arrays are the same length as the original string. I’m going to start again with this approach.

Initial Solution


from collections import defaultdict
from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Calculate the longer repeating character
        string when replacing with one letter
        Args:
            s (str): String to evaluate
            k (int): Number of characters to replace
        Returns:
            int: Length of longest repeating sequence
        """
        positions = defaultdict(list)
        max_length = 0

        for index, char in enumerate(s):
            if char not in positions.keys():
                positions[char] = [0] * len(s)
            positions[char][index] = 1

        for char_array in positions.values():
            char_length = self.calculate_length(char_array, k)
            if char_length > max_length:
                max_length = char_length

        return max_length

    def calculate_length(self, char_positions: List[int], k: int) -> int:
        """Calculate maximum sequence length based
        on the character positions
        Args:
            diffs (List[int]): List of character position
            k (int): Number of characters to replace
        Returns:
            int: Maximum length of replacement
        """
        behind, ahead = 0, 0
        match_count = 1 if char_positions[0] == 1 else 0
        nonmatch_count = 1 if char_positions[0] == 0 else 0
        max_length = 0

        while ahead < len(char_positions):
            if nonmatch_count <= k:
                ahead += 1
                if ahead == len(char_positions):
                    break
                if char_positions[ahead] == 1:
                    match_count += 1
                else:
                    nonmatch_count += 1
            else:
                if char_positions[behind] == 1:
                    match_count -= 1
                else:
                    nonmatch_count -= 1
                behind += 1
            length = match_count + nonmatch_count
            if length > max_length and nonmatch_count <= k:
                max_length = length

        return max_length
        
    and final solution are listed in first'''
