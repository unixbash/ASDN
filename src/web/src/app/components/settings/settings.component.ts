import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { LocalStorageService } from 'angular-2-local-storage';
import { VpnService } from '../../services/vpn-service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class SettingsComponent implements OnInit {

  constructor(
    private localStorageService: LocalStorageService,
    private vpnService: VpnService
  ) { }

  getCustomerVPN(){
    this.vpnService.getCustomerVpn(this.localStorageService.get("user"),this.localStorageService.get("token")).subscribe(
      gotVpn => {
        console.log(gotVpn)
      });
  err => console.log(err);
  }
  ngOnInit(): void {
    if(this.localStorageService.get("token") == null){
      window.location.href='http://localhost:4200/login';
    }
    this.getCustomerVPN();
  }

}
