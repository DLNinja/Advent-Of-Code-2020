#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

string line;

int ct1, ct2, a[30], cnt;

int main(){
    while(getline(fin, line)){
        /// Part 1:
        if(line==""){
            for(int i=0;i<='z'-'a';i++){
                ct1+=a[i];
                a[i] = 0;
            }
        }else{
            for(char ch: line){
                a[ch-'a'] = 1;
            }
        }
        /// Part 2:
        if(line==""){
            if(cnt!=0){
                for(int i=0;i<='z'-'a';i++){
                    if(a[i]==cnt){
                        ct2++;
                    }
                    a[i] = 0;
                }
                cnt = 0;
            }
        }else{
            cnt++;
            for(char ch: line){
                a[ch-'a'] ++;
            }
        }
    }
    fout<<"Part 1: "<<ct1<<'\n';
    fout<<"Part 2: "<<ct2;
    return 0;
}
