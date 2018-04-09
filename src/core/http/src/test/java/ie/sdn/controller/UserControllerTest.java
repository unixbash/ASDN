package ie.sdn.controller;

import ie.sdn.repository.UserRepository;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class UserControllerTest {

    @InjectMocks
    private UserController userController;

    @Mock
    private UserRepository userRepository;

    @Before
    public void setUp() throws Exception {
    }

    @Test
    public void loginUser() {
    }

    @Test
    public void logoutUser() {
    }

    @Test
    public void getUser() {
    }

    @Test
    public void createUser() {
    }

    @Test
    public void updateUserToken() {
    }

    @Test
    public void deleteUser() {
    }
}
