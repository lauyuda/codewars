#include <string>
using namespace std;

vector<std::string> wave(string y){
  int word_length = y.length();
  vector<string> mexico;
  string letter;
  string word = y;
    
  if (word_length == 0) {
    return mexico;
  }
  
  for (int i = 0; i < word_length; i++) {
    letter = toupper(y[i]);
    if (letter == " ") {
      continue;
    }
    
    word.replace(i, 1, letter);
    mexico.push_back(word);
    word = y;
  }
  
  return mexico;
}