import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { TypeDataField, TypePriceRange } from '../models/filter';
import { ErrorService } from "./error.service";
import { Injectable } from '@angular/core';
import { GlobalSettingsService } from './global-settings.service';


@Injectable({
  providedIn: 'root'
})
export class DataService {
  brands$ = new Observable<TypeDataField[]>;
  sizes$ = new Observable<TypeDataField[]>;
  categories$ = new Observable<TypeDataField[]>;
  accessoriesCategories$ = new Observable<TypeDataField[]>;
  colors$ = new Observable<TypeDataField[]>;
  priceRange$ = new Observable<TypePriceRange>;

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

  getPriceRange(): Observable<TypePriceRange>{
    return this.http.get<TypePriceRange>(this.host + 'products/price-range').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getBrands(): void{
    this.brands$ = this.http.get<TypeDataField[]>(this.host + 'brands').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getSizes(): void{
    this.sizes$ = this.http.get<TypeDataField[]>(this.host + 'additional-for-products/sizes').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getCategories(): void{
    this.categories$ = this.http.get<TypeDataField[]>(this.host + 'categories').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getAccessoriesCategories(): void{
    this.accessoriesCategories$ = this.http.get<TypeDataField[]>(this.host + 'categories/accessories').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  getColors(): void{
    this.colors$ = this.http.get<TypeDataField[]>(this.host + 'additional-for-products/colors').pipe(
      catchError(this.errorHandler.bind(this))
    )
  }
}
