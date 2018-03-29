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
    @Autowired
    UserController userController;
    @Autowired
    PasswordEncoder passwordEncoder;

    // API
    /*Check username and password against the ones stored in the DB*/
    @Override
    public Authentication authenticate(final Authentication authentication) throws AuthenticationException {
        //Get request details
        final String userEmail = authentication.getName();
        final String userPassword = authentication.getCredentials().toString();

        //UserDTO logedIn = userController.loginUser(authentication);
        List<GrantedAuthority> grantedAuths = new ArrayList<>();
        UserDetails principal = new User(userEmail, userPassword, grantedAuths);


        if(userPassword != null) {
            //get user from db
            ie.sdn.model.User user = userRepository.findByEmail(userEmail);
            //validate password is ok --> hash what comes in and match against hash password stored
            //If validated then check the roles, if the role is ok then return the auth object
            //else return null
            if (user != null) {
                if (passwordEncoder.matches(userPassword, user.getPwd() )) {
                    //UserDTO logedIn = userController.loginUser(authentication);
                    grantedAuths.add(new SimpleGrantedAuthority("ROLE_USER"));
                    final Authentication auth = new UsernamePasswordAuthenticationToken(principal, userPassword, grantedAuths);
                    return auth;
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
        }

        return new UsernamePasswordAuthenticationToken(principal, userPassword, grantedAuths);
    }

    @Override
    public boolean supports(final Class<?> authentication) {
        return authentication.equals(UsernamePasswordAuthenticationToken.class);
    }
}
