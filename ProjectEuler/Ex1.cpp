/*
Euler 1.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <iostream>
using namespace std;

void problem() {
  cout << "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000." << endl << endl;
}


int naive_multiples(int a) {
  int total = 0;

  for (int i = 0; i < a; i++) {
    if (i%3 == 0 || i%5 == 0)
      total += i;
  }

  return total;
}

/*
This method is 60% of the computation compared to the naive approach:
(1/3)a + (1/5)a + (1/3)(1/5)a = (9/15)a
*/
int improved_multiples(int a) {
  int total = 0;

  for (int i = 1; i <= (a-1)/3; i++) {
      total += i*3;
  }

  for (int i = 1; i <= (a-1)/5; i++) {
      total += i*5;
  }

  for (int i = 0; i <= (a-1)/15; i++) {
      total -= i*15;
  }

  return total;
}


int main() {
  problem();
  int input;
  cout << "Please input an upper bound." << endl;
  cin >> input ;
  cout << naive_multiples(input) << endl;
  cout << improved_multiples(input) << endl;
}
