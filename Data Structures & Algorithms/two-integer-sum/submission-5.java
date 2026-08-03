class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> idxTracker = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int x = nums[i];
            int y = target - x;

            if(idxTracker.containsKey(y)){
                return new int[]{idxTracker.get(y), i};
            }

            idxTracker.put(x, i);
        }

        return new int[] {-1,-1};
    }
}

