#include <iostream>
using namespace std;

int sequence(int& n) {
	if (n < 100) return 1;
	if (n >= 100) {
		int a, b, c;
		a = n / 100;
		b = (n - a * 100) / 10;
		c = n % 10;
		if ((a - b) == (b - c)) return 1;
		return 0;
	}
	return 0;
}
int main() {
	int n, sum = 0;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		sum += sequence(i);
	}
	cout << sum;
	return 0;
}
