#include <iostream>
#include <string>
using namespace std;

int main() {
	int r, t;
	cin >> t;
	string arr;

	for (int i = 0; i < t; i++) {
		cin >> r;
		cin >> arr;
		for (int k = 0; k < arr.length(); k++) {
			for (int j = 0; j < r; j++) {
				cout << arr[k];
			}
		}
		cout << "\n";
	}
	 
	return 0;
}
