#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int numCnt[9];

int main(void){
  string N;
  cin >> N;

  for(auto c : N){
    if(c == '9')
      numCnt[6]++;
    else 
      numCnt[c-'0']++;
  }

  numCnt[6] = (numCnt[6]+1)/2;

  cout << *max_element(numCnt,numCnt+9);
}
