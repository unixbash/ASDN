import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { VPN1, VPN2, VPN } from '../../models/vpn';
import { VpnService } from '../../services/vpn-service';
import { LocalStorageService } from 'angular-2-local-storage';

@Component({
  selector: 'app-wizzard',
  templateUrl: './wizzard.component.html',
  styleUrls: ['./wizzard.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class WizzardComponent implements OnInit{

  rForm: FormGroup;
  vpn1Form: FormGroup;
  vpn2Form: FormGroup;
  post: any;
  publicAddress:string = '';
  privateAddress:string = '';
  public events: any[] = [];
  vpn1: VPN1;
  vpn2: VPN2;

  constructor(
    private localstorageService: LocalStorageService,
    private fb: FormBuilder,
    private vpnService: VpnService) {
  }

  constructForms(){
    this.vpn1Form = this.fb.group({
      publicAddress:  ['', [<any>Validators.required]],
      privateAddress: ['', [<any>Validators.required]],
      ikeAA: ['', [<any>Validators.required]],
      ipsecEA: ['', [<any>Validators.required]],
      dh: ['', [<any>Validators.required]],
      ikeLife: ['', [<any>Validators.required]],
      ikeSecret: ['', [<any>Validators.required]],
      ikeVer: ['', [<any>Validators.required]],

    });

    this.vpn2Form = this.fb.group({
      ikeAuth:  ['', [<any>Validators.required]],
      ipsecAuth: ['', [<any>Validators.required]],
      ipsecLife: ['', [<any>Validators.required]],
      ipsecPFS: ['', [<any>Validators.required]],
    });
    this.subscribeToFormChanges();
  }

  subscribeToFormChanges() {
    const myFormStatusChanges$ = this.vpn1Form.statusChanges;
    const myFormValueChanges$ = this.vpn1Form.valueChanges;

    myFormStatusChanges$.subscribe(x => this.events.push({event: 'STATUS_CHANGED', object: x}));
    myFormValueChanges$.subscribe(x => this.events.push({event: 'VALUE_CHANGED', object: x}));

    const myFormStatusChanges1$ = this.vpn2Form.statusChanges;
    const myFormValueChanges1$ = this.vpn2Form.valueChanges;

    myFormStatusChanges1$.subscribe(x => this.events.push({event: 'STATUS_CHANGED', object: x}));
    myFormValueChanges1$.subscribe(x => this.events.push({event: 'VALUE_CHANGED', object: x}));
  }

  save1(model: VPN1) {
    console.log(model);
    this.vpn1 = model;
  }

  save2(model: VPN2){
    console.log(model);
    this.vpn2 = model;
    this.save();
  }

  save(){

    let newVpn = new VPN();
    newVpn.id = "";
    newVpn.customerId = "1";

    newVpn.publicIp = this.vpn1.publicAddress;
    newVpn.privateSubnet = this.vpn1.privateAddress;
    newVpn.ikeAl = this.vpn1.ikeAA;
    newVpn.ipsecEnc = this.vpn1.ipsecEA;
    newVpn.dhGroup = this.vpn1.dh;
    newVpn.ikeLife = this.vpn1.ikeLife;
    newVpn.ikeSecret = this.vpn1.ikeSecret;
    newVpn.ikeVersion = this.vpn1.ikeVer;

    newVpn.ikeAuth = this.vpn2.ikeAuth;
    newVpn.ipsecAl = this.vpn2.ipsecAuth;
    newVpn.ipsecLife = this.vpn2.ipsecLife;
    newVpn.ipsecSecret = this.vpn2.ipsecPFS;

    let userName: string;
    let userToken: string;
    userName = this.localstorageService.get("user");
    userToken = this.localstorageService.get("token");

    console.log("Creating VPN Object...")
    this.vpnService.createVPN(newVpn,userName, userToken)
      .subscribe(
        createdVpn => {
          console.log(createdVpn)
        });
    err => console.log(err);
    

  }
  addPost(post) {
    this.publicAddress = post.publicAddress;
    this.privateAddress = post.privateAddress;
    
  }

  ngOnInit(){
    this.constructForms();
    
  }

}
