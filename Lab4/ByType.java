package Lab4;

import java.util.Comparator;

//Is used to sort field Type in ascending order.


	public class ByType implements Comparator<Car> {

		@Override
		public int compare(Car o1, Car o2) {
			return o1.Type.compareToIgnoreCase(o2.Type);
		}
		
}
