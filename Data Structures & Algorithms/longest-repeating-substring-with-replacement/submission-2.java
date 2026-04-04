class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> counts = new HashMap<>();
        int res = 0;
        int l = 0; 
        int maxCount = 0;

        for (int r = 0; r < s.length(); r++) {
            char currentChar = s.charAt(r);
            counts.put(currentChar, counts.getOrDefault(currentChar, 0) + 1);
            maxCount = Math.max(maxCount, counts.get(currentChar));
            
            while ((r - l + 1) - maxCount > k) {
                char leftChar = s.charAt(l);
                counts.put(leftChar, counts.get(leftChar) - 1);
                l++;
            }
            
            res = Math.max(res, r - l + 1);
        }
        
        return res;
    }
}
