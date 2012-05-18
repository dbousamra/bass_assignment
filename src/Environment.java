import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class Environment {
	
	final int DUSK = 74;
	
	int time = 0;
	
	public Environment() { }

	public static void main(String[] args) {
		Environment env = new Environment();
		Bird bird = new Bird();
		
		for (int i = 0; i < 150; i++) {
			if (bird.isDead()) {
				break;
			}
			else {
				env.calculateReserves(bird);
				System.out.println("Reserves = " + bird.reserves);
			}
		}
		System.out.println(bird.points);
	}
	
	private void calculateReserves(Bird bird) {
		
		if (isDay()) {
			if (bird.reserves >= 32) {
				bird.sing();
				System.out.println("Sing");
			}
			else {
				bird.forage();
				System.out.println("Forage");
			}
		}
		else {
			bird.rest();
			System.out.println("Rest");
		}
		bird.calculatePoints();
		
	}

	private void increaseTime() {
		this.time += 1;
	}
	
	private boolean isDay() {
		return time < DUSK;
	}
	

}
