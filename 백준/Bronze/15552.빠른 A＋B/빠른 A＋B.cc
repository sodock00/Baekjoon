#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int c; cin >> c;
	int* a = new int[c];
	int* b = new int[c];
	for (int i = 0; i < c; i++) {
		cin >> a[i] >> b[i] ;
	}
	for (int i = 0; i < c; i++) {
		cout << a[i] + b[i] << "\n";
	}

	return 0;
}
