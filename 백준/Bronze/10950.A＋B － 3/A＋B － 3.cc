#include <iostream>
using namespace std;

int main() {
	int c;
	cin >> c;
	int* a = new int[c];
	int* b = new int[c];
	for (int i = 0; i < c; i++)
		cin >> a[i] >> b[i];
	for (int i = 0; i < c; i++)
		cout << a[i] + b[i] << endl;
	delete[]a; 
	delete[]b;
	return 0;
}
