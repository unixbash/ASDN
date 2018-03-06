package ie.sdn.security;

import ie.sdn.controller.UserController;
import ie.sdn.dto.UserDTO;
import ie.sdn.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationProvider;

import java.util.ArrayList;
import java.util.List;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;

public class AuthProvider  implements AuthenticationProvider{

    public AuthProvider() {
        super();
    }
    @Autowired
    UserRepository userRepository;
    UserController userController;
    PasswordEncoder passwordEncoder;

    // API
    /*Check username and password against the ones stored in the DB*/
    @Override
    public Authentication authenticate(final Authentication authentication) throws AuthenticationException {
        //Get request details
        final String userEmail = authentication.getName();
        final String userPassword = passwordEncoder.encode(authentication.getCredentials().toString());

        //get user from db
        ie.sdn.model.User user = userRepository.findByEmail(userEmail);
        //validate password is ok --> hash what comes in and match against hash password stored
        //If validated then check the roles, if the role is ok then return the auth object
        //else return null

        if(user.getPwd().equals(userPassword)) {
            //UserDTO logedIn = userController.loginUser(authentication);
            final List<GrantedAuthority> grantedAuths = new ArrayList<>();
            grantedAuths.add(new SimpleGrantedAuthority("ROLE_USER"));
            final UserDetails principal = new User(user.getName(), user.getPwd(), grantedAuths);
            final Authentication auth = new UsernamePasswordAuthenticationToken(principal, userPassword, grantedAuths);
            return auth;
        } else {
            return null;
        }

        /*
        if (email.equals("filip@asdn.ie") && password.equals("system")) {
            final List<GrantedAuthority> grantedAuths = new ArrayList<>();
            grantedAuths.add(new SimpleGrantedAuthority("ROLE_USER"));
            final UserDetails principal = new User(name, password, grantedAuths);
            final Authentication auth = new UsernamePasswordAuthenticationToken(principal, password, grantedAuths);
            return auth;
        */
    }

    @Override
    public boolean supports(final Class<?> authentication) {
        return authentication.equals(UsernamePasswordAuthenticationToken.class);
    }
}
