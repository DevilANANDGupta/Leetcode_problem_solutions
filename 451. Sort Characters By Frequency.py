class Solution:
    def frequencySort(self, s: str) -> str:
        # count the frequency of each charater in s
        freq = Counter(s)
        # create an array with frequency of each element, and the element itself 
        arr = [(freq[c],c) for c in freq.keys()]
        # sort this array by frequency in decreasing order
        arr.sort(reverse=True)
        # return the element * frequency as an array
        return ''.join([x[1]*x[0] for x in arr])
