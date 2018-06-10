import java.util.ArrayList;
public class Deck {
 private ArrayList<Ship> deck;
 private int totalPoints; 
 
 public Deck(ArrayList<Ship> d) {
	 deck = d;
	 totalPoints = getPoints();
 }
 public Deck() {
	 deck = new ArrayList<Ship>();
	 totalPoints = 0;
 }
 public void addShip(Ship s) {
	 deck.add(s);
 }
 public int getPoints() {
	 int sum = 0;
	 for(int i = 0; i<deck.size(); i++) {
		 sum+=deck.get(i).getValue();
	 }
	 return sum;
 }
 public String toString() {
	 String str = "";
	 for(int i = 0; i < deck.size(); i++) {
		 str+=deck.get(i).toString()+"\n";
	 }
	 return str+getPoints();
 }
}
