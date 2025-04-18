#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define VS2019 1

string s;
char f[256];
vector<int>zhouqi(256);
int n;
int cnt = 0;

void printZhouqi() {
    for (char i = 0; i < 127; i++) {
        cout << "ch: " << i << ", zhouqi: " << zhouqi[i] << endl;
    }
}

void initF() {
    cin >> n;
#ifdef VS2019
    getchar();
#endif 
    for (int i = 0; i < 256; i++) {
        f[i] = i;
        zhouqi[i] = 1;
    }
    for (int i = 0; i < n; i++) {
        string tmp;
        getline(cin,tmp);
        f[tmp[1]] = tmp[2];
        if (tmp[1] != tmp[2])
            zhouqi[tmp[1]] = -1;
    }

    for (int i = 0; i < 256; i++) {
        if (zhouqi[i] != -1)
            continue;
        zhouqi[i] = 0;
        char newChar = i;
        do {
            newChar = f[newChar];
            zhouqi[i]++;
        } while (i != newChar);
    }

}

void preprocessString(string& s) {
    getline(cin, s);

}

string getResult(int k) {
    string ret;
    for (const auto& ch : s) {
        char newChar = ch;
        int k1 = k;
        if (zhouqi[ch] != -1)
            k1 %= zhouqi[ch];

        for (int i = 0; i < k1; i++) {
            if (newChar == f[newChar])
                zhouqi[newChar] = i + 1;
            else
                newChar = f[newChar];
        }
        ret.push_back(newChar);
    }
    return ret;
}

int main() {
    preprocessString(s);
    initF();

    int t;
    cin >> t;

    while (t--) {
        int k;
        cin >> k;
        cout << getResult(k) << endl;

    }

}

