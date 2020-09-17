bool isPrime(int num) {
  
  if(num < 2) {
    std::cout << "false: " << num << std::endl;
    return false;
  }
  
  int square = std::sqrt(num);
  
  for(int i = 2; i <= square; i++) {
    if(num % i == 0){
      return false;  
    }
  }
  return true;
}