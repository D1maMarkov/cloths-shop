import { BehaviorSubject } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class JwtProcessorService{
  token = new BehaviorSubject<string>(this.getToken());

  setToken(token: string): void{
    const encodedToken = encodeURIComponent(token);
    this.token.next(encodedToken);

    localStorage.setItem("token", JSON.stringify(encodedToken))
  }

  getToken(): string{
    const raw = localStorage.getItem("token");

    if (raw !== null){
      return JSON.parse(raw);
    }
    return '';
  }

  resetToken(): void{
    this.setToken("");
  }
}
