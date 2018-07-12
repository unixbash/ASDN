import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Input , NgZone } from '@angular/core';
import { Router } from '@angular/router';
import { Device, ServerDevice } from '../../models/device';
import { LocalStorageService } from 'angular-2-local-storage';
import { DeviceService } from '../../services/device-service';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class NetworkComponent implements OnInit{
  constructor(
    private localStorageService:LocalStorageService,
    private deviceService:DeviceService,
    private zone: NgZone, private router: Router) {

    //exposing component to the outside here
    //componentFn called from outside and it in return calls callExampleFunction()
            window['angularComponentReference'] = {
                zone: this.zone,
                componentFn: (value) => this.updateMap(value),
                component: this,
            }
    };
        

  device:Device = new Device();
  deviceName:string;
  lanHashmap = new Map<string, number>(); 
  routeHashmap= new Map<string, number>(); 
  serviceHashmap= new Map<string, number>(); 
  
  devices: Object[];
  deviceList: ServerDevice[];
  interfaceList: Object[];
  serviceList: Object[];
  lanList: Object[];
  routeList: Object[];

  interfaces = this.device.interfaces;
  routes = this.device.routeInfo;
  vlans = this.device.vlanInfo;
  secDetails = this.device.securityInfo;

  lanDataSource = {
    "chart": {
    "caption": "Network Location",
    "palettecolors":"#607d8b, #8b6e60, #8b8460, #f3b49f, #7d608b",
    "showLegend": "1"
    },
    "data": []
  }

  routeDataSource = {
    "chart": {
    "caption": "Network Location",
    "palettecolors":"#607d8b, #8b6e60, #8b8460, #f3b49f, #7d608b",
    "showLegend": "1"
    },
    "data": []
  }

  serviceDataSource = {
    "chart": {
    "caption": "Network Location",
    "palettecolors":"#607d8b, #8b6e60, #8b8460, #f3b49f, #7d608b",
    "showLegend": "1"
    },
    "data": []
}

  ngOnInit(): void {
    if(this.localStorageService.get("token") == null){
      window.location.href='http://localhost:4200/login';
    }
    this.devices = new Array();
    this.deviceList = new Array();
    this.getDevices();
  }

  updateMap(value:number){
    this.deviceName = this.deviceList[value].hostname;
    console.log(this.deviceList[value])
    this.routeDataSource.data  = new Array();
    this.lanDataSource.data  = new Array();
    this.serviceDataSource.data = new Array();
    this.lanHashmap = new Map<string, number>(); 
    this.routeHashmap= new Map<string, number>(); 
    this.serviceHashmap= new Map<string, number>(); 
    this.interfaceList = [];

    this.getDeviceLan(this.deviceList[value].id);
    this.getDeviceRouting(this.deviceList[value].id);
    this.getDeviceService(this.deviceList[value].id);
    this.getDeviceInterfaces(this.deviceList[value].id);
  }

  getDeviceLan(deviceId:string){
    this.deviceService.getDeviceLan(this.localStorageService.get("user"), this.localStorageService.get("token"), deviceId)
    .subscribe(
      deviceLan => {
        console.log(deviceLan)
        this.lanList = new Array();
        for(let i = 0; i < deviceLan.length; i++){
          let count =  this.routeHashmap.get(deviceLan[i].name);
          if (count == null){
            count = 0;
          }
          this.lanHashmap.set(deviceLan[i].name, count + 1);
          this.lanList.push(deviceLan[i]);
        }
        this.lanHashmap.forEach((value: number, key: string) => {
          this.lanDataSource.data.push( {"label": key, "value":this.lanHashmap.get(key) + ""});
        });
      });
      err => console.log(err);
  }

  getDeviceRouting(deviceId:string){
    this.deviceService.getDeviceRouting(this.localStorageService.get("user"), this.localStorageService.get("token"), deviceId)
    .subscribe(
      deviceRouting => {
        console.log(deviceRouting)
        this.routeList = new Array();
        for(let i = 0; i < deviceRouting.length; i++){
          let count =  this.routeHashmap.get(deviceRouting[i].type);
          if (count == null){
            count = 0;
          }
          console.log(count);
          this.routeHashmap.set(deviceRouting[i].type, count + 1);
          this.routeList.push(deviceRouting[i]);
        }
        this.routeHashmap.forEach((value: number, key: string) => {
          this.routeDataSource.data.push( {"label": key, "value":this.routeHashmap.get(key) + ""});
        });
        console.log(this.routeHashmap)

        console.log(this.routeDataSource)
      });
      err => console.log(err);
  }

  getDeviceService(deviceId:string){
    this.deviceService.getDeviceService(this.localStorageService.get("user"), this.localStorageService.get("token"), deviceId)
    .subscribe(
      deviceService => {
        console.log(deviceService)

        this.serviceList = new Array();
        for(let i = 0; i < deviceService.length; i++){
          let count =  this.serviceHashmap.get(deviceService[i].traversing);
          if (count == null){
            count = 0;
          }
          this.serviceHashmap.set(deviceService[i].traversing, count + 1);
          this.serviceList.push(deviceService[i]);
        }
        this.serviceHashmap.forEach((value: number, key: string) => {
          this.serviceDataSource.data.push( {"label": key, "value":this.serviceHashmap.get(key) + ""});
        });
      });
      err => console.log(err);
  }

  getDeviceInterfaces(deviceId:string){
    this.deviceService.getDeviceInterfaces(this.localStorageService.get("user"), this.localStorageService.get("token"), deviceId)
    .subscribe(
      deviceInterfaces => {
        console.log(deviceInterfaces)
        let interfaceArray = deviceInterfaces.interfaces.split(",");
        this.interfaceList = new Array();
        for(let i = 0; i < interfaceArray.length; i++){
          let currentInterface = interfaceArray[i].split(":");
          this.interfaceList.push({"name":currentInterface[0],"portStatus":currentInterface[1]})
        }
      });
      err => console.log(err);
  }

  getDevices(){
    this.deviceService.getCustomerDevice(this.localStorageService.get("user"), this.localStorageService.get("token"))
    .subscribe(
      deviceList => {
          let unsupported = 0;
          let online = 0;
          let offline = 0;
          let unconfigured = 0;
          let warning = 0;
          for(let i = 0; i < deviceList.length; i++){
              if(deviceList[i].status == "unsupported"){
                  unsupported++;
              }
              else if(deviceList[i].status == "online"){
                  
                  online++;
              }
              else if(deviceList[i].status == "offline"){
                  offline++;
              }
              else if(deviceList[i].status == "unconfigured"){
                  unconfigured++;
              }
              else if(deviceList[i].status == "warning"){
                  warning++;
              }
              this.devices.push({"name": deviceList[i].hostname + ""});
              this.deviceList.push(deviceList[i])
          }
          this.deviceName = deviceList[0].hostname;
          console.log(deviceList[0])
          this.getDeviceLan(deviceList[0].id);
          this.getDeviceRouting(deviceList[0].id);
          this.getDeviceService(deviceList[0].id);
          this.getDeviceInterfaces(deviceList[0].id);

      });
  err => console.log(err);
}

}

//Declare IKE details
interface VPN_ikeDetails{
  ikePubAddress:string,
  privateAddress:string,
  ikeAuthAlgo:string,
  authAlgo:string,
  encryptionAnlgo:string,
  dhGroup:string,
  lifetime:number,
  asciiKey:string,
  veriosn:string
}

//Declare ipsec details
interface VPN_ipsecDetails{
  encryptionAnlgo:string,
  lifetime:number,
  perfectForwardSecrecy:string
}

interface HashMap {
  [details: string] : number;
} 
