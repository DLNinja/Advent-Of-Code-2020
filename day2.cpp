#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int n, low, high, ans1, ans2;
char s[1010], lit;
string line;

int main(){
    while(getline(fin, line)){
        int pos = line.find(" ");
        string numbers = line.substr(0, pos);
        int pos_dash = numbers.find("-");
        int nr1 = stoi(numbers.substr(0, pos_dash));
        int nr2 = stoi(numbers.substr(pos_dash+1));
        /// Part 1:
        char litera = line.at(pos+1);
        string password = line.substr(pos+4);
        char pos1 = password.at(nr1-1);
        char pos2 = password.at(nr2-1);
        bool a = (pos1==litera), b=(pos2 == litera);
        if(a == !b){
            ans1++;
        }
        /// Part 2:
        int cnt = 0;
        for(char ch: password){
            if(ch == litera){
                cnt++;
            }
        }
        if(cnt>=nr1 && cnt<=nr2){
            ans2++;
        }
    }
    fout<<"Part 1: "<<ans1<<"\n";
    fout<<"Part 2: "<<ans2;
    return 0;
}

