// 2023-10
#include <iostream>
#include <cmath>

int main() {
    std::cout << INFINITY << std::endl;
    // inf
    std::cout << NAN << std::endl;
    // nan
    std::cout << isgreater(42, 10) << std::endl;
    // 1
    std::cout << isless(42, 10) << std::endl;
    // 0
    std::cout << isnan(NAN) << std::endl;
    // 1
    std::cout << isinf(INFINITY) << std::endl;
    // 1
    std::cout << isfinite(42) << std::endl;
    // 1

    // trigonometric functions
    std::cout << cos(42) << std::endl;
    // -0.399985
    std::cout << sin(42) << std::endl;
    // -0.916522
    std::cout << tan(42) << std::endl;
    // 2.29139
    
    // exponential and logarithmic functions
    std::cout << exp(2) << std::endl;
    // 7.38906
    std::cout << exp2(2) << std::endl; // binary exponential function
    // 4
    std::cout << log(10) << std::endl; // natural logarithm
    // 2.30259
    std::cout << log10(10) << std::endl;
    // 1
    std::cout << log2(8) << std::endl;
    // 3
    // power functions
    std::cout << pow(2, 3) << std::endl;
    // 8
    std::cout << sqrt(16) << std::endl;
    // 4
    std::cout << cbrt(27) << std::endl;
    // 3
    
    // rounding and remainder functions
    std::cout << ceil(41.5) << std::endl;
    // 42
    std::cout << floor(42.5) << std::endl;
    // 42
    std::cout << trunc(42.5) << std::endl;
    // 42
    std::cout << round(41.5) << std::endl;
    // 42
    std::cout << rint(42.5) << std::endl; // round to nearest integer
    // 42
    std::cout << nearbyint(42.5) << std::endl; // round to nearby integer
    // 42
    std::cout << remainder(142, 100) << std::endl;
    // 42
    
    // manipulation functions
    std::cout << copysign(42, -1) << std::endl;
    // -42
    std::cout << nan("42") << std::endl;
    // nan
    
    // minimum, maximum, difference functions
    std::cout << fdim(52, 10) << std::endl; // positive difference
    // 42
    std::cout << fmax(42, 10) << std::endl;
    // 42
    std::cout << fmin(42, 10) << std::endl;
    // 10
    
    // other functions
    std::cout << fabs(-12.5) << std::endl; // absolute value (can handle floating-point)
    // 12.5
    std::cout << abs(-42) << std::endl; // absolute value (only for integers)
    // 42
    std::cout << fma(42.5, 10, 200) << std::endl; // fused multiply-add
    // 625
}