import java.util.*;
public class Lru
{
  public static void main(String args[])
  {
    Scanner in=new Scanner(System.in);
    int n=in.nextInt();
    int c=in.nextInt();
    Queue<Integer> q=new LinkedList<>();
    for(int i=0;i<n;i++)
    {
      int x=in.nextInt();
      if(q.size()<c)
      {
        q.add(x);
      }
      else{
      q.poll();
      q.add(x);
    }}
    while(!q.isEmpty())
    System.out.print(q.poll()+" ");
  }
}
