#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int n, a[1010], nr;

bool bin(int st, int dr, int v[], int x){
    if(st>dr){
        return 0;
    }else{
        int mij=(st+dr)/2;
        if(v[mij]==x){
            return 1;
        }
        if(x<v[mij]){
            return bin(st, mij-1, v, x);
        }else{
            return bin(mij+1, dr, v, x);
        }
    }
}

void part1(){
    for(int i=0;i<n;i++){
        if(bin(0, n-1, a, 2020-a[i])){
             fout<<a[i]*(2020-a[i])<<" ";
             break;
        }
    }
}

void part2(){
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int sum = a[i] + a[j];
            if(sum<2020){
                if(bin(0, n-1, a, 2020-sum)){
                    fout<<a[i]*a[j]*(2020-sum)<<" ";
                    break;
                }
            }
        }
    }
}

int main(){
    while(fin>>nr){
        a[n] = nr;
        n++;
    }
    sort(a, a+n);
    part1();
    part2();
    return 0;
}

