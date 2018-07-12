package ie.sdn.model;

public class Node {
    String id;
    String label;
    String shape;
    String image;

    public Node(String id, String label, String shape, String image) {
        this.id = id;
        this.label = label;
        this.shape = shape;
        this.image = image;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
}
