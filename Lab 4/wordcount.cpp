#include <iostream>
#include <sstream>
#include <map>

void map_function(const std::string& line, std::map<std::string, int>& intermediate_result) {
    std::istringstream iss(line);
    std::string word;
    while (iss >> word) {
        intermediate_result[word]++;
    }
}

void reduce_function(const std::map<std::string, int>& intermediate_result) {
    for (const auto& pair : intermediate_result) {
        std::cout << pair.first << "\t" << pair.second << std::endl;
    }
}


int main() {
    std::map<std::string, int> intermediate_result;

    std::stringstream input_data;
    input_data << "tell me why\n";
    input_data << "ain nothing but heartbreak\n";
    input_data << "tell me why\n";

    std::string line;
    while (std::getline(input_data, line)) {
        map_function(line, intermediate_result);
    }

	reduce_function(intermediate_result);

    return 0;
}