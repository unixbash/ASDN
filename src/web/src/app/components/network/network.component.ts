import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class NetworkComponent implements OnInit {

  constructor() {}

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