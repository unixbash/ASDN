package ie.sdn.repository;

import ie.sdn.model.Service;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ServiceRepository extends JpaRepository<Service, Long> {
    //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
    Service findById(String id);
    List<Service> findByDeviceId(String id);
}
