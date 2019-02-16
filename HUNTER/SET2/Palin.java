import java.io.*;
import java.util.*;
public class Palin
{
  public static void main(String args[])
  {
    Scanner in=new Scanner(System.in);
    String n,m;
    n=in.next();
    m=n;
    Stack<Character> s=new Stack<>();
    for(int i=0;i<n.length();i++)
    {
      char ch=n.charAt(i);
      s.push(ch);
    }
    int i=0,k=0;
    while(!s.isEmpty() && i<n.length())
    {
      if(s.pop()!=n.charAt(i))
      {
        k=1;
      break;
    }
    else
    i++;
  }
  if(k==0)
  System.out.print("YES");
  else
  System.out.print("NO");
  }
}
