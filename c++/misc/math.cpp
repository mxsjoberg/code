#include <iostream>
#include <cmath>

int main() {
    std::cout << INFINITY << std::endl; // inf
    std::cout << NAN << std::endl; // nan
    std::cout << isgreater(42, 10) << std::endl; // 1
    std::cout << isless(42, 10) << std::endl; // 0
    std::cout << isnan(NAN) << std::endl; // 1
    std::cout << isinf(INFINITY) << std::endl; // 1
    std::cout << isfinite(42) << std::endl; // 1

    // trigonometric
    std::cout << cos(42) << std::endl; // -0.399985
    std::cout << sin(42) << std::endl; // -0.916522
    std::cout << tan(42) << std::endl; // 2.29139
    
    // exponential and logarithmic
    std::cout << log10(10) << std::endl; // 1
    std::cout << log2(8) << std::endl; // 3
    std::cout << exp(2) << std::endl; // 7.38906

    // binary exponential function
    std::cout << exp2(2) << std::endl; // 4

    // natural logarithm
    std::cout << log(10) << std::endl; // 2.30259
    
    // power and root
    std::cout << pow(2, 3) << std::endl; // 8
    std::cout << sqrt(16) << std::endl; // 4
    std::cout << cbrt(27) << std::endl; // 3
    
    // rounding and remainder
    std::cout << ceil(41.5) << std::endl; // 42
    std::cout << floor(42.5) << std::endl; // 42
    std::cout << trunc(42.5) << std::endl; // 42
    std::cout << round(41.5) << std::endl; // 42
    std::cout << remainder(142, 100) << std::endl; // 42

    // round to nearest integer
    std::cout << rint(42.5) << std::endl; // 42
    
    // round to nearby integer
    std::cout << nearbyint(42.5) << std::endl; // 42
    
    // manipulation
    std::cout << copysign(42, -1) << std::endl; // -42
    std::cout << nan("42") << std::endl; // nan
    
    // minimum, maximum, difference
    std::cout << fdim(52, 10) << std::endl; // 42
    std::cout << fmax(42, 10) << std::endl; // 42
    std::cout << fmin(42, 10) << std::endl; // 10
    
    // absolute value (can handle floating-point)
    std::cout << fabs(-12.5) << std::endl; // 12.5

    // absolute value (only for integers)
    std::cout << abs(-42) << std::endl; // 42

    // fused multiply-add
    std::cout << fma(42.5, 10, 200) << std::endl; // 625
}