#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	int max, min ;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (i == 0) { max = arr[0]; min = arr[0]; }
		if (arr[i] > max) max = arr[i];
		if (arr[i] < min)min = arr[i];
	}
	cout << min << " " << max;
	return 0;
}
