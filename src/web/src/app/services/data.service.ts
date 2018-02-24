import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
//import { get } from 'http';
import { post } from 'selenium-webdriver/http';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {

  constructor() { 
    console.log("DataService connected!");
  }

  getPosts() {
    //return this.http.get('https://jsonplaceholder.typicode.com/posts')
    //  .map(res => res.json());
  }
}