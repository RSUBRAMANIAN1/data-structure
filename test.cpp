#include<iostream>
using namespace std;
int fact(int a)
{
	if(a==0 || a==1)
	return 1;
	long unsigned int arr[a];
	arr[0]=1;
	arr[1]=1;
	for(int i=1;i<=a;i++)
	{ 
	   	arr[i] = i*arr[i-1];
	}
	return arr[a];
}
int main()
{   
    cout<<fact(20)<<endl;
	return 0;
}
