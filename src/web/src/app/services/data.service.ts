import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';
import { post } from 'selenium-webdriver/http';
import { Device } from '../models/device';
import { DevicesStatusToken } from '../models/device';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {
  ENDPOINT = "http://localhost:8080/devstatus";

  constructor(private http: Http) { }
   ngOnInit() {
      this.http.get(this.ENDPOINT).
      map((response) => response.json()).
      subscribe((data) => console.log(data))
   }
}