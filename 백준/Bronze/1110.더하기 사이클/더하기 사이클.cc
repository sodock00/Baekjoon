#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int N, t, n, _new=0;
	cin >> N;
	int cycle = 0;
	int input = N;
	while (true) {
		n = (input / 10 + input % 10) % 10;
		t = input % 10;
		_new = t * 10 + n;
		input = _new;
		cycle++;
		if (_new == N) break;
	}
	cout << cycle;
	return 0;
}
