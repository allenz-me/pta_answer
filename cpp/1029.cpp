#include <bits/stdc++.h>
using namespace std;

int main() {
    int n1, n2, tt;
    vector<int> nums;
    cin >> n1;
    for (int i = 0; i < n1; i++) {
        cin >> tt;
        nums.push_back(tt);
    }
    cin >> n2;
    for (int i = 0; i < n2; i++) {
        cin >> tt;
        nums.push_back(tt);
    }
    sort(nums.begin(), nums.end());
    int med = (n1 + n2 - 1) / 2;
    cout << nums[med];
}