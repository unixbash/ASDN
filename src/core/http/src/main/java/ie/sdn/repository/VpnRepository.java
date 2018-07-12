package ie.sdn.repository;

import ie.sdn.model.Vpn;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface VpnRepository extends JpaRepository<Vpn, Long>{
        //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
        Vpn findByCustomerId(String id);
}
