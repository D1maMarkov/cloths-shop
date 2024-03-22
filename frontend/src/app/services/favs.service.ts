import { Observable, catchError, throwError, BehaviorSubject } from 'rxjs';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { HttpErrorResponse } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { ErrorService } from "./error.service";
import { IProduct } from '../models/product';
import { GlobalSettingsService } from './global-settings.service';

@Injectable({
  providedIn: 'root'
})
export class FavsService implements OnInit{
  len: number = 0;
  products = new BehaviorSubject<IProduct[]>([]);
  host: string;

  httpOptions = {
    withCredentials: true
  };

  constructor(
    private http: HttpClient,
    private errorService: ErrorService,
    private global: GlobalSettingsService,
  ){
    this.host = this.global.host + 'favs';
    this.getFavs().subscribe(products => {
      this.products.next([...products]);
    })
    this.products.subscribe(products => {
      this.len = products.length;
    })
  }

  getFavs(): Observable<IProduct[]>{
    return this.http.get<IProduct[]>(this.host + '/get', {
          withCredentials: true
    }).pipe(
        catchError(this.errorHandler.bind(this))
    )
  }

  private errorHandler(error: HttpErrorResponse){
    this.errorService.handle(error.message)
    return throwError(() => error.message)
  }

  addInSession(product: IProduct){
    const httpOptions = {
      ...this.httpOptions,
      headers: new HttpHeaders({
          'accept': 'application/json',
          'Content-Type': 'application/json',
      })
    };

    this.http.post(this.host + '/add', product, httpOptions).subscribe()
  }

  removeFromSession(id: number){
    this.http.get(this.host + `/remove/${id}`, this.httpOptions).subscribe()
  }

  addProduct(product: IProduct){
    const products = this.products.getValue()
    this.products.next([...products, product]);
    this.addInSession(product);
  }

  removeProduct(id: number){
    this.products.next([...this.products.getValue().filter(product => product.id !== id)]);
    this.removeFromSession(id);
  }

  ngOnInit(): void {
  }

  isInFavs(id: number){
    let isIn = false;
    this.products.getValue().forEach(product => {
      if (product.id === id){
        isIn = true;
      }
    })

    return isIn;
  }
}