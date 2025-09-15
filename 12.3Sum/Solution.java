class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
       Set<List<Integer>> solution = new HashSet<>();
       Arrays.sort(nums);
       for (int i = 0; i < nums.length; i++) {
            if (i == 0 || (i != 0 && nums[i] != nums[i - 1])) {
                int pointerS = i + 1;
                int pointerM = nums.length - 1;
                while (pointerS < pointerM) {
                    if (nums[i] + nums[pointerS] + nums[pointerM] == 0) {
                        System.out.println("found solution");
                        solution.add(Arrays.asList(nums[i], nums[pointerS], nums[pointerM]));
                        pointerS++;
                        pointerM--;
                    } else if (nums[i] + nums[pointerS] + nums[pointerM] > 0) {
                        pointerM--;
                    } else {
                        pointerS++;
                    }
                }
                }
            }
       return new ArrayList(solution);
    }
}

