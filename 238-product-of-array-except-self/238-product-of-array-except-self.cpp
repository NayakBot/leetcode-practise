class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1, count = 0;
        vector<int> out;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i] == 0)
                count++;
            else
                prod *= nums[i];
        }
        if(count > 1)
        {
            for(int i=0; i<nums.size(); i++)
                out.push_back(0);
        }
        else if(count == 1)
        {
            for(int i=0; i<nums.size(); i++)
                if(nums[i] == 0)
                    out.push_back(prod);
                else
                    out.push_back(0);
        }
        else
        {
            for(int i=0; i<nums.size(); i++)
                out.push_back(prod/nums[i]);
        }
        return out;
    }
};