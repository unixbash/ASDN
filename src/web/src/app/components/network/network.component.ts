import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Device } from '../../models/device';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class NetworkComponent {
  constructor() {}

  device:Device = new Device();

  interfaces = this.device.interfaces;
  routes = this.device.routeInfo;
  vlans = this.device.vlanInfo;
  secDetails = this.device.securityInfo;

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