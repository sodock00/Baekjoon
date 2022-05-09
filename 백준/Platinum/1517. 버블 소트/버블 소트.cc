#include <iostream>
using namespace std;
// 버블 소팅으로 하면 N^2 > 시간초과
// merge sort (합병 정렬)로 해야댐
// 와 이거 징챠 어렵네ㅠ

void merge_sort(int *arr, int start, int end);
void merge(int* arr, int start, int mid, int end);
long long result = 0;

int main() {
	int N, temp;
	cin >> N;
	int *A = new int[N];
	
	for (int i = 0; i < N; i++)
		cin >> A[i];

	merge_sort(A, 0, N - 1);
	cout << result ;


}

// 배열 반으로 가르는 함수 (쪼갬)
void merge_sort(int* arr, int start, int end) {
	if (start < end) {
		int mid = (start + end) / 2;
		merge_sort(arr, start, mid); // 왼쪽 배열 정렬
		merge_sort(arr, mid+1, end); // 오른쪽 배열 정렬
	
		merge(arr, start, mid, end); // 자른거 합치기

	}
}
void merge(int* arr, int start, int mid, int end) {
	int left = start;
	int right = mid + 1;
	int c = start;
	int count = 0;

	// 정렬된 배열
	int sorted[500000];

	// 분할 정렬된 배열 merge
	while (left <= mid && right <= end) {
		if (arr[left] <= arr[right]) {
			sorted[c] = arr[left];
			left++;
			result += (long long)count;
		}
		else {
			// merge에서 바꾸는 경우 두 수가 떨어진 거리만큼을 count해준다. 
			sorted[c] = arr[right];
			right++;
			count ++;
		}
		c++;
	}

	// 남아 있는 오른쪽 값들 모두 복사
	if (left > mid) {
		for (int t = right; t <= end; t++) {
			sorted[c] = arr[t];
			c++;
			count++;
		}
	}
	// 남아 있는 왼쪽 값들 모두 복사
	else {
		for (int t = left; t <= mid; t++) {
			sorted[c] = arr[t];
			c++;
			result += (long long)count;
		}
	}

	// 정렬된 배열 삽입
	for (int t = start; t <= end; t++) {
		arr[t] = sorted[t];
	}
	
}

