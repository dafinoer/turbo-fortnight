#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
      int i,no,arr[200],j,sz,p,t,c;
cin>>no;
arr[0]=1;
sz=1;
for(i=2;i<=no;i++)
    {
        p=sz;c=0;
        for(j=0;j<sz;j++)
            {
                t=arr[j]*i+c;
                c=t/10;
                arr[j]=t%10;
        }
    while(c)
        {
            arr[j]=c%10;sz++;j++;
            c=c/10;
    }
}
for(i=sz-1;i>=0;i--)
    {
    cout<<arr[i];
} /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
