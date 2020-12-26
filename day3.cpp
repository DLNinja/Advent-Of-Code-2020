#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

string line;
vector<string> treemap;

int getMap(vector<string> treemap, int d, int r){
    int ct = 0, i = 0, j=0;
    while(i<treemap.size()){
        if(treemap[i].at(j)=='#'){
            ct++;
        }
        i+= d;
        j = (j+r)%treemap[0].size();
    }
    return ct;
}

int main(){
    while(fin>>line){
        treemap.push_back(line);
    }
    fout<<"Part 1: "<<getMap(treemap, 1, 3)<<endl;
    fout<<"Part 2: "<<1LL * getMap(treemap, 1, 1) * getMap(treemap, 1, 3) * getMap(treemap, 1, 5) * getMap(treemap, 1, 7) * getMap(treemap, 2, 1);
    return 0;
}
