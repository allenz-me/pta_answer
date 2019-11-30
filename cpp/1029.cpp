#include <bits/stdc++.h>
using namespace std;

int main() {
    int n1, n2, tt;
    vector<int> nums1, nums2;
    cin >> n1;
    for (int i = 0; i < n1; i++) {
        cin >> tt;
        nums1.push_back(tt);
    }
    cin >> n2;
    for (int i = 0; i < n2; i++) {
        cin >> tt;
        nums2.push_back(tt);
    }
    vector<int> nums;
    int i = 0, j = 0;
    while (i < n1 && j < n2) {
        if (nums1[i] < nums2[j]) {
            nums.push_back(nums1[i++]);
        } else {
            nums.push_back(nums2[j++]);
        }
    }
    while (i < n1) {
        nums.push_back(nums1[i++]);
    }
    while (j < n2) {
        nums.push_back(nums2[j++]);
    }
    int med = (n1 + n2 - 1) / 2;
    cout << nums[med];
}