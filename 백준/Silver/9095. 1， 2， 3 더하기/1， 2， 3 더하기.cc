#include <iostream>
using namespace std;

int div(int n) {
	if (n == 1) return 1;
	if (n == 2) return 2;
	if (n == 3) return 4;
	else return div(n - 1) + div(n - 2) + div(n - 3);
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int n, result;
		cin >> n;
		result = div(n);
		cout << result << endl;
	}
	return 0;
}