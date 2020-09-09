#include <functional>
#include <queue>
#include <vector>
#include <iostream>
using namespace std;
template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        cout << q.top() << " ";
        q.pop();
    }
    cout << '\n';
}
 
int main() {
    priority_queue<int, std::vector<int>, std::greater<int> > q;
    int n,t,k;
    cin>>n;
    while(n-->0){
	   cin>>t;
	   int ar[t];
	   for(int i=0;i<t;i++)cin>>ar[i];
	   cin>>k;
    for(int i=0;i<t;i++ )
    {   
	
        q.push(ar[i]);
         if(q.size()>k)
        {
        	q.pop();
		}
       
	 }
   } 
	cout<<q.top();
    
 
    /*std::priority_queue<int, std::vector<int>, std::greater<int> > q2;
 
    for(int n : {1,8,5,6,3,4,0,9,7,2})
        q2.push(n);
 
    print_queue(q2);
 
    // Using lambda to compare elements.
    auto cmp = [](int left, int right) { return (left ^ 1) < (right ^ 1); };
    std::priority_queue<int, std::vector<int>, decltype(cmp)> q3(cmp);
 
    for(int n : {1,8,5,6,3,4,0,9,7,2})
        q3.push(n);
 
    print_queue(q3);
    */
 
}
