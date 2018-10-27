#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    long long int max,min,summax=0,summin=0,i;
    cin >> n;
    int arr[n];
    for(i=0;i<n;i++)
        {
        cin>>arr[i];
    }
    max=arr[0];
    min=arr[0];
    for(i=0;i<n;i++)
        {
        if(arr[i]>max)
        {max=arr[i];   summax++;}
        else if(arr[i]<min)
        {min=arr[i];summin++;}
    }
    cout<<summax<<" "<<summin;
      return 0;
}
