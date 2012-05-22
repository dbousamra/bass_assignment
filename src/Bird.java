import java.util.Random;


public class Bird {

	double reserves = 0;
	int points = 0;
	boolean hasMate = false;
	
	public Bird() {
		
	}
	
	public void sing() {
		double foodUsed = 12 * (0.002 * this.reserves) + getB();
		this.reserves -= foodUsed;
		pairWithMate();
	}
	
	public void forage() {
		double foodFound = 8 + (0.007 * this.reserves) + getB();
		this.reserves += foodFound;
		findFood();
	}
	
	public void rest() {
		this.reserves += -3.6;
	}
	
	public boolean isDead() {
		return this.reserves < 0;
	}
	
	private void pairWithMate() {
		//0.004 % chance to mate
		if (new Random().nextInt(1000) > 4) {
			this.hasMate = true;
		}
	}
	
	private void findFood() {
		if( new Random().nextInt(100) < 60) {
			this.reserves += 32;
		}
	}
	
	public void calculatePoints() {
		if (hasMate && !isDead()) {
			points += 2;
		}
		else if (!isDead()) {
			points += 1;
		}
		else if (isDead()) {
			points += 0;
		}
	}

	private double getB() {
		int randomNumber = new Random().nextInt(100);
		if (randomNumber < 50) {
			return -6.4;
		}
		else if (randomNumber >= 50 && randomNumber < 75) {
			return 0;
		}
		else {
			return 6.4;
		}
	}
}
