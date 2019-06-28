
#include<iostream>
#include"stdio.h"
#include<string.h>
using namespace std;
int main()
{
	char a[30];
	cout<<"enter a string ";
	gets(a);
	int n=strlen(a);
	char m;
	for(int i=0;i<n;i++)
	{
	char t=a[i];
	m=t;
	int c=(int)t;
	
	if(c>=65 && c<=90)
	{
		if(c-62<26)
		{
			m=(char)(c+3);
		}
		else{
			m=(char)(c-23);
		}
	}
	
	if(c>=97 && c<=122)
	{
		if(c-94<26)
		{
			m=(char)(c+3);
		}
		else{
			m=(char)(c-23);
		}
	}
	if(c>=48 && c<=57)
	{
		if(c-45<10)
		{
			m=(char)(c+3);
		}
		else{
			m=(char)(c-7);
		}
	}	
	a[i]=m;	
}
for(int i=0;i<n;i++)
	{
		cout<<a[i];
	}
	return 0;
}
