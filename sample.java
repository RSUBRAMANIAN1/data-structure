public class sample {
    int [] array=null;
    int size ;
    int count;

    public sample ()
    {array = new int[1];
        size=1;
        count=0;
    }

    public void add(int data)
    {
     if(count==size){
         addcapacity();
     }
     array[count]=data;
     count++;

    }
    public void addcapacity()
    {

    }


}