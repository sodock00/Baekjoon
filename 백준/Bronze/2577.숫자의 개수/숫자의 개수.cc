#include <iostream>
using namespace std;

int main() {
	int arr[10] = {};
	int a, b, c, res;
	cin >> a; cin >> b; cin >> c;
	res = a * b * c;
	while (res != 0) {
		arr[res % 10]++;
		res /= 10;
	}
	for (int i = 0; i < 10; i++) {
		cout << arr[i] << "\n";
	}
	return 0;
}
