#include <iostream>
#include <string>

class Company {
public:
    std::string name;

    Company(std::string company_name, double budget) 
        : name(company_name), annual_budget(budget) {}

    double get_budget() const {
        return annual_budget;
    }

    void set_budget(double updated_budget) {
        annual_budget = updated_budget;
    }

private:
    double annual_budget;

    void internal_audit() const {
        std::cout << "Performing internal audit for " << name << "...\n";
    }
};

int main() {
    Company miftahcoding("MiftahCoding", 1000000);
    std::cout << miftahcoding.get_budget() << "\n";

    // std::cout << miftahcoding.annual_budget << "\n"; // Compilation error: private member

    miftahcoding.name = "MiftahCoding Inc.";
    miftahcoding.set_budget(200000000);
    std::cout << miftahcoding.get_budget() << "\n";

    // miftahcoding.annual_budget = 20000000; // Compilation error: private member

    return 0;
}