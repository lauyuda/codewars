#include <iostream>
#include <map> 
using namespace std; 

class StockList
{
public:
  static string stockSummary(vector<string> &lstOfArt, vector<string> &categories) {
    string stock = "";
    map<string, int> stocklist; 
    map<string, int>::iterator itr; 
    string key;
    string search_key;
    int cat_size = categories.size();
    int lstOfArt_size = lstOfArt.size();
    int space_index;
    int number;
    
    if (cat_size == 0 || lstOfArt_size == 0) {
      return stock;
    }
     
    for (int i = 0; i < cat_size; i++) {
      key = categories.at(i)[0];
      stocklist.insert({key, 0});
      
      for(int j = 0; j < lstOfArt_size; j++) {
        search_key = lstOfArt.at(j)[0];
        if(search_key == key) {
          space_index = lstOfArt.at(j).find(" ") + 1;
          number = stoi(lstOfArt.at(j).substr(space_index));
          //cout << "number after space: " << number << endl;
          stocklist[search_key] += number;
        }
        
      }
      
    }
    
    for (itr = stocklist.begin(); itr != stocklist.end(); ++itr) { 
        cout << "(" << itr->first << " : " << itr->second << ") - ";
    } 
    
    for (int i = 0; i < cat_size; i++) {
      key = categories.at(i)[0];
      stock = stock + "(" + key + " : " + to_string(stocklist[key]) + ")";
      if(i + 1 != cat_size) {
        stock += " - ";
      }
    }    
    
    return stock;
    }
};