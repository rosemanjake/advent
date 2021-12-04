#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
using namespace std;

vector<string> getInput(string filename) {
    ifstream file(filename);

    string text;
    vector<string> inputstr;

    while (getline(file, text)) {
        inputstr.push_back(text);
    }

    file.close();
    return inputstr;
}

tuple<string, string> split(string line, string delimiter) {
    string str1;
    string str2;
    
    int start = 0;
    int end = line.find(delimiter);
    while (end != -1) {
        str1 = line.substr(start, end - start);
        start = end + delimiter.size();
        end = line.find(delimiter, start);
        str2 = line.substr(start, end - start);
    }

    return tuple<string, string>(str1, str2);
}

tuple<int, int> getSolution(vector<string> input) {
    int hpos1 = 0;
    int depth1 = 0;
    int aim1 = 0;

    int hpos2 = 0;
    int depth2 = 0;
    int aim2 = 0;

    for (size_t i = 0; i < input.size(); i++) {
        tuple<string, string> splits = split(input[i], " ");
        string direction = get<0>(splits);
        int degree = stoi(get<1>(splits));

        if (direction == "forward") {
            // part 2
            hpos1 = hpos1 + degree;
            // part 2
            hpos2 = hpos2 + degree;
            depth2 = depth2 + (aim2 * degree);
        }
        else if (direction == "up") {
            // part 1
            depth1 = depth1 - degree;
            
            // part 2
            aim2 = aim2 - degree;
        }
        else if (direction == "down") {
            // part 1
            depth1 = depth1 + degree;
            // part 2
            aim2 = aim2 + degree;
        }
        else {
            cout << "something has gone wrong";
        }
    }
    
    return tuple<int, int>(hpos1 * depth1, hpos2 * depth2);
}

int main()
{
    vector<string> input = getInput("day2.txt");
    tuple<int, int>solution = getSolution(input);
    cout << "The solution for part 1 is " << get<0>(solution) << endl << "The solution for part 2 is " << get<1>(solution);
}

