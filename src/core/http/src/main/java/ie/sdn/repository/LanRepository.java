package ie.sdn.repository;

import ie.sdn.model.Lan;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LanRepository extends JpaRepository<Lan, Long> {
    //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
    Lan findById(String id);
    List<Lan> findByDeviceId(String id);
}
