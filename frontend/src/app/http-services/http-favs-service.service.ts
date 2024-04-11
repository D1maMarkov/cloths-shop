import { Observable, catchError } from 'rxjs';
import { HttpClient } from "@angular/common/http";
import { Injectable } from '@angular/core';
import { ErrorService } from '../services/error.service';
import { ICatalogProduct } from '../models/product';
import { GlobalSettingsService } from '../services/global-settings.service';
import { HttpBaseService } from './base-http-service.service';

@Injectable({
  providedIn: 'root'
})
export class HttpFavsService extends HttpBaseService{
  constructor(
    http: HttpClient,
    errorService: ErrorService,
    global: GlobalSettingsService,
  ){
    super(http, errorService, global)
    this.host = this.host + 'favs';
  }

  getFavs(): Observable<ICatalogProduct[]>{
    return this.http.get<ICatalogProduct[]>(this.host, this.httpOptions).pipe(
        catchError(this.errorHandler.bind(this))
    )
  }

  addInSession(product: ICatalogProduct){
    this.http.post(this.host, product, this.httpOptions).subscribe()
  }

  removeFromSession(id: number){
    this.http.get(this.host + `/remove/${id}`, this.httpOptions).subscribe()
  }
}
