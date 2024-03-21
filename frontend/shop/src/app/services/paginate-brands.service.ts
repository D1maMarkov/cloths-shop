import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, throwError, catchError } from 'rxjs';
import { ErrorService } from './error.service';
import { TypeBrand } from '../models/brands';
import { Injectable } from '@angular/core';
import { GlobalSettingsService } from './global-settings.service';

@Injectable({
  providedIn: 'root'
})
export class PaginateBrandsService {
  brands$ = new Observable<TypeBrand[]>;
  host: string;

  constructor(
    private http: HttpClient,
    private errorService: ErrorService,
    private global: GlobalSettingsService,
  ){
    this.host = this.global.host + 'brands';
    this.brands$ = this.getBrands();
  }

  private errorHandler(error: HttpErrorResponse){
    this.errorService.handle(error.message)
    return throwError(() => error.message)
  }

  getBrands(): Observable<TypeBrand[]>{
    return this.http.get<TypeBrand[]>(this.host + '/paginate-brands').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }
}
