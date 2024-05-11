import java.util.Arrays;

public class InsertionSort {

    static int[] insertionSort(int[] arr) {
        int atual, j;

        for (int i = 1; i < arr.length; i++) {
            j = i - 1;
            atual = arr[i];

            while (j >= 0 && atual < arr[j]) {
                arr[j + 1] = arr[j]; 
                j--;
            }

            arr[j + 1] = atual;
            
        }

        return arr;
    }

    public static void main(String[] args) {

        int[] arr = {15, 5, 1, 8, 10, 3, 9, 12, 4, 2};

        int[] v = insertionSort(arr);

        System.out.println(Arrays.toString(v));
        
    }
}
