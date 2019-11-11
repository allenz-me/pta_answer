#include <bits/stdc++.h>
using namespace std;

char c;
int main() {
    int s = 0;
    while (cin >> c) {
        s += c - '0';
    }
    unordered_map<char, string> hash{{'1', "one"},
    {'2', "two"}, {'3', "three"}, {'4', "four"}, {'5', "five"},
    {'6', "six"}, {'7', "seven"}, {'8', "eight"}, {'9', "nine"},
    {'0', "zero"}};
    string res = to_string(s);
    for (int i = 0; i < res.length(); i++) {
        if (i == 0) cout << hash[res[0]];
        else cout << " " << hash[res[i]];
    }
    return 0;

}