import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class NetworkComponent implements OnInit {

  constructor() {}
  portImg: string = "/assets/port.png";
  states: string[] = [
    "/assets/port.png",
    "/assets/port-ok.png",
    "/assets/port-alert.png",
    "/assets/port-error.png"
  ];

  ports: { name:string, portStatus:string }[] = [
    {"name":"ge-0/0/0", "portStatus":this.states[0]},
    {"name":"ge-0/0/1", "portStatus":this.states[1]},
    {"name":"ge-0/0/2", "portStatus":this.states[2]},
    {"name":"ge-0/0/3", "portStatus":this.states[3]},
    {"name":"ge-0/0/4", "portStatus":this.states[1]},
    {"name":"ge-0/0/5", "portStatus":this.states[1]},
    {"name":"ge-0/0/6", "portStatus":this.states[2]},
    {"name":"ge-0/0/7", "portStatus":this.states[2]},
    {"name":"ge-0/0/8", "portStatus":this.states[1]},
    {"name":"ge-0/0/9", "portStatus":this.states[1]},
    {"name":"ge-0/0/10", "portStatus":this.states[0]},
    {"name":"ge-0/0/11", "portStatus":this.states[0]},
    {"name":"ge-0/0/12", "portStatus":this.states[0]},
    {"name":"ge-0/0/13", "portStatus":this.states[0]},
    {"name":"ge-0/0/14", "portStatus":this.states[1]},
    {"name":"ge-0/0/15", "portStatus":this.states[1]},
];

  ngOnInit() {
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