// Last updated: 9/16/2025, 2:16:14 PM
class Solution {
    public boolean hasMatch(String s, String p) {
       int ind=p.indexOf("*");
       int s1=s.indexOf(p.substring(0,ind));
       int s2=s.indexOf(p.substring(ind+1),s1+ind);
       if(s1!=-1 && s2!=-1){
        return true;
       }
       return false;
    }
}