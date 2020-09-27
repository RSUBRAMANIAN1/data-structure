#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

void maxval(int a[],int n)
{
	int presum[n];
	presum[0]=a[0];
	 for (int i = 1; i < n; i++) {
 
            presum[i] = presum[i - 1] + a[i];
        }
    int l[n]={0},r[n]={0};
    stack<int> st;
    stack<int> st1;
    for (int i = 1; i < n; i++) {
 

            while (!st.empty()
                   && a[st.top()] >= a[i])
                st.pop();
 
            if (!st.empty())
                l[i] = st.top() + 1;
            else
                l[i] = 0;
                
            st.push(i);
        }
         for (int i = 1; i < n; i++) {
		       cout<<l[i]<<" ";
		 }
		 cout<<'\n';
         for (int i = n - 1; i >= 0; i--) {
 
            while (!st1.empty()
                   && a[st1.top()] >= a[i])
                st1.pop();
 
            if (!st1.empty())
                r[i] = st1.top() - 1;
            else
                r[i] = n - 1;
 
            st1.push(i);
        }
         for (int i = 0; i < n; i++) {
		       cout<<r[i]<<" ";
		 }
		 cout<<'\n';
        
         int maxProduct = 0;
 
        int tempProduct;
 

        for (int i = 0; i < n; i++) {
             cout<<l[i]<<'\n';
         if(l[i]==0)
		tempProduct= a[i]* (presum[r[i]]);
		else
		 tempProduct= a[i]*(presum[r[i]]-presum[l[i] - 1]);
                

            maxProduct = max(maxProduct,tempProduct);
        }
        cout<<maxProduct;
       
}

int main(){
    int arr[] = {3, 1, 6, 4, 5, 2};
    int len = sizeof(arr)/sizeof(arr[0]);
   maxval(arr,len);
    
    return 0;
}

