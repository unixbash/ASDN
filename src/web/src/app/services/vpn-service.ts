import {Injectable} from '@angular/core';
import {Headers, Http, RequestOptions, Response} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import {VPN} from '../models/vpn';

@Injectable()
export class VpnService{
    constructor (private http: Http) {}
    ENDPOINT = "http://localhost:8080/vpn/";

  getCustomerVpn(username: string, token: string): Observable<VPN> {
    let headers = new Headers();
    let auth = btoa(username + ":" + token);
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Basic ' + auth)
    let options = new RequestOptions({headers: headers});
    return this.http.get(this.ENDPOINT + "username", options)
                                 .map((res:Response) => res.json())
                                 .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

    }

  createVPN(body: Object, username: string, token: string): Observable<VPN> {
    let bodyString = JSON.stringify(body);
    let headers = new Headers();
    let auth = btoa(username + ":" + token);
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Basic ' + auth)
    let options = new RequestOptions({headers: headers});

    return this.http.post(this.ENDPOINT, body, options)
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
  }
}
