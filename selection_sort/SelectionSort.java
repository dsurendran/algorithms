import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SelectionSort {

    public static void main(String[] args) {
        Random random = new Random();
        List<Integer> inputList = new ArrayList<>();
        for(int i = 0 ;i< 500;i++)
            inputList.add(random.nextInt(1000));
        Integer[] sortedArray = selectionSort((Integer[])inputList.toArray(new Integer[inputList.size()]));
        for(Integer val :sortedArray)
            System.out.println(val);
    }

    public static Integer[] selectionSort(Integer[] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = i; j < array.length; j++) {
                if (array[i] > array[j]) {
                    Integer temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
        return array;
    }
}
