package ie.sdn.controller;

import ie.sdn.dto.ApplicationDTO;
import ie.sdn.model.Activity;
import ie.sdn.model.Application;
import ie.sdn.repository.ActivityRepository;
import ie.sdn.repository.ApplicationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/activity")
public class ActivityController {

    @Autowired
    ActivityRepository activityRepository;

    @GetMapping(value = "/{id}")
    @ResponseBody
    public Activity getActivity(@PathVariable String id) {
        return activityRepository.findByCustomerId(id);
    }

    @PutMapping(value = "/{id}")
    @ResponseBody
    public ApplicationDTO updateActivity(@PathVariable String id, @RequestBody String activityString) {
        Activity activity = activityRepository.findByCustomerId(id);
        activity.setActivity(activityString);
        activityRepository.save(activity);
        return null;
    }
}
