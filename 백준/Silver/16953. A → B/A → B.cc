#include <iostream>
using namespace std;

int first(int num) {
	num = num / 2;
	return num;
}
int second(int num) {
	num = (num - 1) / 10;
	return num;
}

int main() {
	int a, b;
	int count = 1;
	cin >> a >> b;

	while (a!=b) {
		if (b % 2 == 0 && a < b) {
			b = first(b);
			count++;
		}
		else if (b % 10 == 1 && a < b) {
			b = second(b);
			count++;
		}
		else {
			cout << "-1" << endl;
			break;
		}
	}

	if(a==b) cout << count << endl;
	return 0;
}