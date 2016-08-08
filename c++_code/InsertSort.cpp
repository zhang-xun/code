#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int  mylist[8]  = {8,7,6,5,4,3,2,1};
	
	void Insert(int *, int);

	Insert(mylist,8);

	cout << "after sorting " <<endl;
	for(int  i = 0; i < 8; i++)
	{
		cout << mylist[i] << endl;
	}

	return 0;
}


void Insert(int *a ,int n)
{
	int temp,i,j ;
	for(i = 1; i < n; i++)
	{
		temp = a[i];
		for( j = i; j > 0 && a[j-1] > temp; j--)
		{
			a[j] = a[j-1];	
		
		}
		a[j] = temp;

	
	}


}
