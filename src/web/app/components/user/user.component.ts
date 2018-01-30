import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Title } from '@angular/platform-browser/src/browser/title';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class UserComponent implements OnInit {

  userID:number;
  firstName:string;
  lastName:string;
  companyName:string;
  email:string;
  passwords:string[];
  posts:Post[];
  
  constructor(private dataService:DataService) {
    
  }

  ngOnInit() {
    //console.log("ngOnInit initialised");
    this.firstName = "Filip";
    this.userID = 20;
    this.email = "filip.nikolic@agilenetworks.ie";
    this.passwords = ["password123","password321"];

    
  }

  register() {
    console.log("Registered");
  }
  
}

interface Post{
  id:number,
  title:string,
  body:string,
  userID:number
}
