class Solution {
    public int maxArea(int[] heights) {
        int max = -1;
        int currentArea = -1;
        for (int i = 0; i < heights.length - 1; i++) {
            for (int j = i + 1; j < heights.length; j++) {
                currentArea = Math.min(heights[i], heights[j]) * (j - i);
                max = Math.max(max, currentArea);
            }
        }

        return max;
    }
}
