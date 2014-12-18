using System;
using System.Collections.Generic;

namespace Algos
{
    class BinarySearch
    {
        public static void Main(string[] args)
        {
            List<int> list = generateRandomList(500);
            list.Sort();
            Console.WriteLine(binarySearch(list, 100));
            Console.WriteLine(binarySearch(list, 10000));
            Console.WriteLine(binarySearch(list, 500));
            Console.ReadLine();
        }

        private static Boolean binarySearch(List<int> list, int value)
        {
            if (list.Count == 1)
                return value == list[0];
            int mid = list.Count / 2;
            if (value == list[mid])
                return true;
            else if (value < list[mid])
                return binarySearch(list.GetRange(0, mid), value);
            else if (value > list[mid])
                return binarySearch(list.GetRange(mid, list.Count / 2), value);
            return false;
        }

        private static List<int> generateRandomList(int size)
        {
            List<int> list = new List<int>();
            Random rand = new Random();
            for (int i = 0; i < size; i++)
                list.Add(rand.Next(1000));            
            return list;
        }
    }
}
