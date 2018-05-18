package ie.sdn.controller;

import ie.sdn.dto.UserDTO;
import ie.sdn.dto.UserTokenDTO;
import ie.sdn.enums.TokenStatus;
import ie.sdn.model.User;
import ie.sdn.model.UserToken;
import ie.sdn.repository.UserRepository;
//import ie.sdn.service.EmailService;
import ie.sdn.repository.UserTokenRepository;
import ie.sdn.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;


@Controller
@RequestMapping("/user")
public class UserController {

    @Autowired
    UserRepository userRepository;
    @Autowired
    UserTokenRepository userTokenRepository;
    @Autowired
    PasswordEncoder passwordEncoder;
    @Autowired
    UserService userService;


    @GetMapping(value = "/login")
    @ResponseBody
    public UserTokenDTO loginUser(Authentication auth) {
        if (!auth.getPrincipal().equals("")) {
            String email = auth.getName();
            User user = userRepository.findByEmail(email);

            //Generate a token and save it on the DB, give that token back to the user
            String token = UUID.randomUUID().toString();
            UserToken userToken = new UserToken();
            userToken.setToken(token);
            userToken.setUserId(user.getId());

            //Invalidate any token currently there
            UserToken currentToken = userTokenRepository.findFirstByUserIdOrderByCreatedAtDesc(user.getId());
            if(currentToken != null){
                currentToken.setStatus(TokenStatus.INACTIVE.toString());
                userTokenRepository.save(currentToken);
            }
            //Save the new token
            userToken = userTokenRepository.save(userToken);

            return new UserTokenDTO(userToken);
        } else {
            return null;
        }

    }

    @GetMapping(value = "/logout")
    @ResponseBody
    public UserTokenDTO logoutUser(Authentication auth) {
        String email = auth.getName();
        User user = userRepository.findByEmail(email);

        //Invalidate any token currently there
        UserToken currentToken = userTokenRepository.findFirstByUserIdOrderByCreatedAtDesc(user.getId());
        if(currentToken != null){
            currentToken.setStatus(TokenStatus.INACTIVE.toString());
            userTokenRepository.save(currentToken);
            return new UserTokenDTO(currentToken);
        }
        return null;
    }

    @GetMapping(value = "/{id}")
    @ResponseBody
    public UserDTO getUser(@PathVariable String id, Authentication auth) {
        final User account = userRepository.findByEmail(auth.getName());
        if (account.getId().equals(id)) {
            User user = userRepository.findById(id);
            UserDTO userDTO = new UserDTO();
            userDTO.setId(user.getId());
            userDTO.setName(user.getName());
            return userDTO;
        } else if ("ADMIN".equals(account.getRole())) {
             User user = userService.getUsers().stream()
                    .filter(currentId -> currentId.equals(id))
                    .findAny().orElse(null);

             UserDTO userDTO = new UserDTO();
             userDTO.setId(user.getId());
             userDTO.setName(user.getName());
             return userDTO;
        } else {
            return null;
        }
    }

    @PostMapping()
    @ResponseBody
    public UserDTO createUser(@RequestBody UserDTO userToCreate) {

        User user = new User();
        user.setName(userToCreate.getName());
        //Send confirmation email to the new user
        user.setEmail(userToCreate.getEmail());
        //emailService.sendRegEmail(userToCreate.getEmail());

        user.setPwd(passwordEncoder.encode(userToCreate.getPwd()));
        user.setRole("USER");
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
        userRepository.delete(user);
        return null;
    }
}
