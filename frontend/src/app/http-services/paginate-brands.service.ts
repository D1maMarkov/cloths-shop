import { HttpClient } from '@angular/common/http';
import { Observable, catchError } from 'rxjs';
import { ErrorService } from '../services/error.service';
import { TypeBrand } from '../models/brands';
import { Injectable } from '@angular/core';
import { GlobalSettingsService } from '../services/global-settings.service';
import { HttpBaseService } from './base-http-service.service';

@Injectable({
  providedIn: 'root'
})
export class PaginateBrandsService extends HttpBaseService{
  brands$ = new Observable<TypeBrand[]>;

  constructor(
    http: HttpClient,
    errorService: ErrorService,
    global: GlobalSettingsService,
  ){
    super(http, errorService, global)
    this.host = this.host + 'brands';
    this.brands$ = this.getBrands();
  }

  getBrands(): Observable<TypeBrand[]>{
    return this.http.get<TypeBrand[]>(this.host + '/paginate-brands').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }
}
