class Solution {
    public boolean isPalindrome(String s) {
        int firstPointer = 0;
        int secondPointer = s.length() - 1;
        while(firstPointer <= secondPointer) {
            if(!isAlphaNumerical(s, firstPointer)) {
                firstPointer += 1;
                continue;
            } 
            if(!isAlphaNumerical(s, secondPointer)) {
                secondPointer -= 1;
                continue;
            }

            if (Character.toLowerCase(s.charAt(firstPointer)) != Character.toLowerCase(s.charAt(secondPointer))) {
                return false;
            }
            firstPointer += 1;
            secondPointer -= 1;
        }
        return true;
    }

    private boolean isAlphaNumerical(String s, int pos) {
        return ((s.charAt(pos) >= 'A' && s.charAt(pos) <= 'Z') ||
            s.charAt(pos) >= 'a' && s.charAt(pos) <= 'z' ||
            s.charAt(pos) >= '0' && s.charAt(pos) <= '9');
    }
}

