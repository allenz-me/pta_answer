#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> M >> N;
    unordered_map<int, int> cnt;
    int tt;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> tt;
            cnt[tt]++;
        }
    }
    auto it = cnt.begin();
    int res = it->first, v = it->second;
    it++;
    while (it != cnt.end()) {
        if (it->second > v) {
            v = it->second;
            res = it->first;
        }
        it++;
    }
    cout << res;
    return 0;
}