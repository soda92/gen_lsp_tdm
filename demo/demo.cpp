#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector<string> arr = {"hello", "lsp", "world", "!"};
  for (auto s : arr) {
    cout << s << ' ';
  }
}