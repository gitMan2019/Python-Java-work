public class SpaceNeedleProject
{

   public static void main(String[] args)
   {
		int SIZE = 5;
	   
		// First four rows of the needle
		for ( int i = 1; i <= SIZE; i++ )
		{
			for ( int j = 1; j <= ( SIZE * 3 ); j++ )
				System.out.print(" ");

			System.out.println("||");
		}
   
		// Top part of top section
		for ( int row = 0; row < SIZE; row++ )
		{    
         // Number of spaces is set equal to three times the size given above,
         // and then subtracted from that is 3 times the current row plus one.
			for ( int j = 0; j < ( ( 3 * SIZE) - ( 3 * ( row + 1 ) ) ); j++ ) 
				System.out.print(" ");
			
			System.out.print("__");
			System.out.print("/");
			
			for ( int i = 0; i < 3 * row; i++ )
				System.out.print(":");
			
			System.out.print("||");
			
			for ( int i = 0; i < 3 * row; i++ )
				System.out.print(":");
			
			System.out.print("\\");
			
			System.out.print("__");
			
			System.out.println();
		}
      
		// Middle of top section
		System.out.print("|");
      
		for ( int n = 0; n < ( SIZE* 6 ); n++ )
			System.out.print("\"");
         
		System.out.print("|");
        
		// Lower part of top section
		for ( int row = 0; row < SIZE; row++ )
		{
			System.out.println();
      
			// Prints out necessary number of spaces at the start of each row,
         // namely, twice the number of the current row.
			for ( int k = 0; k < ( row * 2 ); k++ )
				System.out.print(" ");
            
			System.out.print("\\_/");
         
			for ( int n = 0; n < ( ( 2 * SIZE ) + ( SIZE - 2 ) ) - ( row * 2 ); n++ )
				System.out.print("\\/");
         
			System.out.print("\\_/");      
		}
      
		// Short stem connector section
		for ( int row = 1; row <= SIZE; row++ )
		{
			System.out.println();
      
			for ( int j = 1; j <= ( SIZE * 3 ); j++ )
				System.out.print(" ");

			System.out.print("||");
		}
      
		// Longer, wider connector section
		for ( int row = 0; row < ( Math.pow(SIZE, 2) ); row++ )
		{
			System.out.println();
         
			// Prints out number of spaces that is one added to twice the size
			for ( int i = 0; i < ( ( SIZE * 2 ) + 1 ); i++ )
				System.out.print(" ");
            
			System.out.print("|");

			for ( int j = 0; j < ( SIZE - 2 ); j++ )
				System.out.print("%");
			
			System.out.print("|");
			System.out.print("|");
			
			for ( int j = 0; j < ( SIZE - 2 ); j++ )
				System.out.print("%");
			
			System.out.print("|");
		}
      
		// Next four rows after the longer stem section--
      // same code as top part of top section.      
		for ( int row = 0; row < SIZE; row++ )
		{    
			System.out.println();
      
			for ( int j = 0; j < ( ( 3 * SIZE) - ( 3 * ( row + 1 ) ) ); j++ ) 
				System.out.print(" ");
			
			System.out.print("__");
			System.out.print("/");
			
			for ( int i = 0; i < 3 * row; i++ )
				System.out.print(":");
			
			System.out.print("||");
			
			for ( int i = 0; i < 3 * row; i++ )
				System.out.print(":");
			
			System.out.print("\\");
			
			System.out.print("__");		
		}
      
		// Very last row
		System.out.println("");
      
		System.out.print("|");
      
		for ( int n = 0; n < ( SIZE * 6 ); n++ )
			System.out.print("\"");
         
		System.out.print("|");
   }
   
}