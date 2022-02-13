#include <iostream>
using namespace std;

int main() {
	int a, b, c, max = 0;
	cin >> a >> b >> c;

	max = a > b ? (a > c ? a : c) : (b > c ? b : c);

	if (a == b) {
		if (a == c) cout << 10000 + a * 1000;
		else cout << 1000 + a * 100;
	}
	else if (b == c) cout << 1000 + b * 100;
	else if (a == c) cout << 1000 + a * 100;
	else cout << max * 100;
	return 0;
}