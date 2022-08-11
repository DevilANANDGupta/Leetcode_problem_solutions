class Solution {
public:
    int longestPalindrome(string s) {
        map<char,int>mp;
        for(auto i : s){
            if(mp.find(i) != mp.end())
                mp[i]++;
            else mp[i] = 1;
        }
        int ans = 0;
        for(auto i : mp){
            int k = i.second;
            ans += k - (k % 2);
        }
        if(ans == s.size()) return ans;
        else return (ans+1);
        
    }
};
