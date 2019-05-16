public class StickFigures
{
   static int SIZE = 3;
   
   public static void main(String[] args)
   {
      step();
      base();
   }
   
   public static void step()
   {
        
      for ( int row = SIZE; row > 0; row-- )
      {
         
         // number of spaces in first line of a step
         for ( int space = 0; space < (5 * row) - 3; space++ )
            System.out.print(" ");
         
         // one lower case O per iteration
         System.out.print("o");
         
         // two spaces follow afterwards
         System.out.print("  ");
         
         // six asterisks after the two spaces
         for ( int asterisk = 0; asterisk < 6; asterisk++ )
            System.out.print("*");
            
         // prints out number of spaces between last and second to last asterisk in first line of each step
         for ( int space = 0; space < (5 * SIZE) - (5 * row); space++ )
            System.out.print(" ");
            
         // asterisk in last column
         System.out.print("*");
         
         // new line   
         System.out.println();
         
         // number of spaces for middle body
         for ( int space = 0; space < (5 * row) - 4; space++ )
            System.out.print(" ");
            
         // middle body
         System.out.print("/|\\");
         
         // space and one asterisk after middle body
         System.out.print(" *");
         
         // number of spaces after previous asterisk and asterisk in last column
         for ( int space = 0; space < (5 * SIZE) - (5 * (row - 1)); space++ )
            System.out.print(" ");
            
         // asterisk in last column
         System.out.print("*");
                        
         // new line
         System.out.println();
            
         // number of spaces for lower body
         for ( int space = 0; space < (5 * row) - 4; space++ )
            System.out.print(" ");
              
         // lower body
         System.out.print("/ \\");
          
         // space and asterisk after lower body
         System.out.print(" *");
          
         // number of spaces after previous asterisk and asterisk in last column 
         for ( int space = 0; space < (5 * SIZE) - (5 * (row - 1)); space++ )
            System.out.print(" ");
               
         // asterisk in last column
         System.out.print("*");
                         
         // new line for first line in the next step
         System.out.println();
      }
      
   }
   
   public static void base()
   {
      // prints out necessary number of asterisks in base,
      // which is dependent upon SIZE
      for ( int space = 0; space < ((SIZE * 6) + 2) + (-SIZE + 5); space++ )
         System.out.print("*");
   }
   
}