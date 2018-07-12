import {Injectable} from '@angular/core';
import {Headers, Http, RequestOptions, Response} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import {VPN} from '../models/vpn';
import { ServerDevice, Service, Lan, Routing, Interface } from '../models/device';

@Injectable()
export class DeviceService{
    constructor (private http: Http) {}
    ENDPOINT = "http://localhost:8080/device/";

  getCustomerDevice(username: string, token: string): Observable<ServerDevice[]> {
    let headers = new Headers();
    let auth = btoa(username + ":" + token);
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Basic ' + auth)
    let options = new RequestOptions({headers: headers});
    return this.http.get(this.ENDPOINT + "username", options)
                                 .map((res:Response) => res.json())
                                 .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

    }

    getDeviceLan(username: string, token: string, deviceId:string): Observable<Lan[]> {
        let headers = new Headers();
        let auth = btoa(username + ":" + token);
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Basic ' + auth)
        let options = new RequestOptions({headers: headers});
        return this.http.get(this.ENDPOINT + "lan/" + deviceId, options)
                                     .map((res:Response) => res.json())
                                     .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    
        }

    getDeviceService(username: string, token: string,deviceId:string): Observable<Service[]> {
        let headers = new Headers();
        let auth = btoa(username + ":" + token);
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Basic ' + auth)
        let options = new RequestOptions({headers: headers});
        return this.http.get(this.ENDPOINT + "service/" + deviceId, options)
                                        .map((res:Response) => res.json())
                                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    
        }

    getDeviceRouting(username: string, token: string,deviceId:string): Observable<Routing[]> {
        let headers = new Headers();
        let auth = btoa(username + ":" + token);
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Basic ' + auth)
        let options = new RequestOptions({headers: headers});
        return this.http.get(this.ENDPOINT + "route/" + deviceId, options)
                                        .map((res:Response) => res.json())
                                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

        }

    getDeviceInterfaces(username: string, token: string,deviceId:string): Observable<Interface> {
        let headers = new Headers();
        let auth = btoa(username + ":" + token);
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Basic ' + auth)
        let options = new RequestOptions({headers: headers});
        return this.http.get(this.ENDPOINT + "interface/" + deviceId, options)
                                        .map((res:Response) => res.json())
                                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

        }
}
