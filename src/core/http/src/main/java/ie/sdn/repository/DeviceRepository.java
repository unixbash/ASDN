package ie.sdn.repository;

import ie.sdn.model.Device;
import ie.sdn.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DeviceRepository extends JpaRepository<Device, Long> {
    //@Query("SELECT i FROM Submission i WHERE i.partyId=?1 AND i.status = 'PENDING'")
    Device findById(String id);
    List<Device> findAllByCustomerId(String id);
}