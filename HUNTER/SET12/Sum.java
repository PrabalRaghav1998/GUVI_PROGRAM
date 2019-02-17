import java.util.*;
public class Sum
{
  public static void main(String args[])
  {
    Scanner in=new Scanner(System.in);
    int n=in.nextInt();
    int a[][]=new int[n][n];
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
      {
        a[i][j]=in.nextInt();
      }
    }
    int s=0;
    for(int i=0;i<n;i++)
    {
        s+=a[i][i];
      }
      System.out.print(s);
    }
  }
