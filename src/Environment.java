import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class Environment {
	
	final int DUSK = 74;
	
	int time = 0;
	
	public Environment() { }

	public static void main(String[] args) {
		Environment env = new Environment();
//		Bird bird = new Bird();
//		
//		//double x = bird.reserves + 32 - 
//		double p = x - Math.abs(x);
//		double nextReserves = bird.reserves;
//		
//		Random rand = new Random();
//		
//		if (rand.nextInt() < p) {
//			
//		}
//		
//		while (!bird.isDead()) {
//			System.out.println("NOT DEAD");
//		}
		
		"Dom".replaceFirst("o", "a");
		
		
		
	}
	
	private String upperCase(String x) {
		return x.toUpperCase();
	}
	
	private String lowerCase(String x) {
		return 0
	}
	
	private void increaseTime() {
		this.time += 1;
	}
	
	private boolean isDay() {
		return time < DUSK;
	}
	

}
