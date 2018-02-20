package ie.sdn.service;

import ie.sdn.model.User;
import ie.sdn.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;
import java.util.stream.Stream;

public class UserService {
    public Stream<User> stream() {
        return getUsers().stream();
    }

    @Autowired UserRepository userRepository;

    public List<User> getUsers() {
        return userRepository.findAll();
    }

    public User getUser(String id) {
        return userRepository.findById(id);
    }
}
