package ie.sdn.model;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.UpdateTimestamp;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "vpn")
public class Vpn {

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
    private String customerId;

    @Column(name = "public_ip", nullable = false)
    private String publicIp;

    @Column(name = "private_subnet", nullable = false)
    private String privateSubnet;

    @Column(name = "ike_auth", nullable = false)
    private String ikeAuth;

    @Column(name = "ipsec_enc", nullable = false)
    private String ipsecEnc;

    @Column(name = "dh_group", nullable = false)
    private String dhGroup;

    @Column(name = "ike_life", nullable = false)
    private String ikeLife;

    @Column(name = "ike_secret", nullable = false)
    private String ikeSecret;

    @Column(name = "ike_version", nullable = false)
    private String ikeVersion;

    @Column(name = "ike_al", nullable = false)
    private String ikeAl;

    @Column(name = "ipsec_al", nullable = false)
    private String ipsecAl;

    @Column(name = "ipsec_life", nullable = false)
    private String ipsecLife;

    @Column(name = "ipsec_secret", nullable = false)
    private String ipsecSecret;



    public Vpn() {
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getCustomerId() {
        return customerId;
    }

    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    public String getPublicIp() {
        return publicIp;
    }

    public void setPublicIp(String publicIp) {
        this.publicIp = publicIp;
    }

    public String getPrivateSubnet() {
        return privateSubnet;
    }

    public void setPrivateSubnet(String privateSubnet) {
        this.privateSubnet = privateSubnet;
    }

    public String getIkeAuth() {
        return ikeAuth;
    }

    public void setIkeAuth(String ikeAuth) {
        this.ikeAuth = ikeAuth;
    }

    public String getIpsecEnc() {
        return ipsecEnc;
    }

    public void setIpsecEnc(String ipsecEnc) {
        this.ipsecEnc = ipsecEnc;
    }

    public String getDhGroup() {
        return dhGroup;
    }

    public void setDhGroup(String dhGroup) {
        this.dhGroup = dhGroup;
    }

    public String getIkeLife() {
        return ikeLife;
    }

    public void setIkeLife(String ikeLife) {
        this.ikeLife = ikeLife;
    }

    public String getIkeSecret() {
        return ikeSecret;
    }

    public void setIkeSecret(String ikeSecret) {
        this.ikeSecret = ikeSecret;
    }

    public String getIkeVersion() {
        return ikeVersion;
    }

    public void setIkeVersion(String ikeVersion) {
        this.ikeVersion = ikeVersion;
    }

    public String getIkeAl() {
        return ikeAl;
    }

    public void setIkeAl(String ikeAl) {
        this.ikeAl = ikeAl;
    }

    public String getIpsecAl() {
        return ipsecAl;
    }

    public void setIpsecAl(String ipsecAl) {
        this.ipsecAl = ipsecAl;
    }

    public String getIpsecLife() {
        return ipsecLife;
    }

    public void setIpsecLife(String ipsecLife) {
        this.ipsecLife = ipsecLife;
    }

    public String getIpsecSecret() {
        return ipsecSecret;
    }

    public void setIpsecSecret(String ipsecSecret) {
        this.ipsecSecret = ipsecSecret;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }
}
