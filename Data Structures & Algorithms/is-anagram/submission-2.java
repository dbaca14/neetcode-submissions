class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){return false;}
        int j =0;
        HashMap<Character, Integer> charCountS = new HashMap();
        HashMap<Character, Integer> charCountT = new HashMap();

        for(int i = 0; i < s.length(); i++){
            if(charCountS.containsKey(s.charAt(i))){
                int currCount = charCountS.get(s.charAt(i));
                charCountS.put(s.charAt(i), currCount+=1);
            }else{
                charCountS.put(s.charAt(i), 0);
            }
            if(charCountT.containsKey(t.charAt(j))){
                int currCount = charCountT.get(t.charAt(j));
                charCountT.put(t.charAt(j), currCount+=1);
            }else{
                charCountT.put(t.charAt(j), 0);
            }
            j++;
        }

        return charCountS.equals(charCountT);
    }
}
