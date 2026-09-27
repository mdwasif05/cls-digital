#include <iostream>
using namespace std;

class person {
protected:
    string name;
public:
    void setdata(string n) {
        name = n;
    }
};

class student : public person {
private:
    int student_id;
public:
    void setstudentid(int m) {
        student_id = m;
    }
    void display() {
        cout << "Name: " << name << endl;
        cout << "Id: " << student_id << endl;
    }
};

int main() {
    student s;
    s.setdata("Altaf");
    s.setstudentid(123);
    s.display();
    return 0;
}
