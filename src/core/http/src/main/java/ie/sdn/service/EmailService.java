package ie.sdn.service;
import ie.sdn.model.Mail;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

//Source https://memorynotfound.com/spring-mail-sending-simplemailmessage-javamailsender-example/
@Service
public class EmailService {

    @Autowired
    private JavaMailSender emailSender;

    public void sendRegEmail(String email){
        Mail mail = new Mail("no-reply@asdn.ie", email, "ASDN - Email Confirmation",
                "Hi, please confirm your email address.");

        SimpleMailMessage message = new SimpleMailMessage();
        message.setSubject(mail.getSubject());
        message.setText(mail.getContent());
        message.setTo(mail.getTo());
        message.setFrom(mail.getFrom());

        emailSender.send(message);
    }
}
