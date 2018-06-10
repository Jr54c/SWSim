
public class Ship {
	private int value;
	private String name;
	private String sclass;
	private int crew;
	public Ship(int v, int c, String n, String s) {
		value = v;
		name = n;
		crew = c;
		sclass = s;
	}
	public int getValue() {
		return value;
	}
	public String getName() {
		return name;
	}
	public String getSclass() {
		return sclass;
	}
	public int getCrew() {
		return crew;
	}
	public String toString() {
		return name+"\n"+sclass;
	}
	
}
