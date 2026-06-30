public class Type{
    public static void main (String [] args){
        int a=20;
        String b="hello";
        float c = 20.5;
        System.out.println(((Object)a).getClass().getName());
        System.out.println(((Object)b).getClass().getName());
        System.out.println(((Object)c).getClass().getName());
    }
}