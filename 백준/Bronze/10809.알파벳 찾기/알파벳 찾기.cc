#include <iostream>
#include <string>
using namespace std;

int main() {
	int num = 0;
	string arr;
	cin >> arr; 
	for (int j = 'a'; j <= 'z'; j++) {
		for (int i = 0; i<arr.length(); i++) {
			if ((int)j == (int)arr[i]) {
				cout << i << " ";
				num++;
				break;
			}
		}
		if (num == 0) cout << "-1 ";
		num = 0;
	}
	return 0;
}
