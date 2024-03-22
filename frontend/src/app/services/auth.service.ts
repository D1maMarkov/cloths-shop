import { AccessTokenType, isAuthResponseType, UserInfoType } from '../models/auth';
import { GlobalSettingsService } from './global-settings.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, throwError } from 'rxjs';
import { TypeRegisterForm } from '../models/auth';
import { catchError } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService{
  token = new BehaviorSubject<string>(this.getToken());
  host: string;

  httpOptions = {
    withCredentials: true,
    headers: new HttpHeaders({
      'accept': 'application/json',
      'Authorization': `Bearer ${this.token.getValue()}`,
    })
  };

  async isAuth(){
    try {
      const auth = await this.http.get<isAuthResponseType>(this.host + '/is-auth', this.httpOptions).toPromise();
      return auth;
    } 
    catch (error) {
      return false;
    }
  }

  getAccessToken(formData: FormData, error: BehaviorSubject<string>): void{
    this.http.post<AccessTokenType>(this.host + '/token', formData).pipe(
      catchError(err => {
        error.next("Неверное имя пользоваеля или пароль");
        return throwError(() => err.message)
      })
    ).subscribe(response => {
      const token = response.access_token;
      this.setToken(token);

      this.route.navigate(["/profile"])
    })
  }

  register(data: TypeRegisterForm, error: BehaviorSubject<string>): void{
    this.http.post(this.host, data, this.httpOptions).pipe(
      catchError(err => {
        if (err.status == 409){
          error.next("пользователь с таким именем уже существует")
        }
        return throwError(() => err.message)
      })
    ).subscribe(() => {
      const form = new FormData();
      form.append("username", data.username);
      form.append("password", data.password);
      this.getAccessToken(form, error);
    });
  }

  async getUserInfo(){
    const userInfo = await this.http.get<UserInfoType>(this.host + '/get-info', this.httpOptions).toPromise();
    return userInfo;
  }

  setToken(token: string): void{
    const encodedToken = encodeURIComponent(token);

    this.token.next(encodedToken);

    localStorage.setItem("token", JSON.stringify(encodedToken))
  }

  constructor(
    private route: Router,
    private http: HttpClient,
    private global: GlobalSettingsService,
  ) { 
    this.host = this.global.host + 'auth';
    this.token.subscribe(token => {
      this.httpOptions = {
        withCredentials: true,
        headers: new HttpHeaders({
          'accept': 'application/json',
          'Authorization': `Bearer ${token}`,
        })
      };
    })
  }

  getToken(): string{
    const raw = localStorage.getItem("token");
    
    if (raw !== null){
      return JSON.parse(raw);
    }
    return '';
  }

  logout(): void{
    this.setToken("");
  }
}