//Hey, I Already Did That!

import java.util.Arrays; 
import java.util.List; 
import java.util.ArrayList;
import java.util.Collections;

public class Solution2b {

public static int solution(String n, int b){

	List<String> allDerivedMinionId = new ArrayList<String>();
	String derivedMinionId = "";
	int j = 0;
	int cycle;

	do{

		if(derivedMinionId != "") {
			allDerivedMinionId.add(derivedMinionId);
			n = derivedMinionId;
		}

		String[] stringArrayOfMinionId = n.split("");

		Integer [] intArrayOfMinionId = new Integer[stringArrayOfMinionId.length];
		for(int i = 0; i < stringArrayOfMinionId.length; i++) {
			intArrayOfMinionId[i] = Integer.parseInt(stringArrayOfMinionId[i]);
		}

		Arrays.sort(intArrayOfMinionId);
		String ascendStringOfMinionId = String.join("", Arrays.toString(intArrayOfMinionId).replaceAll("\\[|\\]|,|\\s", ""));
	     
		Arrays.sort(intArrayOfMinionId, Collections.reverseOrder());
		String descendStringOfMinionId = String.join("", Arrays.toString(intArrayOfMinionId).replaceAll("\\[|\\]|,|\\s", ""));

		int x = Integer.parseInt(descendStringOfMinionId, b);
		int y = Integer.parseInt(ascendStringOfMinionId, b);

		derivedMinionId = Integer.toString(x-y,b);

		//if derivedMinionId length less than length of n append zero
		if(derivedMinionId.length() < n.length()) {
			int diff = n.length() - derivedMinionId.length();
			StringBuilder sb = new StringBuilder(derivedMinionId);
			for(int k = 0; k < diff; k++) {
			    sb.insert(0, "0");
			    derivedMinionId = sb.toString();
			}
		}

		j++;

	} while(!allDerivedMinionId.contains(derivedMinionId));

	cycle = allDerivedMinionId.size() - allDerivedMinionId.indexOf(derivedMinionId);

	return cycle;
}

public static void main(String[] args){
	int x = Solution.solution("210022", 3);
	System.out.println("Final: " + x);
	// int x = Solution.solution("1211", 10);
	// System.out.println("Final: " + x);
}

}