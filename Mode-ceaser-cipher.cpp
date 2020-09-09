#include <iostream>  
#include <cstring>  
using namespace std; 
void func(string key , string buf)
{ string code=" ";
  int lk=key.length();
  int lb=buf.length();
  char k[lk];
  char b[lb+1];
  for(int i=0;i<lk;i++){k[i]=key[i];}
  for(int i=0;i<lb;i++){b[i]=buf[i];}

  int j=0,i=0;
  
  for(;i<lb;i++)
  {   	if(j==lk)
  	  { j=0;
	  }
	  if(int(b[i]+char(k[j]-'a'))>122){
	  	b[i]=(b[i]+char(k[j]-'a'))%'z'+char(96);
	  }
	  else
	  {
	  	b[i]=b[i]+char(k[j]-'a');
	  }
  	
  
	  j++;
  }
  b[i]='\0';
  code.append(b);
   cout<<code;
 } 
int main()  
{  

 string key;
 string buffer;
 cin>>key>>buffer;
 func(key,buffer);
 


}  
