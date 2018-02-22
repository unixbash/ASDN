import { Component, OnInit, ViewChild, ElementRef, ViewEncapsulation } from '@angular/core';
import { UserService } from '../../services/user-service';
import { User } from '../../models/user';

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
  public user:User;

  constructor(private userService:UserService) { }

  /*
  loginUser(loginEmail:string, loginPassword:string) {
    User user = new User;

    this.userService.getUser(email)
    .subscribe(
      user => {
        this.user = user
      });
      err => console.log(err);
  }
  */
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
