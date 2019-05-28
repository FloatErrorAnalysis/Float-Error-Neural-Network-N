#include "cmath"
#include "iRRAM.h"
#include "iostream"

using namespace iRRAM;

/**
 * calculation with error
 * @param x input
 * @return result of sqrt minus
 */
double sqrt_minus_error(double x) {
    return sqrt(x + 1) - sqrt(x);
}

/**
 * calculation without error
 * @param x input
 * @return result of sqrt minus
 */
REAL sqrt_minus_real(const REAL &x) {
    return iRRAM::sqrt(x + 1) - iRRAM::sqrt(x);
}

/**
 * Generate data from low bound to high bound, set initial gap as 1
 * @param low_bound low bound
 * @param high_bound high bound
 * @param gap interval
 * @param number the number of data to be generated
 */
void generate_data(double low_bound, double high_bound, double gap) {
    orstream file("../result.csv", std::ios::out);
    file << "x,y\n";

    int number = static_cast<int>((high_bound - low_bound) / gap);
    REAL current_input = low_bound;
    REAL real_gap = REAL(gap);
    REAL max_input = 0.0;
    REAL max_error = 0.0;
    REAL tmp_error;
    for (int i = 0; i <= number; i++) {
        tmp_error = iRRAM::abs(sqrt_minus_real(current_input) - (REAL)(sqrt_minus_error(current_input.as_double())));
        if(tmp_error > max_error){
            max_error = tmp_error;
            max_input = current_input;
        }
        current_input += real_gap;
    }
    file << max_input << "," << max_error << "\n";
}

/**
 * iRRAM main function
 */
void compute() {
    generate_data(100000000000, 1000000000000, 100000000000);
}