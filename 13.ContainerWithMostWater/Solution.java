class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        for (int i = 0; i < heights.length; i++) {
            for (int p = i; p < heights.length; p++) {
                int waterAmount = (p - i) * Math.min(heights[i], heights[p]);

                if (waterAmount > max) {
                    max = waterAmount;
                }
            }
        } 
        return max;
    }
}

