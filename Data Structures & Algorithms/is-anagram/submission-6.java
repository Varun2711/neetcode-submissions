class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> frequencies = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (frequencies.containsKey(c)) {
                frequencies.put(c, frequencies.get(c) + 1);
            } else {
                frequencies.put(c, 1);
            }
        }

        for (char c: t.toCharArray()) {
            if (frequencies.containsKey(c)) {
                if (frequencies.get(c) == 1) {
                    frequencies.remove(c);
                } else {
                    frequencies.put(c, frequencies.get(c)-1);
                }
            } else {
                return false;
            }
        }
        return frequencies.size() == 0;
    }
}
