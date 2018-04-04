import { Component, OnInit, ViewChild, ElementRef, ViewEncapsulation, NgModule } from '@angular/core';
import { UserService } from '../../services/user-service';
import { User } from '../../models/user';
import {NgForm} from '@angular/forms';
import { UserToken } from '../../models/usertoken';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class LoginComponent {

  public showlogin = true;
  public showRegister = false;
  public loginColor = "#337ab7";
  public registerColor = "#00bcd4";
  public user:User;
  public userToken:UserToken;

  constructor(private userService:UserService) {}

  ngOnInit() {
    this.user = new User();
  }

  onLogin(loginForm: NgForm) {
    this.user.email = loginForm.value.loginEmail;
    this.user.pwd = loginForm.value.loginPwd;

    this.userService.loginUser(this.user)
    .subscribe(
      userToken => {
        this.userToken = userToken;
        console.log(userToken);
        if(userToken != null){
          window.location.href='http://localhost:4200/dashboard';
        }
      });
      err => console.log(err);
  }

  onRegister(registerForm: NgForm) {
    this.user.name = registerForm.value.fName;
    this.user.email = registerForm.value.email;
    this.user.pwd = registerForm.value.password;

    this.userService.registerUser(this.user)
    .subscribe(
      user => {
        this.user = user
        if(user != null){
          window.location.href='http://localhost:4200/';
        }
      });
      err => console.log(err);
    
  }

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
