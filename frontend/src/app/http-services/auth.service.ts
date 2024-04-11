import { AccessTokenType, isAuthResponseType, TypePayload, UserInfoType } from '../models/auth';
import { GlobalSettingsService } from '../services/global-settings.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, throwError } from 'rxjs';
import { TypeRegisterForm } from '../models/auth';
import { catchError } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { JwtProcessorService } from '../services/jwt-processor.service';
import { HttpBaseService } from './base-http-service.service';
import { ErrorService } from '../services/error.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService extends HttpBaseService{

  constructor(
    private route: Router,
    http: HttpClient,
    global: GlobalSettingsService,
    errorService: ErrorService,
    private jwtProcesor: JwtProcessorService
  ) {
    super(http, errorService, global)
    this.host = this.host + 'auth';
    this.jwtProcesor.token.subscribe(token => {
      this.httpOptions = {
        withCredentials: true,
        headers: new HttpHeaders({
          'accept': 'application/json',
          'Authorization': `Bearer ${token}`,
        })
      };
    })
  }

  async isAuth(){
    try {
      const auth = await this.http.get<isAuthResponseType>(this.host + '/is-auth', this.httpOptions).toPromise();
      return auth;
    }
    catch (error) {
      return false;
    }
  }

  async getConfirmEmailPayload(token: string){
    const payload = await this.http.get<TypePayload>(this.host + `/confirm-email/${token}`).toPromise();
    return payload;
  }

  activateUser(user_id: number){
    this.http.get<AccessTokenType>(this.host + `/activate-user/${user_id}`).subscribe(response => {
      const token = response.access_token;

      this.jwtProcesor.setToken(token);
      this.route.navigate(["/profile"])
    });
  }

  getAccessToken(formData: FormData, error: BehaviorSubject<string>): void{
    this.http.post<AccessTokenType>(this.host + '/token', formData).pipe(
      catchError(err => {
        error.next("Неверное имя пользоваеля или пароль");
        return throwError(() => err.message)
      })
    ).subscribe(response => {
      const token = response.access_token;

      this.jwtProcesor.setToken(token);
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
    const userInfo = await this.http.get<UserInfoType>('http://127.0.0.1:8000/user/get-info', this.httpOptions).toPromise();
    return userInfo;
  }

  logout(): void{
    this.jwtProcesor.setToken("");
    this.route.navigate(["/"])
  }
}
