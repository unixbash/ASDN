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

    @Column(name = "customer_id", nullable = false)
    private String customer_id;

    @Column(name = "net_id", nullable = false, unique = true)
    private String net_id;

    @CreationTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdAt;

    @UpdateTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    private Date updatedAt;

    @Column(name = "public_ip", nullable = false)
    private String public_ip;

    @Column(name = "private_subnet", nullable = false)
    private String private_subnet;

    @Column(name = "ike_auth", nullable = false)
    private String ike_auth;

    @Column(name = "ipsec_enc", nullable = false)
    private String ipsec_enc;

    @Column(name = "dh_group", nullable = false)
    private String dh_group;

    @Column(name = "ike_life", nullable = false)
    private String ike_life;

    @Column(name = "ike_secret", nullable = false)
    private String ike_secret;

    @Column(name = "ike_version", nullable = false)
    private String ike_version;

    @Column(name = "ike_al", nullable = false)
    private String ike_al;

    @Column(name = "ipsec_al", nullable = false)
    private String ipsec_al;

    @Column(name = "ipsec_life", nullable = false)
    private String ipsec_life;

    @Column(name = "ipsec_secret", nullable = false)
    private String ipsec_secret;



    public Vpn() {
    }


    public String getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(String customer_id) {
        this.customer_id = customer_id;
    }

    public String getNet_id() {
        return net_id;
    }

    public void setNet_id(String net_id) {
        this.net_id = net_id;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public String getPublic_ip() {
        return public_ip;
    }

    public void setPublic_ip(String public_ip) {
        this.public_ip = public_ip;
    }

    public String getPrivate_subnet() {
        return private_subnet;
    }

    public void setPrivate_subnet(String private_subnet) {
        this.private_subnet = private_subnet;
    }

    public String getIke_auth() {
        return ike_auth;
    }

    public void setIke_auth(String ike_auth) {
        this.ike_auth = ike_auth;
    }

    public String getIpsec_enc() {
        return ipsec_enc;
    }

    public void setIpsec_enc(String ipsec_enc) {
        this.ipsec_enc = ipsec_enc;
    }

    public String getDh_group() {
        return dh_group;
    }

    public void setDh_group(String dh_group) {
        this.dh_group = dh_group;
    }

    public String getIke_life() {
        return ike_life;
    }

    public void setIke_life(String ike_life) {
        this.ike_life = ike_life;
    }

    public String getIke_secret() {
        return ike_secret;
    }

    public void setIke_secret(String ike_secret) {
        this.ike_secret = ike_secret;
    }

    public String getIke_version() {
        return ike_version;
    }

    public void setIke_version(String ike_version) {
        this.ike_version = ike_version;
    }

    public String getIke_al() {
        return ike_al;
    }

    public void setIke_al(String ike_al) {
        this.ike_al = ike_al;
    }

    public String getIpsec_al() {
        return ipsec_al;
    }

    public void setIpsec_al(String ipsec_al) {
        this.ipsec_al = ipsec_al;
    }

    public String getIpsec_life() {
        return ipsec_life;
    }

    public void setIpsec_life(String ipsec_life) {
        this.ipsec_life = ipsec_life;
    }

    public String getIpsec_secret() {
        return ipsec_secret;
    }

    public void setIpsec_secret(String ipsec_secret) {
        this.ipsec_secret = ipsec_secret;
    }
}
