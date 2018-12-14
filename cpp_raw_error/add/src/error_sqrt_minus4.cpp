#include "cmath"
#include "iRRAM.h"
using namespace iRRAM;
double sqrt_minus_error(double x) {
   return sqrt(x+5) - sqrt(x+4);
}

REAL sqrt_minus_real(const REAL &x) {
  return REAL(1) / (REAL(sqrt(x+4 + 1)) + REAL(sqrt(x+4)));
}
void generate_data(double low_bound, double high_bound, double gap) {
  orstream file("../../../dataset/add/4.csv", std::ios::out);
  int number = static_cast<int>((high_bound - low_bound) / gap);
  double current_input = low_bound;
  for (int i = 0; i <= number; i++) {
      double result_error = sqrt_minus_error(current_input);
      REAL result_real = sqrt_minus_real(current_input);
      file << current_input << "," << abs(REAL(result_real) - REAL(result_error)).as_double() << "\n";
      current_input += gap;
  }
}
void compute() {
  generate_data(0, 10000, 1);
}
