package ie.sdn.enums;

public enum TokenStatus {
    ACTIVE("ACTIVE"),
    REDACTED("REDACTED"),
    UPGRADED("UPGRADED"),
    INACTIVE("INACTIVE");

    private String status;

    TokenStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return status;
    }
}
