import { Injectable }     from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';
import { User } from '../models/user';

@Injectable()
export class UserService{
    constructor (private http: Http) {}
    ENDPOINT = "http://localhost:8080/";

    loginUser(user:User) : Observable<User> {
        let headers     = new Headers({ 'Authorization': 'Basic ' + btoa(user.email + ':' + user.pwd)}); 
        let options     = new RequestOptions({ headers: headers }); 
        return this.http.get(this.ENDPOINT + "user/login")
                        .map((res:Response) => res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    registerUser (body:Object): Observable<User> {
        let bodyString  = JSON.stringify(body);
        let headers     = new Headers({ 'Content-Type': 'application/json' }); 
        let options     = new RequestOptions({ headers: headers }); 
        return this.http.post(this.ENDPOINT + "user/create", body) 
                         .map((res:Response) => res.json())
                         .catch((error:any) => Observable.throw(error.json().error || 'Server error')); 
    }   
}