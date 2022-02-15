#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; cin >> t;
	int* a = new int[t];
	int* b = new int[t];

	for (int i = 0; i < t; i++) {
		cin >> a[i] >> b[i];
	}
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": " << a[i] + b[i] << "\n";
	}

	return 0;
}
