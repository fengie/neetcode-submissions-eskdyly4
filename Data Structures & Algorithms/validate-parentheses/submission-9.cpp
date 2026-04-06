class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> brackets = {
            {'}','{'},
            {']','['},
            {')','('}
        };

        stack<char> temp;

        for(char c : s){
            if(brackets.count(c)){
                if(temp.empty() || temp.top()!= brackets[c])
                    return false;
                temp.pop();
            }
            else
                temp.push(c);
        }
        return temp.empty();
    }
};
