import java.io.*;
import java.util.*;
public class type
{
  public static void main(String args[])
  {
  Scanner in =new Scanner(System.in);
  int n,i,j;
  n=in.nextInt();
  if((n>=-2147483648)&&(n<=2147483647))
  System.out.print("INT");
  else
  System.out.print("LONG");
}
}
