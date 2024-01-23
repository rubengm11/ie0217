CXX = g++
CXXFLAGS = -std=c++11 -Wall

TARGET_correo = correo/correo
TARGET_matriz = matriz/matriz

SRC_correo = ./correo/funciones.cpp ./correo/main.cpp
SRC_matriz = ./matriz/funciones.cpp ./matriz/main.cpp

ifeq ($(OS),Windows_NT)
    RM = del /Q
    TARGET_EXTENSION = .exe
else
    RM = rm -f
    TARGET_EXTENSION =
endif

correo: build_correo run_correo

build_correo: $(TARGET_correo)

$(TARGET_correo): $(SRC_correo)
	$(CXX) $(CXXFLAGS) -o $(TARGET_correo) $(SRC_correo)

run_correo:
	./$(TARGET_correo)

clean_correo:
	$(RM) $(TARGET_correo)$(TARGET_EXTENSION)


matriz: build_matriz run_matriz

build_matriz: $(TARGET_matriz)

$(TARGET_matriz): $(SRC_matriz)
	$(CXX) $(CXXFLAGS) -o $(TARGET_matriz) $(SRC_matriz)

run_matriz:
	./$(TARGET_matriz)

clean_matriz:
	$(RM) $(TARGET_matriz)$(TARGET_EXTENSION)

