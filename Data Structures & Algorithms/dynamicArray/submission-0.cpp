
class DynamicArray {
public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        arr = new int[capacity];
        curr_size = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (curr_size == capacity) {
            resize();
        }
        arr[curr_size++] = n; 
    }

    int popback() {
        return arr[--curr_size];
    }

    void resize() {
        capacity = capacity*2;
        int* new_arr = new int[capacity];
        std::copy(arr, arr + curr_size, new_arr);

        delete[] arr;
        arr = new_arr;
    }

    int getSize() {
        return curr_size;
    }

    int getCapacity() {
        return capacity;
    }
private:
    int curr_size;
    int capacity;
    int* arr;
};
