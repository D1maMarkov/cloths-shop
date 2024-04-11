import { HttpClient } from "@angular/common/http";
import { Observable, catchError } from 'rxjs';
import { GlobalSettingsService } from "../services/global-settings.service";
import { ICartProduct } from 'src/app/models/product';
import { ErrorService } from "../services/error.service";
import { Injectable } from '@angular/core';
import { HttpBaseService } from "./base-http-service.service";

@Injectable({
  providedIn: 'root'
})
export class HttpCartService extends HttpBaseService{
  constructor(
    http: HttpClient,
    errorService: ErrorService,
    global: GlobalSettingsService,
  ){
    super(http, errorService, global)
    this.host = this.host + 'cart'
  }

  getCart(): Observable<ICartProduct[]>{
    return this.http.get<ICartProduct[]>(this.host, this.httpOptions).pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  clearSession(): void{
    this.http.get(this.host + '/clear', this.httpOptions).subscribe();
  }

  addInSession(product: ICartProduct){
    this.http.post(this.host + '/add', product, this.httpOptions).subscribe()
  }

  lowQuantityInSession(product: ICartProduct){
    this.http.post(this.host + `/low-quantity`, product, this.httpOptions).subscribe()
  }
}
