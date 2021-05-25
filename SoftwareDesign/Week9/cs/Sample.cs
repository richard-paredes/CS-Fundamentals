using System;
using System.Collections;
using System.Collections.Generic;

class Sample {
    static void Main(string[] args) {
        List<int> numbers = new List<int> {1, 2, 3};

        IEnumerator enumerator = numbers.GetEnumerator();
        while (enumerator.MoveNext()) {
            Console.WriteLine(enumerator.Current);
        }
        Console.WriteLine(enumerator.GetType());
    }
}
