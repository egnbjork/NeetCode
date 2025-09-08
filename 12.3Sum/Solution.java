class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
       Set<List<Integer>> solution = new HashSet<>();
       Arrays.sort(nums);
       for (int i = 0; i < nums.length; i++) {
        for (int p = 0; p < nums.length; p++) {
            for (int k = 0; k < nums.length; k++) {
                if (i != p && p != k && i != k &&
                (nums[i] + nums[p] + nums[k]) == 0) {
                    List combinations = Arrays.asList(nums[i], nums[p], nums[k]);
                    Collections.sort(combinations);
                    solution.add((combinations));
                }
            }
        }
       } 
       return new ArrayList(solution);
    }
}

