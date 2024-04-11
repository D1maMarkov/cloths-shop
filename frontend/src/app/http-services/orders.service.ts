import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import { GlobalSettingsService } from '../services/global-settings.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TypeOrder } from '../models/order';
import { TypeCreateOrder } from '../models/order';
import { HttpBaseService } from './base-http-service.service';
import { ErrorService } from '../services/error.service';

@Injectable({
  providedIn: 'root'
})
export class OrdersService extends HttpBaseService{
  constructor(
    private authService: AuthService,
    global: GlobalSettingsService,
    errorService: ErrorService,
    http: HttpClient
  ) {
    super(http, errorService, global);
    this.host = this.host + 'orders';
  }

  place(data: TypeCreateOrder): void{
    this.http.post(this.host, data, this.authService.httpOptions).subscribe();
  }

  getOrders(): Observable<TypeOrder[]>{
    return this.http.get<TypeOrder[]>(this.host, this.authService.httpOptions);
  }
}
