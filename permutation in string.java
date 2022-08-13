class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n=s1.length();
        int m=s2.length();
      // If s1 length > s2 length  
        if(n>m)return false;
      //Create two HashMap for s1 and s2
        HashMap<Character,Integer>s1FrequencyMap=new HashMap<>();
        HashMap<Character,Integer>s2FrequencyMap=new HashMap<>();
      // Fill s1frequencyMap
        for(char ch:s1.toCharArray()){
            s1FrequencyMap.put(ch,s1FrequencyMap.getOrDefault(ch,0)+1);
        }
      // create a window for the size s1
        int i=0;
        int j=-1;
        for(;i<n-1;i++){
            char ch=s2.charAt(i);
            s2FrequencyMap.put(ch,s2FrequencyMap.getOrDefault(ch,0)+1);
        }
       //Acquire and Relase Strategy or Sliding Window 
        i--;
        while(i<m-1){
            i++;
          char ch=s2.charAt(i);
             s2FrequencyMap.put(ch,s2FrequencyMap.getOrDefault(ch,0)+1);
            if(isPermutation(s1FrequencyMap,s2FrequencyMap)){
                return true;
            }
            j++;
             ch=s2.charAt(j);
            s2FrequencyMap.put(ch,s2FrequencyMap.get(ch)-1);
            if(s2FrequencyMap.get(ch)==0)s2FrequencyMap.remove(ch);
            
        }
        return false;
        
    }
    public boolean isPermutation(HashMap<Character,Integer>s1FrequencyMap,HashMap<Character,Integer>s2FrequencyMap){
        for(int i=0;i<26;i++){
            char ch=(char)(i+'a');
            int f1=s1FrequencyMap.getOrDefault(ch,0);
            int f2=s2FrequencyMap.getOrDefault(ch,0);
            if(f1!=f2)return false;
        }
        return true;
    }
}
