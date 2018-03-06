package ie.sdn.service;

import ie.sdn.model.User;
import ie.sdn.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

import java.util.List;
import java.util.stream.Stream;

public class UserService {
    @Autowired UserRepository userRepository;

    public Stream<User> stream() {
        return getUsers().stream();
    }

    public List<User> getUsers() {
        return userRepository.findAll();
    }

    public User getUser(String id) {
        User user = userRepository.findById(id);
        if (user == null) {
            throw new UsernameNotFoundException(id);
        }
        return user;
    }
}
