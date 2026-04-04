class Solution {
    
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            encoded.append(s.length()).append("/").append(s);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> words = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int slashIndex = str.indexOf('/', i);
            if (slashIndex == -1) {
                break; // No more encoded parts
            }
            int len = Integer.parseInt(str.substring(i, slashIndex));
            String word = str.substring(slashIndex + 1, slashIndex + 1 + len);
            words.add(word);
            i = slashIndex + 1 + len;
        }
        return words;
    }
}