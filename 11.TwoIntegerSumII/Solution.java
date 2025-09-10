class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int firstPointer = 0;
        int secondPointer = numbers.length - 1;
        while(firstPointer < numbers.length) {
            int firstNum = numbers[firstPointer];
            int secondNum = numbers[secondPointer];
            if (firstNum + secondNum == target) {
                return new int[] {firstPointer + 1, secondPointer + 1};
            } else if (firstNum + secondNum < target) {
                firstPointer++;
            } else {
                secondPointer--;
            }
        }
        return new int [0];
    }
}

