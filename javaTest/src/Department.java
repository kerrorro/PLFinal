/**
 * Created by fahrankamili on 4/8/16.
 */
public class Department {
    private String id;
    private String name;
    private String region_id;

    public Department(String id, String name, String region_id) {
        this.id = id;
        this.name = name;
        this.region_id = region_id;
    }

    public Department(String[] dept){
        this(dept[0], dept[1], dept[2]);
    }

    public String getId() {
        return id;
    }

    public String getRegion_id() {
        return region_id;
    }

    public String getName() {
        return name;
    }

    public String toString(){
        return id + " " + name + " " + region_id;
    }
}
