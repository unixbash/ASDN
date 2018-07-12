import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { LocalStorageService } from 'angular-2-local-storage';
import { UserService } from '../../services/user-service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class NavComponent implements OnInit {

  constructor(private localStorageService: LocalStorageService, private userService: UserService) { }

  logoutUser(){

    this.userService.logoutUser(this.localStorageService.get("user"), this.localStorageService.get("token"))
      .subscribe(
        returnedToken => {
          console.log(returnedToken)
          this.localStorageService.clearAll();
          window.location.href='http://localhost:4200/login';
        });
    err => console.log(err);
    
  }
  ngOnInit() {

  }

}
