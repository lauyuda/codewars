#include <map>
using namespace std;

int solve(const string &s)
{
  map<string, int> alphabets = {{"a" , 1}, {"b", 2}, {"c" , 3}, {"d", 4}, {"e" , 5}, {"f", 6}, {"g" , 7}, {"h", 8},
                                 {"i" , 9}, {"j", 10}, {"k" , 11}, {"l", 12}, {"m" , 13}, {"n", 14}, {"o" , 15}, {"p", 16},
                                 {"q" , 17}, {"r", 18}, {"s" , 19}, {"t", 20}, {"u" , 21}, {"v", 22}, {"w" , 23}, {"x", 24},
                                 {"y" , 25}, {"z", 26}};
  string vowels = "aeiou";
  string letter = "";
  int word_length = s.length();
  int max = 0;
  int current = 0;
  for (int i = 0; i < word_length; i++) {
    cout << s[i] << endl;
    letter = s[i];
    if (vowels.find(s[i]) == string::npos) {
      current += alphabets[letter];
      if (max < current) {
        max = current;
      }
    }
    else {
      current = 0;
    }
  }
  return max;
}