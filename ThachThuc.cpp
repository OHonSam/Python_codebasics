#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int totalP(int n, vector<int> p){
    if(n == 1 || n == 2 || n == 3)
        return p[n];
    if(!p[n-1] && !p[n-2])
        return p[n] = totalP(n-1,p) + totalP(n-2,p);
    else 
       return p[n-1] +  p[n-2];
}

int main() {
    vector<int> p(1000001, 0);
    p[1] = 1;
    p[2] = 2;
    p[3] = 3;
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i){
        int n;
        cin >> n;
        cout << totalP(n,p) % 10 << endl;
        
        
    }
    return 0;
}