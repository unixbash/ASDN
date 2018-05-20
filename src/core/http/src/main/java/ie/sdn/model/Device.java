package ie.sdn.model;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.UpdateTimestamp;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "device")
public class Device {

    @Id
    @GeneratedValue(generator = "uuid2")
    @GenericGenerator(name = "uuid2", strategy = "uuid2")
    private String id;

    @CreationTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdAt;

    @UpdateTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    private Date updatedAt;

    @Column(name = "customer_id", nullable = false)
    private String customer_id;

    @Column(name = "hostname", nullable = false)
    private String hostname;

    @Column(name = "address", nullable = false, unique = true)
    private String address;

    @Column(name = "vendor")
    private String vendor;

    @Column(name = "status")
    private String status;

    @Column(name = "config")
    private String config;

    @Column(name = "configOld")
    private String configOld;

    @Column(name = "latestos")
    private String latestos;

    public Device() {
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public String getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(String customer_id) {
        this.customer_id = customer_id;
    }

    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getConfig() {
        return config;
    }

    public void setConfig(String config) {
        this.config = config;
    }

    public String getConfigOld() {
        return configOld;
    }

    public void setConfigOld(String configOld) {
        this.configOld = configOld;
    }


    public String getLatestos() {
        return latestos;
    }

    public void setLatestos(String latestos) {
        this.latestos = latestos;
    }
}
