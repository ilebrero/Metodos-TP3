#include <string>
#include <fstream>
#include <sstream>
#include <iostream> 

int main(int argc, char** argv) {
  std::string fileTestData(argv[1]);

  std::ifstream fileData (fileTestData.c_str());

  int z = 0;
  std::string aeropuerto;
   
  std::cout << "¿Que aeropuerto desea filtrar" << std::endl;
  std::cin >> aeropuerto;

  std::string text = aeropuerto;
  text.append(fileTestData);
  
  std::ofstream fileWrite (text.c_str());
  std::string lineData;
  getline(fileData, lineData); // Pido primer línea para instanciar todo
  fileWrite << lineData << std::endl;

  while (getline (fileData, lineData)) {
    std::istringstream issData(lineData);
    std::istringstream aux(lineData);

    std::string s;
    int k = 1;

    while (getline(aux, s, ',') && k <= 17) {
      if (k == 17) {

        if (aeropuerto == s)
          fileWrite << lineData << std::endl;

        }
      ++k;
    }
  }
}
