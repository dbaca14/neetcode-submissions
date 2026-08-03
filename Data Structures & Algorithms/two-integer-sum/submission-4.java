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


        // for(int i = 0; i < nums.length; i++){
        //     idxTracker.put(nums[i], i);
        //     int diff = 0;
        //     diff = target - nums[i];
        //     if(idxTracker.containsKey(diff)){

        //     }

        // }

        // for(int i = 0; i < nums.length; i++){
        //     idxTracker.put(nums[i], i);
        // }
        // int diff = 0;
        // for(int i = 0; i < nums.length; i++){
        //     diff = target - nums[i];
        //     if(idxTracker.containsKey(diff)){
        //         int hmapI = idxTracker.get(diff);
        //         if(i < hmapI){return new int[] {i, hmapI};}
        //         else{return new int[] {hmapI, i};}
        //     }
        // }
        // return new int[] {-1,-1};

    }
}

// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         Map<Integer, Integer> d = new HashMap<>();
//         for (int i = 0;; ++i) {
//             int x = nums[i];
//             int y = target - x;
//             if (d.containsKey(y)) {
//                 return new int[] {d.get(y), i};
//             }
//             d.put(x, i);
//         }
//     }
// }
