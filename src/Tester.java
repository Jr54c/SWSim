
public class Tester {

	public static void main(String[] args) {
		Ship s1 = new Ship(44, 1000, "Striker", "ISD I");
		Deck deck = new Deck();
		deck.addShip(s1);
		deck.addShip(new Ship(44, 1000, "Relentless", "ISD II"));
		System.out.println(deck);
	}

}
