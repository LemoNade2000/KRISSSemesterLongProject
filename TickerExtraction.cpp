#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define MOD 1000000007

ifstream in;
ofstream out;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    in.open("TickerTable.txt");
    out.open("TickerList.csv");
    string str;
    string compStr = "NyseSymbol";
    int cnt = 0;
    while(in >> str){
        if(str.size() > 3 && compStr.compare(0, 10, str, 3, 10) == 0){
            if(cnt != 0) out << ",";
            string symbol = "";
            for(int pos = 14; pos < str.size(); pos++){
                if(str[pos] == '}'){
                    break;
                }
                symbol.push_back(str[pos]);
            }
            out << symbol;
            cnt++;
        }
    }
    out.close();
    return 0;
}