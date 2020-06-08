package Lab4;

import java.util.Arrays;

public class Lab4 {

	public static void main(String[] args) {
		Car Car1 = new Car ("Легковий", 1500, 4, "жовтогарячий", 5);
		Car Car2 = new Car ("Фура", 20000, 8, "зелений", 3);
		Car Car3 = new Car ("Трицикл", 2500, 3, "жовтий", 4);
		Car Array[] = {Car1, Car2, Car3};
		System.out.println("\nСортування машин за типом у алфавітному порядку (у порядку зростання):");
		Arrays.sort(Array, new ByType());
		for (int i = 0; i < Array.length; i++) {
			System.out.println(Array[i].Type);
		}
		System.out.println("\nСортування машин за кількістю колес у спадаючому порядку");
		Arrays.sort(Array, new ByAmount());
		for (int i = 0; i < Array.length; i++) {
			System.out.println(Array[i].AmountOfWheels);
		}
	}
}
