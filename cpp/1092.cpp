#include <bits/stdc++.h>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    unordered_map<char, int> m1, m2;
    for (char c : s1) {
        m1[c]++;
    }
    for (char c : s2) {
        m2[c]++;
    }
    bool flag = true;
    for (auto it = m2.begin(); it != m2.end(); it++) {
        if (m2[it->first] > m1[it->first]) {
            flag = false;
            break;
        }
    }
    int res = 0;
    if (flag) {
        res = s1.size() - s2.size();
        cout << "Yes " << res;
        return 0;
    }
    // else
    for (auto it = m2.begin(); it != m2.end(); it++) {
        if (m1[it->first] < m2[it->first]) {
            res += m2[it->first] - m1[it->first];
        }
    }
    cout << "No " << res;
    return 0;
}