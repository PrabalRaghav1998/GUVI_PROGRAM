import java.io.*;
import java.util.*;
public class matrix
{
  public static void main(String args[])
  {
  Scanner in =new Scanner(System.in);
  int n,i,j;
  n=in.nextInt();
  int a[][]=new int[n][n];
  for (i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      a[i][j]=in.nextInt();
    }
  }
  for (i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      System.out.print(a[i][j]+"  ");
    }
    System.out.println();
  }
  int c=0;
  for (i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      if(a[i][j]==1 && i>0 && i<n-1 && j>0 && j<n-1)
      {
        if(a[i+1][j]==0 && a[i-1][j]==0 && a[i][j+1]==0 && a[i][j-1]==0)
        c+=1;
      }
      if(a[i][j]==1 && i==0 && j==0)
      {
        if(a[i+1][j]==0  && a[i][j+1]==0)
        c+=1;
      }
      if(a[i][j]==1 && i==0 && j>0 &&j<n-1)
      {
        if(a[i+1][j]==0  && a[i][j+1]==0 && a[i][j-1]==0)
        c+=1;
      }
      if(a[i][j]==1 && i==0 && j==n-1)
      {
        if(a[i+1][j]==0 && a[i][j-1]==0)
        c+=1;
      }
      if(a[i][j]==1 && j==0 && i>0 && i<n-1)
      {
        if(a[i+1][j]==0  && a[i][j+1]==0 && a[i-1][j]==0)
        c+=1;
      }
      if(a[i][j]==1 && j==0 && i==n-1)
      {
        if(a[i][j+1]==0 && a[i-1][j]==0)
        c+=1;
      }
      if(a[i][j]==1 && i==n-1 && j>0 && j<n-1)
      {
        if(a[i-1][j]==0  && a[i][j+1]==0 && a[i][j-1]==0)
        c+=1;
      }
      if(a[i][j]==1 && j==n-1 && i==n-1)
      {
        if(a[i][j-1]==0 && a[i-1][j]==0)
        c+=1;
      }
      if(a[i][j]==1 && j==n-1 && i>0 && i<n-1)
      {
        if(a[i-1][j]==0  && a[i][j+1]==0 && a[i][j-1]==0)
        c+=1;
      }
    }
  }

      System.out.println(c);
}
}
