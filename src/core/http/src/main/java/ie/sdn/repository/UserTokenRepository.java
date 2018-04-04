package ie.sdn.repository;

import ie.sdn.model.UserToken;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface UserTokenRepository extends JpaRepository<UserToken, Long> {
    UserToken findById(String id);

    UserToken findFirstByUserIdOrderByCreatedAtDesc(String userId);
}
