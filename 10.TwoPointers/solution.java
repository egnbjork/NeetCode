class Solution {
    public boolean isPalindrome(String s) {
        String normalizedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversedNormalizedString = new StringBuilder(normalizedString).reverse().toString();
        return normalizedString.equals(reversedNormalizedString);
    }
}
