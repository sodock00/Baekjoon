#include <iostream>
#include <algorithm>
using namespace std;

int arr[100001];

bool binary_search(int arrSize, int key) {
	int start = 0;
	int end = arrSize - 1;
	int mid;

	while (end >= start) {
		mid = (start + end) / 2;

		if(arr[mid] == key) {
			return true;
			break;
		} 
		else if (arr[mid] > key) {   
			end = mid - 1;
		}
		else {  
			start = mid + 1;
		}
	}
	return false;
}

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);

	cin >> M;
	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;
		if(binary_search(N, num)==true)
			cout << "1\n";
		else cout << "0\n";
	}
	
}