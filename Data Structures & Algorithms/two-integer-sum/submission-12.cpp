class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> check;

        for(int i = 0; i<nums.size();i++){
            int difference = target-nums[i];
            if(check.count(difference))
                return {check[difference],i};
            
            check[nums[i]] = i;
        }
    }
};
