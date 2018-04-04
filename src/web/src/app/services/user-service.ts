import { Injectable }     from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';
import { User } from '../models/user';
import { UserToken } from '../models/usertoken';

@Injectable()
export class UserService{
    constructor (private http: Http) {}
    ENDPOINT = "http://localhost:8080/user/";

    loginUser(user:User) : Observable<UserToken> {
        console.log(user);
        let headers     = new Headers({ 'Content-Type': 'application/json','Authorization': 'Basic ' + btoa(user.email + ':' + user.pwd)}); 
        let options     = new RequestOptions({ headers: headers }); 
        console.log(options);
        return this.http.get(this.ENDPOINT + "login",options)
                        .map((res:Response) => res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    registerUser (body:Object): Observable<User> {
        let bodyString  = JSON.stringify(body);
        let headers     = new Headers({ 'Content-Type': 'application/json' }); 
        let options     = new RequestOptions({ headers: headers }); 
        return this.http.post(this.ENDPOINT, body,options) 
                         .map((res:Response) => res.json())
                         .catch((error:any) => Observable.throw(error.json().error || 'Server error')); 
    }   
}