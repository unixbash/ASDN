package ie.sdn.security;

import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import java.util.ArrayList;
import java.util.List;

import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

public class AuthProvider  implements AuthenticationProvider{

    public AuthProvider() {
        super();
    }

    // API
    /*Check username and password against the ones stored in the DB*/
    @Override
    public Authentication authenticate(final Authentication authentication) throws AuthenticationException {
        //get user from db
        
        //validate password is ok --> hash what comes in and match against hash password stored
        //If validated then check the roles, if the role is ok then return the auth object
        //else return null
        final String name = authentication.getName();
        final String password = authentication.getCredentials().toString();
        if (name.equals("admin") && password.equals("system")) {
            final List<GrantedAuthority> grantedAuths = new ArrayList<>();
            grantedAuths.add(new SimpleGrantedAuthority("ROLE_USER"));
            final UserDetails principal = new User(name, password, grantedAuths);
            final Authentication auth = new UsernamePasswordAuthenticationToken(principal, password, grantedAuths);
            return auth;
        } else {
            return null;
        }
    }

    @Override
    public boolean supports(final Class<?> authentication) {
        return authentication.equals(UsernamePasswordAuthenticationToken.class);
    }


}
