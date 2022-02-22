#include <iostream>
using namespace std;

int main() {
	int n, max;
	double sum = 0;
	cin >> n;
	int* score = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> score[i];
		if(i==0) max = score[0];
		if (score[i] > max) max = score[i];
		sum += score[i];
	}
	sum = (sum / max * 100)/n;

	cout << fixed;
	cout.precision(6);
	cout << sum ;

	
	return 0;
}
