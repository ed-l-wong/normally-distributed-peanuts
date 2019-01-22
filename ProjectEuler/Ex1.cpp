/*
Euler 1.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <iostream>
using namespace std;

void problem() {
  cout << "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get \
  3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or \
  5 below 1000." << endl << endl;
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

int formula(float n, float m) {
  return (n/2)*(n+1)*m;
}

/*
This one take the sum of consecutive numbers by using 1+2+3+...+n = (n/2)(n+1)

I think this should be the most efficient one as there is no loop required as we utilise the arithmetic formula.
*/
int best_multiple(int a) {
  int x = (a-1)/3;
  int y = (a-1)/5;
  int z = (a-1)/15;
  cout << x << " summed to: " << formula(x,3) << endl;
  cout << y << " summed to: " << formula(y,5) << endl;
  cout << z << " summed to: " << formula(z,15) << endl;
  return formula(x,3) + formula(y,5) - formula(z,15);
}


int main() {
  problem();
  int input;
  cout << "Please input an upper bound." << endl;
  cin >> input;
  cout << "Total is: " << best_multiple(input) << endl;
  cout << "Actual answer is: " << improved_multiples(input) << endl;
}
