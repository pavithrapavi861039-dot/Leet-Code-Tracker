// Last updated: 7/16/2026, 4:05:33 PM
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int n = arr.length;
        if (n == 1) return 1;
        int maxLen = 1;
        int curr = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] == arr[i - 1]) {
                curr = 1;
            } else if (i == 1 || 
                      (arr[i] > arr[i - 1] && arr[i - 1] < arr[i - 2]) ||
                      (arr[i] < arr[i - 1] && arr[i - 1] > arr[i - 2])) {
                curr++;
            } else {
                curr = 2; 
            }
            maxLen = Math.max(maxLen, curr);
        }
        return maxLen;
    }
}