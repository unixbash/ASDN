import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class AccountComponent implements OnInit {

  constructor(private dataService:DataService) { 
    
  }

  ngOnInit() {
  }

}
