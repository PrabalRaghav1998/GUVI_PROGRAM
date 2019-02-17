import java.util.*;
import java.math.*;
public class Coprime
{
  public static void main(String args[])
  {
    Scanner in=new Scanner(System.in);
    String n=in.next();
    String c=in.next();
    BigInteger a=new BigInteger(n);
    BigInteger b=new BigInteger(c);
    BigInteger g=a.gcd(b);
    int k=g.intValue();
    if(k==1)
    System.out.print("yes");
    else
    System.out.print("no");

  }
}
