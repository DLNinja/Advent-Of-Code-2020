#include <bits/stdc++.h>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int ma;
vector <int> seats;
string line;

int main(){
    while(fin>>line){
        replace(line.begin(), line.end(), 'F', '0');
        replace(line.begin(), line.end(), 'B', '1');
        replace(line.begin(), line.end(), 'R', '1');
        replace(line.begin(), line.end(), 'L', '0');
        int seatId = stoi(line, 0, 2);
        ma = max(ma, seatId);
        seats.push_back(seatId);
    }
    fout<<"Part 1: "<<ma<<'\n';
    sort(begin(seats), end(seats));
    fout<<"Part 2: ";
    for(int i=1; i<seats.size()-1;i++){
        if(seats[i+1]-seats[i] == 2){
            fout<<seats[i]+1<<" ";
            break;
        }
    }
    return 0;
}
