#include "cmath" 
using namespace std;
double sqrt_minus_error(double x) {
   return sqrt(9*x+1) - sqrt(9*x);
}