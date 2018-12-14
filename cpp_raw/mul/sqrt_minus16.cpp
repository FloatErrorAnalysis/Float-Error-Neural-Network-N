#include "cmath" 
using namespace std;
double sqrt_minus_error(double x) {
   return sqrt(16*x+1) - sqrt(16*x);
}