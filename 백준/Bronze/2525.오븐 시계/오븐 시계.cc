#include <iostream>
using namespace std;

int main() {
	int h, m, t, ah, am;
	cin >> h >> m;
	cin >> t;
	ah = t / 60, am = t % 60;	

	if (m + am > 59) {
		if (h + ah > 22) cout << (h + ah + 1) - 24 << " " << m + am - 60;
		else cout << h + ah + 1 << " " << m + am - 60;
	}
	else {
		if (h + ah > 23) cout << h + ah - 24 << " " << m + am;
		else cout << h + ah << " " << m + am;
	}
	return 0;
}