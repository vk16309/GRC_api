//this code is written by Tatwick Utkarsh.
#include<bits/stdc++.h>
using namespace std;
int main()
{
   int ati[5],bt[5];
   for(int i=0;i<5;i++)
   {
     cin>>ati[i]>>bt[i];
   }
   int cumulative=bt[0]+ati[0],wt=0,tat=bt[0]-ati[0];
   for (int i=1;i<5;i++)
   {
      if(ati[i]<cumulative)
      {wt+=cumulative - ati[i];
      }
      cumulative+=bt[i];
      tat+=cumulative-ati[i];
   }
   cout<<wt/5.0<<" "<<tat/5.0<<endl;
}
