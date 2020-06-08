package Lab4;

import java.util.Comparator;


//Is used to sort field Type in descending order.


public class ByAmount implements Comparator<Car> {

	@Override
	public int compare(Car o1, Car o2) {
		return o2.AmountOfWheels - o1.AmountOfWheels;
	}
}
