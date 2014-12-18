import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class BinarySearch {

    public static void main(String[] args) {
        ArrayList<Integer> integers = generateRandomList(1000);
        Collections.sort(integers);
        System.out.println(binarySearch(integers, 200));
        System.out.println(binarySearch(integers, 10000));
        System.out.println(binarySearch(integers, 100));

    }

    private static boolean binarySearch(final List<Integer> list, int value) {
        int mid = list.size() / 2;
        if(value == list.get(mid))
            return true;
        if (list.size() == 1)
            return value == list.get(0);
        if (value < list.get(mid))
            return binarySearch(list.subList(0, mid), value);
        else if (value > list.get(mid))
            return binarySearch(list.subList(mid, list.size()), value);
        return false;
    }

    private static ArrayList<Integer> generateRandomList(int size) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        Random random = new Random();
        for (int i = 0; i < size; i++)
            list.add(random.nextInt(1000));
        return list;
    }
}
