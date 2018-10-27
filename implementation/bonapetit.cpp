#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
 long n,k,bc,ba=0;
cin>>n>>k;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
}
cin>>bc;
for( long i=0;i<n;i++){
    if(i!=k){
        ba+=a[i];
    }
}
int g=ba/2;
if(g==bc){
    cout<<"Bon Appetit"<<endl;
}
else{
    cout<<bc-g;
}   /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
