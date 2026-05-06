class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
    
        for (String str : strs) {
            String hash = getHash(str);
            if (groups.containsKey(hash)) {
                groups.get(hash).add(str);
            } else {
                groups.put(hash, new ArrayList<String>(){{add(str);}});
            }
        }

        return new ArrayList<>(groups.values());
    }

    private String getHash(String s) {
        int[] count = new int[26];
        for (char c: s.toCharArray()) {
            count[c-'a']++;
        }
        return Arrays.toString(count);
    }
}
