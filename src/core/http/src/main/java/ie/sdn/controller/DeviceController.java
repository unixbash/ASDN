package ie.sdn.controller;

import ie.sdn.model.*;
import ie.sdn.repository.*;
import ie.sdn.service.StorageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/device")
public class DeviceController {

    @Autowired
    DeviceRepository deviceRepository;

    @Autowired
    LanRepository lanRepository;

    @Autowired
    ServiceRepository serviceRepository;

    @Autowired
    RoutingRepository routingRepository;

    @Autowired
    InterfaceRepository interfaceRepository;


    @Autowired
    StorageService storageService;

    @GetMapping(value = "/{customerId}")
    @ResponseBody
    public List<Device> getDevices(@PathVariable String customerId) {
        List<Device> devices = deviceRepository.findAllByCustomerId("1");
        for(Device device: devices){
            device.setConfig(storageService.loadData(device.getConfig()));
            device.setConfigOld(storageService.loadData(device.getConfigOld()));
        }
        return devices;
    }

    @GetMapping(value = "/map/{customerId}")
    @ResponseBody
    public DeviceMap getDeviceMap(@PathVariable String customerId) {
        List<Device> devices = deviceRepository.findAllByCustomerId("1");
        List<Node> nodeList = new ArrayList<>();
        List<Edge> edgeList = new ArrayList<>();
        for(int i = 0 ; i< devices.size(); i++){
            nodeList.add(new Node(i + "",devices.get(i).getHostname(),"image","assets/device.png"));

            if(i != 0) {
                edgeList.add(new Edge(0 + "",i + ""));
            }
        }
        return new DeviceMap(nodeList,edgeList);
    }

    @GetMapping(value = "/lan/{deviceId}")
    @ResponseBody
    public List<Lan> getDeviceLan(@PathVariable String deviceId) {
        return lanRepository.findByDeviceId(deviceId);
    }

    @GetMapping(value = "/route/{deviceId}")
    @ResponseBody
    public List<Routing>  getDeviceRouting(@PathVariable String deviceId) {
        return routingRepository.findByDeviceId(deviceId);
    }

    @GetMapping(value = "/service/{deviceId}")
    @ResponseBody
    public List<Service> getDeviceService(@PathVariable String deviceId) {
        return serviceRepository.findByDeviceId(deviceId);
    }

    @GetMapping(value = "/interface/{deviceId}")
    @ResponseBody
    public Interface getDeviceInterface(@PathVariable String deviceId) {
        return interfaceRepository.findByDeviceId(deviceId);
    }
}
