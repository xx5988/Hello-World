#pragma once

#include <iostream>

class Animal {
public:
    Animal(const std::string& name) : name(name) {}
    void sayHello() const {
        std::cout << "Hello, My name is: " << name << std::endl;
    }

    virtual void saySomething() const = 0;
private:
    std::string name;
};



class Cat: public Animal {
public:
    Cat(const std::string& name) : Animal(name) {}
    void saySomething() const override {
        std::cout << "I am a little cat." << std::endl;
    }   
};