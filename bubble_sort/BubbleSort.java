import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class BubbleSort {

    public static void main(String[] args) {

        Random random = new Random();
        List<Integer> inputList = new ArrayList<>();
        for (int i = 0; i < 5; i++)
            inputList.add(random.nextInt());
        Integer[] sortedArray = bubbleSort((Integer[]) inputList.toArray(new Integer[inputList.size()]));
        for (Integer val : sortedArray)
            System.out.println(val);
    }

    private static Integer[] bubbleSort(Integer[] inp) {
        for (int i = 0; i < inp.length; i++) {
            for (int j = i + 1; j < inp.length; j++) {
                if (inp[i] > inp[j]) {
                    int temp = inp[i];
                    inp[i] = inp[j];
                    inp[j] = temp;
                }

            }
        }
        return inp;
    }
}
