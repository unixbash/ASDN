package ie.sdn.config;

import ie.sdn.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.authentication.configurers.GlobalAuthenticationConfigurerAdapter;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class AuthenticationConfig extends GlobalAuthenticationConfigurerAdapter {

    private @Autowired
    UserService userService;

    @Bean
    public DaoAuthenticationProvider authProvider() {
        final DaoAuthenticationProvider authProvider = new DaoAuthenticationProvider();
        authProvider.setUserDetailsService(getUserDetailsService());
        authProvider.setPasswordEncoder(getPasswordEncoder());
        return authProvider;
    }
    @Bean
    public UserDetailsService getUserDetailsService() {

        return  id -> (UserDetails) userService.stream()
                .filter(currentID -> currentID.equals(id))
                .findAny()
                .orElseThrow(() -> new UsernameNotFoundException(
                        "Could not find the user '" + id + "'"
                ));
    }
    @Bean
    public PasswordEncoder getPasswordEncoder() {
        return new BCryptPasswordEncoder();
    }
    @Override
    public void init(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(getUserDetailsService())
                .passwordEncoder(getPasswordEncoder());
    }
}