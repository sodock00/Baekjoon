#include <iostream>
using namespace std;

int main() {
	int a, b, first,second,third;
	cin >> a;
	cin >> b;
	first = (b % 10) * a;
	second = ((b % 100) - (b % 10))/10 * a;
	third = (b - (b % 100))/100 * a;
	cout << first << endl << second << endl << third << endl
		<< (first + second * 10 + third * 100);
	return 0;
}