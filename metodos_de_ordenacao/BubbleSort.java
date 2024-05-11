import java.util.Arrays;

class BubbleSort {

    static int[] bubbleSort(int[] arr, int len) {
        int continua, fim = len;
        int aux;

        do {
            continua = 0;

            for (int i = 0; i < fim - 1; i++) {

                /*
                 compara o elemento da esquerda com o da direita
                 se for maior, troca de lugar
                 faz isso até que o elemento comparado seja rolado para a maior posição à direita 
                 */

                if (arr[i] > arr[i + 1]) {
                    aux = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = aux;

                    continua = i;
                }
            }

            fim--;

        } while (continua != 0);

        return arr;
    }
    public static void main(String[] args) {
        int[] arr = {20, 5, 1, 8, 10, 11, 3, 9, 12, 4, 2};

        int[] v = bubbleSort(arr, arr.length);

        System.out.println(Arrays.toString(v));
    }
    
}