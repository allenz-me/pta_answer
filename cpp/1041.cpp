#include <bits/stdc++.h>
using namespace std;

int cnt[10500];
int tt;

int main() {
    int N;
    cin >> N;
    bool flag = true;
    memset(cnt, 0, sizeof(cnt));
    vector<int> ns;
    for (int i = 0; i < N; i++) {
        cin >> tt;
        ns.push_back(tt);
        cnt[tt]++;
    }
    for (auto i : ns) {
        if (cnt[i] == 1) {
            cout << i;
            flag = false;
            return 0;
        }
    }
    if (flag) {
        cout << "None";
    }
    return 0;
}