#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int a=1, b=1, i = 0;

	while (true){
		cin >> a >> b;
		if (a == 0 && b == 0) break;
		cout << a + b << "\n";
	}

	return 0;
}
