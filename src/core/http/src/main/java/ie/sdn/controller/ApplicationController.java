package ie.sdn.controller;

import ie.sdn.dto.ApplicationDTO;
import ie.sdn.model.Application;
import ie.sdn.repository.ApplicationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/application")
public class ApplicationController {

    @Autowired
    ApplicationRepository applicationRepository;

    @GetMapping(value = "/{id}")
    @ResponseBody
    public ApplicationDTO getApplication(@PathVariable String id) {
        Application application = applicationRepository.findById(id);
        // translate your user object to the dto and return it
        return null;
    }

    @PostMapping()
    @ResponseBody
    public ApplicationDTO createApplication(@RequestBody ApplicationDTO applicationDTO) {
        //based on the dto handed in you create a user
        Application user = new Application();
        return null;
    }

    @PutMapping(value = "/{id}/token")
    @ResponseBody
    public ApplicationDTO updateApplication(@PathVariable String id, @RequestBody String token) {
        //take on what was passed in and update what you wanted in the DTO
        Application user = applicationRepository.findById(id);

        applicationRepository.save(user);
        return null;
    }

    @DeleteMapping(value = "/{id}")
    @ResponseBody
    public ApplicationDTO deleteApplication(@PathVariable String id) {
        Application user = applicationRepository.findById(id);
        return null;
    }
}
