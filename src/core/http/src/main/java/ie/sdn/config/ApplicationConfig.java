package ie.sdn.config;

import ie.sdn.security.AuthProvider;
import ie.sdn.service.EmailService;
import ie.sdn.service.UserService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ApplicationConfig {

    @Bean
    public UserService getUserService() {
        return new UserService();
    }

    @Bean
    public EmailService getEmailService() {
        return new EmailService();
    }

    @Bean
    public AuthProvider getAuthProvider() { return new AuthProvider(); }
}
