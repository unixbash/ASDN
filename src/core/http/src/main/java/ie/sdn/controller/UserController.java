package ie.sdn.controller;

import ie.sdn.dto.UserDTO;
import ie.sdn.model.User;
import ie.sdn.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/user")
public class UserController {

    @Autowired
    UserRepository userRepository;

    @GetMapping(value = "/{id}")
    @ResponseBody
    public UserDTO getUser(@PathVariable String id) {
        User user = userRepository.findById(id);
        UserDTO userDTO = new UserDTO();
        userDTO.setId(user.getId());
        userDTO.setName(user.getName());
        return userDTO;
    }

    @PostMapping()
    @ResponseBody
    public UserDTO createUser(@RequestBody UserDTO userToCreate) {

        User user = new User();
        user.setName(userToCreate.getName());
        user = userRepository.save(user);
        userToCreate.setId(user.getId());
        return userToCreate;
    }

    @PutMapping(value = "/{id}")
    @ResponseBody
    public UserDTO updateUserToken(@PathVariable String id, @RequestBody UserDTO userToUpdate) {
        User user = userRepository.findById(id);
        //take on what was passed in and update what you wanted in the DTO
        userRepository.save(user);
        return null;
    }

    @DeleteMapping(value = "/{id}")
    @ResponseBody
    public UserDTO deleteUser(@PathVariable String id) {
        User user = userRepository.findById(id);
        //update the flag as delete or outright delte with .delete(user)
        userRepository.save(user);
        return null;
    }

}
