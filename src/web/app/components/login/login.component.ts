import { Component, OnInit, ViewChild, ElementRef, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class LoginComponent implements OnInit {

  public showlogin = true;
  public showRegister = false;
  public loginColor = "#337ab7";
  public registerColor = "#00bcd4";

  constructor() { }

  ngOnInit() {}

  showLoginBtn() {
    this.showlogin = true;
    this.showRegister = false;
    this.loginColor="#337ab7";
    this.registerColor = "#00bcd4";
  }

  showRegisterBtn() {
    this.showlogin = false;
    this.showRegister = true;
    this.loginColor="#00bcd4";
    this.registerColor = "#337ab7";
  }

}
