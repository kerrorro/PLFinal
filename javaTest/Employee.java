package javaTest;

/**
 * Created by fahrankamili on 4/8/16.
 */
public class Employee {
    private String id;
    private String lastName;
    private String firstName;
    private String userId;
    private String start_date;
    private String comments;
    private String title;
    private String salary;
    private String commision;
    private String dept_id;
    private String manager_id;


    public Employee(String id, String lastName, String firstName, String userId, String start_date, String comments, String title, String salary, String commision, String dept_id, String manager_id) {
        this.id = id;
        this.lastName = lastName;
        this.firstName = firstName;
        this.userId = userId;
        this.start_date = start_date;
        this.comments = comments;
        this.title = title;
        this.salary = salary;
        this.commision = commision;
        this.dept_id = dept_id;
        this.manager_id = manager_id;
    }

    public String getId() {
        return id;
    }

    public String getUserId() {
        return userId;
    }

    public String getLastName() {
        return lastName;
    }


    public String getFirstName() {
        return firstName;
    }

    public String getStart_date() {
        return start_date;
    }

    public String getComments() {
        return comments;
    }

    public String getTitle() {
        return title;
    }

    public String getSalary() {
        return salary;
    }

    public String getCommision() {
        return commision;
    }

    public String getDept_id() {
        return dept_id;
    }

    public String getManagerId() {
        return manager_id;
    }

}
