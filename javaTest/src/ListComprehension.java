import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;


public class ListComprehension {
    public static void run(Employee[] empArray, Department[] deptArray) throws IOException {
        System.out.println("Creating arraylists");
        ArrayList<Employee> emp = new ArrayList<>();
        ArrayList<Department> dept = new ArrayList<>();
        for (Employee e : empArray){
            emp.add(e);
        }
        for (Department d : deptArray){
            dept.add(d);
        }

        //ArrayList<Employee> emp = new ArrayList<Employee>(Arrays.asList(emp));
        //ArrayList<Department> dept = new ArrayList<Department>(Arrays.asList(dept));
        /*ArrayList<Employee> emp = new ArrayList<>();
        ArrayList<Department> dept = new ArrayList<>();

        String path = System.getProperty("user.dir") + "/";

        File file = new File(path + "employees.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;
        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> empList = Arrays.asList(a.split(","));
            for (int i = 0;i<empList.size();i++){
                empList.set(i,empList.get(i).trim());
            }
            empList.get(0);
            Employee e = new Employee(empList.get(0),empList.get(1),empList.get(2),empList.get(3),empList.get(4),empList.get(5),empList.get(6),empList.get(7),empList.get(8),empList.get(9),empList.get(10));
            emp.add(e);
        }


        br = new BufferedReader(new FileReader(path + "departments.txt"));
        while ((line = br.readLine()) != null){
            String a = line.substring(1, line.length() - 2);
            List<String> deptList = Arrays.asList(a.split(","));
            Department d = new Department(deptList.get(0),deptList.get(1),deptList.get(2));
            dept.add(d);
        }
*/
        System.out.println("\nSELECT first_name, last_name, manager_id, salary FROM emp ORDER BY manager_id, salary");
               emp.stream()
                       .collect(Collectors.groupingBy(Employee::getManagerId))
                       .entrySet()
                       .stream()
                       .map(kv -> kv.getValue())
                       .forEach((l) -> {
                           l.stream()
                                   .sorted((e1, e2) -> e1.getSalary()
                                           .compareTo(e2.getSalary()))
                                   .forEach(e -> {
                                       String toPrint = e.getFirstName() + " " + e.getLastName() + " " + e.getManagerId() + " " + e.getSalary();
                                       System.out.println(toPrint);
                                   });
                       });

        System.out.println("\nSELECT first_name,last_name,title,salary FROM emp WHERE salary > 1500 and dept_id > 40");
        emp.stream()
                .filter(p -> (Integer.parseInt(p.getSalary()) > 1500) && (Integer.parseInt(p.getDept_id()) > 40))
                .forEach(e -> {
                    String toPrint = e.getFirstName() + " " + e.getLastName() + " " + e.getDept_id() + " " + e.getSalary();
                    System.out.println(toPrint);
                });

        System.out.println("\nSELECT dept_id, avg(salary) FROM emp GROUP BY dept_id");
        emp.stream()
                .collect(Collectors.groupingBy(Employee::getDept_id))
                .entrySet()
                .stream()
                .map(kv -> kv.getValue())
                .forEach(empList -> {
                    double avg = empList.stream().mapToInt(e -> Integer.parseInt(e.getSalary())).average().getAsDouble();
                    String dept_id = empList.get(0).getDept_id();
                    System.out.println(dept_id + " " + avg);
                });

        System.out.println("\nSELECT * FROM dept");
        dept.stream().forEach(d -> System.out.println(d));


        System.out.println("\nSELECT first_name, last_name, commission FROM emp ORDER BY commission DESC");
        emp.stream()
                .sorted((e1, e2) -> e2.getCommision().compareTo(e1.getCommision()))
                .forEach(e->System.out.println(e.getFirstName() + " " + e.getLastName() + " " + e.getCommision()));

    }
}
