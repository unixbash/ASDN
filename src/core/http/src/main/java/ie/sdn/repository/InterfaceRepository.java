package ie.sdn.repository;

import ie.sdn.model.Interface;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface InterfaceRepository extends JpaRepository<Interface, Long> {
    //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
    Interface findById(String id);
    Interface findByDeviceId(String id);
}
