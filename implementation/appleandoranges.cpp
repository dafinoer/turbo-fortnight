#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int s,t,a,b,m,n,ap,apcnt = 0,ora,orcnt = 0;
    cin >> s >> t >> a >> b >> m >> n;
    for(int i = 0;i < m;i++){
        cin >> ap;
        if(a+ap >= s && a+ap <= t)apcnt++;
    }
    for(int i = 0;i < n;i++){
        cin >> ora;
        if(b+ora >= s && b+ora <= t)orcnt++;
    }
    cout << apcnt <<endl<< orcnt << endl;
    return 0;
}
