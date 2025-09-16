// Last updated: 9/16/2025, 2:17:43 PM
class Solution {
    public char repeatedCharacter(String s) {
        HashSet<Character> seen=new HashSet<>();
        for(char c:s.toCharArray()){
            if(seen.contains(c)){
                return c;
            }
            seen.add(c);
        }
        return ' ';
    }
}