import java.io.*;
import java.util.*;
public class balance
{
  public static void main(String args[])
  {
  Scanner in =new Scanner(System.in);
  int i,j,k=0;
  String n=in.next();
  Stack<Character> s=new Stack<Character>();
  for(i=0;i<n.length();i++)
  {
    char ch=n.charAt(i);
    if(ch=='(')
    s.push(ch);
    if(ch==')')
    {
            if(s.isEmpty())
            {
                k=1;
                break;
            }
      s.pop();
        }
    }
  if(k==1 || !s.isEmpty())
  System.out.println("no");
  else
  System.out.println("yes");
}
}
