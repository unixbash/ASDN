package ie.sdn.controller;

import ie.sdn.model.Vpn;
import ie.sdn.repository.VpnRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/vpn")
public class VpnController {

    @Autowired
    VpnRepository vpnRepository;

    @GetMapping(value = "/{id}")
    @ResponseBody()
    public Vpn getVpn(@PathVariable String id){
        return vpnRepository.findByCustomerId("1");
    }

    @PostMapping()
    @ResponseBody()
    public Vpn createVpn(@RequestBody Vpn vpnToCreate){
        Vpn v = vpnRepository.save(vpnToCreate);
        return v;
    }
}
