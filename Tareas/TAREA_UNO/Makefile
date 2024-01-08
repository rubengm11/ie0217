CXX = g++
CXXFLAGS = -std=c++11 -Wall
TARGET = adivina.x
SRC = funciones.cpp main.cpp

all: build run

build: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

run:
	./$(TARGET)

clean:
	rm -f $(TARGET)
