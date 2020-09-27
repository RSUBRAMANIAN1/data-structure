#include<bits/stdc++.h>
#include<vector>

using namespace std;

int main() {

 int t=0;
 cin>>t;
 while(t--)
 {
 
    int n=1,flag=-1;

    cin>>n;
    int ar[n];
	for(int i=0;i<n;i++)
	    { cin>>ar[i];
		  }  

	if(n==1) 
	{   
		cout<<ar[0]<<endl;
	}
	else
	{
	int rsum=0,lsum=0;
	 for(auto i:ar)
	  { rsum=rsum+i;
	   }
	 for(int i=0;i<n;i++)
	  {  //cout<<lsum<<" "<<rsum-ar[i]<<endl;
	  		if(lsum==(rsum-ar[i]))
	  	 { cout<<i+1<<endl;
	  	    flag++;
		   }
	    if(lsum<rsum)
		{ lsum+=ar[i];
		    rsum-=ar[i];
		 }
	  
		
	  }
	}
 if(flag==-1)
  cout<<-1<<endl;
}
	return 0;
}


/*
#include<bits/stdc++.h>
using namespace std;
int main()
{
int t, n, temp, sum, start, end; cin>>t;
while(t--) {
cin>>n>>sum;
vector<int> v(n);
for(auto& i: v) cin>>i;
temp=end=start=0;
while((!(temp < sum && start == n)&& !(temp == sum))) {
	cout<<temp<<endl;
if (temp < sum) temp += v[start++];
if (temp > sum) temp -= v[end++];
}
if (temp == sum) 
cout<<end+1<<" "<<start<<" "<<endl;
else
cout<<-1<<endl;
    
} 

return 0; 
    
}
*/


