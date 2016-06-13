#include <string>
#include <fstream>
#include <sstream>
#include <iostream> 

int main(int argc, char** argv) {
  std::string fileTestData(argv[1]);

  std::ifstream fileData (fileTestData.c_str());

  int z = 0;
  int filtroAeropuerto;
  std::string aeropuerto;

  int opcion;
  std::cout << "¿Qué variable queres obtener?" << std::endl;
  std::cout << "0:  Año" << std::endl;
  std::cout << "1:  Mes" << std::endl;
  std::cout << "2:  Día del mes" << std::endl;
  std::cout << "3:  Día de la semana" << std::endl;
  std::cout << "4:  Hora real de partida" << std::endl;
  std::cout << "5:  Hora programada de partida " << std::endl;
  std::cout << "6:  Hora real de llegada " << std::endl;
  std::cout << "7:  Hora programada de llegada " << std::endl;
  std::cout << "8:  Nombre del aeropuerto " << std::endl;
  std::cout << "9:  Número del vuelo " << std::endl;
  std::cout << "10: Número del avión " << std::endl;
  std::cout << "11: No se qué es esto " << std::endl;
  std::cout << "12: No se qué es esto " << std::endl;
  std::cout << "14: Tiempo de vuelo " << std::endl;
  std::cout << "15: Delay de llegada " << std::endl;
  std::cout << "16: Delay de salida " << std::endl;
  std::cout << "17: Lugar de origen " << std::endl;
  std::cout << "18: Lugar de destino " << std::endl;
  std::cout << "19: Distancia " << std::endl;
  std::cout << "20: TaxiIn " << std::endl;
  std::cout << "21: TaxiOut " << std::endl;
  std::cout << "22: Cancelación " << std::endl;
  std::cout << "23: Redirigido " << std::endl;
  std::cout << "24: Carrier delay " << std::endl;
  std::cout << "25: Weather delay " << std::endl;
  std::cout << "26: NAS delay " << std::endl;
  std::cout << "27: Security delay " << std::endl;
  std::cout << "28: Late Aircraft delay " << std::endl;
  std::cin >> opcion;  
   
  std::cout << "¿Desea filtrar por algún aeropuerto? (1/0)" << std::endl;
  std::cin >> filtroAeropuerto;

  std::ofstream fileWrite ("out.txt");
  std::string lineData;
  getline(fileData, lineData); // Pido primer línea para instanciar todo

  if (filtroAeropuerto) {
    std::cout << "Ingrese el IATA del aeropuerto" << std::endl;
    std::cin >> aeropuerto;

    while (getline (fileData, lineData)) {
      std::istringstream issData(lineData);
      std::istringstream aux(lineData);

      std::string s;
      int k = 1;

      while (getline(aux, s, ',') && k <= 9) {
        if (k == 9) {

          if (aeropuerto == s) {

            int z = 0;
            while (getline(issData, s, ',') && z <= opcion) {
              if (z == opcion)
                fileWrite << s << std::endl;

              ++z;
            }
          }
        }
        ++k;
      }
    }
  } else {

    while (getline (fileData, lineData)) {
      std::istringstream issData(lineData);

      std::string s;
      int z = 0;
      while (getline(issData, s, ',') && z <= opcion) {
        if (z == opcion) {
          fileWrite << s << std::endl;
        }
        ++z;
      }
    }
  }
}
