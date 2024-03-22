import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { TypeDataFilter } from '../models/filter';
import { ErrorService } from "./error.service";
import { Injectable } from '@angular/core';
import { GlobalSettingsService } from './global-settings.service';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  brands$ = new Observable<TypeDataFilter[]>;
  sizes$ = new Observable<TypeDataFilter[]>;
  categories$ = new Observable<TypeDataFilter[]>;
  accessoriesCategories$ = new Observable<TypeDataFilter[]>;
  colors$ = new Observable<TypeDataFilter[]>;
  priceRange$ = new Observable<number[]>;

  host: string;

  constructor(
    private http: HttpClient,
    private errorService: ErrorService,
    private global: GlobalSettingsService,
  ){
    this.host = this.global.host;
    this.getBrands();
    this.getSizes();
    this.getCategories();
    this.getAccessoriesCategories();
    this.getColors();
  }

  private errorHandler(error: HttpErrorResponse){
    this.errorService.handle(error.message)
    return throwError(() => error.message)
  }

  getPriceRange(): Observable<number[]>{
    return this.http.get<number[]>(this.host + 'products/price-range').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getBrands(): void{
    this.brands$ = this.http.get<TypeDataFilter[]>(this.host + 'brands').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getSizes(): void{
    this.sizes$ = this.http.get<TypeDataFilter[]>(this.host + 'products/sizes').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getCategories(): void{
    this.categories$ = this.http.get<TypeDataFilter[]>(this.host + 'categories').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getAccessoriesCategories(): void{
    this.accessoriesCategories$ = this.http.get<TypeDataFilter[]>(this.host + 'categories/accessories').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getColors(): void{
    this.colors$ = this.http.get<TypeDataFilter[]>(this.host + 'products/colors').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }
}
