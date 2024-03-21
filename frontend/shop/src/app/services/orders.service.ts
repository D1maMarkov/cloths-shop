import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import { GlobalSettingsService } from './global-settings.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TypeOrder } from '../models/order';
import { TypeCreateOrder } from '../models/order';

@Injectable({
  providedIn: 'root'
})
export class OrdersService {
  host: string;

  constructor(
    private authService: AuthService,
    private global: GlobalSettingsService,
    private http: HttpClient
  ) { 
    this.host = this.global.host + 'cart';
  }

  place(data: TypeCreateOrder): void{
    this.http.post(this.host + '/create-order', data, this.authService.httpOptions).subscribe();
  }

  getOrders(): Observable<TypeOrder[]>{
    return this.http.get<TypeOrder[]>(this.host + '/get-orders', this.authService.httpOptions);
  }
}
