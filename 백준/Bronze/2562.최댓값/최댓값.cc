#include <iostream>
using namespace std;

int main() {
	int max_num, max = 0;
	int arr[9];
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		if (arr[i] >= max)
		{ max = arr[i]; max_num = i; }
	}
	cout << max << "\n";
	cout << max_num + 1;
	return 0;
}
