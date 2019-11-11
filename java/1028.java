import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int C = in.nextInt();
        in.nextLine();
        ArrayList<Stu> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String s = in.nextLine();
            String[] data = s.split(" ");
            arr.add(new Stu(data));
        }
        Comparator<Stu> cmp = Comparator.comparingInt(t -> Integer.parseInt(t.id));
        Comparator<Stu> c2 = Comparator.comparing(t -> t.name);
        Comparator<Stu> c3 = Comparator.comparing(t -> t.grade);
        if (C == 1) {
            arr.sort(cmp);
        } else if (C == 2) {
            arr.sort((t1, t2) -> {
                if (c2.compare(t1, t2) != 0) {
                    return c2.compare(t1, t2);
                }
                // if name equals
                return cmp.compare(t1, t2);
            });
        } else {
            arr.sort((t1, t2) -> {
                if (c3.compare(t1, t2) != 0) {
                    return c3.compare(t1, t2);
                }
                return cmp.compare(t1, t2);
            });
        }
        for (Stu t : arr) {
            System.out.println(t.id + " " + t.name + " " + t.grade);
        }

    }
}

class Stu {
    String id, name, grade;

    public Stu(String[] data) {
        id = data[0];
        name = data[1];
        grade = data[2];
    }

}