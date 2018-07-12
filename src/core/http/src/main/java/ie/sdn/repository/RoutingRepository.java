package ie.sdn.repository;

import ie.sdn.model.Routing;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RoutingRepository extends JpaRepository<Routing, Long> {
    //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
    Routing findById(String id);
    List<Routing> findByDeviceId(String id);
}
