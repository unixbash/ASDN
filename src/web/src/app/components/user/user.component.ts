import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Title } from '@angular/platform-browser/src/browser/title';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class UserComponent {

  firstName:string;
  lastName:string;
  email:string;
  passwords:string[];
  posts:Post[];
  
  constructor(private dataService:DataService) {
    
  }

  ngOnInit() {}
  
}

interface Post{
  id:number,
  title:string,
  body:string,
  userID:number
}
