#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int n = 1, nr, a[202];

map<int, long long> m;

int countDiff(int diff){
    int cnt = 0;
    for(int i=1;i<=n;i++){
        if(a[i]-a[i-1]==diff){
            cnt++;
        }
    }
    return cnt;
}

long long ways(int i){
    if(m[i]!=0){
        return m[i];
    }
    if(i==n)
        return 1;
    long long sum = 0;
    if(a[i+1] && a[i+1]-a[i]<=3){
        sum+= ways(i+1);
    }
    if(a[i+2] && a[i+2]-a[i]<=3){
        sum+= ways(i+2);
    }
    if(a[i+3] && a[i+3]-a[i]<=3){
        sum+= ways(i+3);
    }
    m.insert({i, sum});
    return sum;
}

int main(){
    a[0] = 0;
    while(fin>>nr){
        a[n] = nr;
        n++;
    }
    sort(a, a+n);
    a[n] = a[n-1] + 3;
    fout<<"Part 1: "<<countDiff(1) * countDiff(3)<<endl;
    ///Part 2 takes a while to return the result
    /// 'cause of complexity 3^n
    fout<<"Part 2: "<<ways(0);
    return 0;
}
