#include <iostream>
using namespace std;

int main()
{
    string names[8] = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"};
    string target;
    bool found = false;
    cout << "Enter the name you whant to find: " << endl;
    cin >> target;

    for (int i = 0; i < 8; i++)
    {
        if (names[i] == target)
        {
            cout << "Name found at " << i + 1 << endl;
            found = true;
            break;
        }
    }
    if (!found)
    {
        cout << "the name is not found";
    }
}