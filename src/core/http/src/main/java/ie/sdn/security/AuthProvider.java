package ie.sdn.security;

import ie.sdn.enums.TokenStatus;
import ie.sdn.model.Authority;
import ie.sdn.model.User;
import ie.sdn.model.UserToken;
import ie.sdn.repository.UserRepository;
import ie.sdn.repository.UserTokenRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationProvider;

import java.util.ArrayList;
import java.util.List;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.crypto.password.PasswordEncoder;

public class AuthProvider  implements AuthenticationProvider{

    public AuthProvider() {
        super();
    }
    @Autowired
    UserRepository userRepository;
    @Autowired
    UserTokenRepository userTokenRepository;
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
        List<Authority> grantedAuths = new ArrayList<>();


        if(userPassword != null) {
            //get user from db
            User user = userRepository.findByEmail(userEmail);
            //validate password is ok --> hash what comes in and match against hash password stored
            //If validated then check the roles, if the role is ok then return the auth object
            //else return null
            if (user != null) {
                if (passwordEncoder.matches(userPassword, user.getPwd() )) {
                    //UserDTO logedIn = userController.loginUser(authentication);
                    grantedAuths.add(new Authority("USER"));
                    return new UsernamePasswordAuthenticationToken(userEmail, userPassword, grantedAuths);
                }
                //Passwords may not match but are they a token we have given them?
                if(isCurrentToken(user.getId(),userPassword)){
                    //UserDTO logedIn = userController.loginUser(authentication);
                    grantedAuths.add(new Authority("USER"));
                    return new UsernamePasswordAuthenticationToken(userEmail, userPassword, grantedAuths);
                }
            }
        }

        return new UsernamePasswordAuthenticationToken(userEmail, userPassword, grantedAuths);
    }

    @Override
    public boolean supports(final Class<?> authentication) {
        return authentication.equals(UsernamePasswordAuthenticationToken.class);
    }

    private boolean isCurrentToken(String userId, String potentialToken){
        UserToken userToken = userTokenRepository.findFirstByUserIdOrderByCreatedAtDesc(userId);
        if(userToken != null) {
            return userToken.getToken().equals(potentialToken) && userToken.getStatus().equals(TokenStatus.ACTIVE.toString());
        }
        return false;
    }
}
