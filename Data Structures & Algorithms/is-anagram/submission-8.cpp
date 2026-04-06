class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> sCount;
        unordered_map<char,int> tCount;

        int sLength = s.length();
        int tLength = t.length();

        if(sLength != tLength)
            return false;

        for(int i = 0; i<sLength;i++){
            sCount[s[i]]++;
            tCount[t[i]]++;
        }

        if (sCount == tCount)
            return true;
        return false;
    }
};
