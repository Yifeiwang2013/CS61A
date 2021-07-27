//Written by: Churuo Zhang
//Assignment: Lab 11 - Page 276 - 7.1
//Class:      CS 113
//Date:       July 23, 2021
//Description: This program reads student scores, get the best score and then assigns grade based on the given scheme

import java.util.Scanner;
public class HelloWorld{

     public static void main(String []args){
        System.out.println ("This program reads student scores, get the best score and then assigns grade based on the given scheme");
		Scanner input = new Scanner(System.in); 

		//get input from user
		System.out.println ("Enter the number of students: ");
		int n = input.nextInt();
		System.out.println ("Enter " + n + " scores: ");

		int [] values = new int[n];
		int temp;

		for (int i=0; i<9; i++ )
		{
			for (int k=0;k<9-i;k++)
			{
				temp = values[k];
				values[k] = values[k+1];
				values[k+1] = temp;
				
			}
		}
			
		for (int i = 0; i<10; i++)
		{
			System.out.println(values[i]);
		}
		
     }
}



