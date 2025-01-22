#include <iostream>
#include "hello.hpp"


int main() {
    std::cout << "Hello, World!" << std::endl;
    Cat cat("Tom");
    cat.sayHello();
    cat.saySomething();
    return 0;
}