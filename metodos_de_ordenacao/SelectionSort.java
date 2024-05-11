import java.util.Arrays;

public class SelectionSort {

    static int[] selectionSort(int[] arr) {
        int menor, aux;


        for (int i = 0; i < arr.length - 1; i++) {
            menor = i;

            // j será utilizado para procurar o elemento menor de todos
            for (int j = i + 1; j < arr.length; j++) {

                // quero encontrar um elemento menor que o menor que ja tenho
                if (arr[j] < arr[menor]) { 
                    menor = j; // encontrou um elemento menor ainda                
                }
            }

            if (i != menor) {
                aux = arr[i];
                arr[i] = arr[menor];
                arr[menor] = aux;
            }
            
        }

        return arr;
    }

    public static void main(String[] args) {

        int[] arr = {18, 6, 5, 1, 8, 10, 11, 3, 9, 12, 4, 2};

        int[] v = selectionSort(arr);

        System.out.println(Arrays.toString(v));
        
    }
}
