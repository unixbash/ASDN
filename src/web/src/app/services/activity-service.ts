import {Injectable} from '@angular/core';
import {Headers, Http, RequestOptions, Response} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import {VPN} from '../models/vpn';
import { ServerActivity } from '../models/device';

@Injectable()
export class ActivityService{
    constructor (private http: Http) {}
    ENDPOINT = "http://localhost:8080/activity/";

  getCustomerActivity(username: string, token: string): Observable<ServerActivity> {
    let headers = new Headers();
    let auth = btoa(username + ":" + token);
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Basic ' + auth)
    let options = new RequestOptions({headers: headers});
    return this.http.get(this.ENDPOINT + "1", options)
                                 .map((res:Response) => res.json())
                                 .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

    }
}
