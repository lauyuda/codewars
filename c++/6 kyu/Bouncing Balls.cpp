using namespace std;
class Bouncingball
{
public:
  static int bouncingBall(double h, double bounce, double window) {
    int times = 0;
    
    if(h <= 0 || bounce <= 0 || bounce >= 1 || h <= window) {
      return -1;
    }
    
    while (h > window) {
      h *= bounce;
      times++;
    }
    
    times = times * 2 - 1;
      
    return times;
  }
};