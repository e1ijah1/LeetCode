//
// Created by F1renze on 2019-03-22.
//


#include <map>
#include <string>
#include <iostream>

using namespace std;


class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int num = 0;
        for (char& c : S) {
            if (J.find(c) != string::npos)
                num++;
        }
        return num;
    }
};

int main(int argc, char *argv[]) {
    Solution().numJewelsInStones("aA", "aAAbbbb");
    return 0;
}

